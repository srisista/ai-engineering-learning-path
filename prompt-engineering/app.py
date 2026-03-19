import os
from pathlib import Path

from dotenv import load_dotenv
import requests


def load_env() -> None:
    """Load environment from local .env and shared root .env (if present)."""
    load_dotenv()
    root_env = Path(__file__).resolve().parents[1] / ".env"
    if root_env.exists():
        load_dotenv(root_env, override=False)


def get_api_key() -> str:
    load_env()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("Set OPENAI_API_KEY in a .env file before running.")
    return api_key


def chat_with_pattern(user_input: str, pattern: str) -> str:
    """
    Send a prompt using one of a few prompt-engineering patterns.
    """
    api_key = get_api_key()
    base_url = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1").rstrip("/")
    model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    system_prompts = {
        "bullet_explainer": "You are a senior AI engineer. Explain concepts in concise bullet points.",
        "step_by_step": "You are a careful tutor. Always reason step by step before answering.",
        "few_shot_classifier": (
            "You are a sentiment classifier.\n"
            "Example 1:\n"
            "Text: \"I love this product.\"\n"
            "Label: positive\n\n"
            "Example 2:\n"
            "Text: \"This is terrible.\"\n"
            "Label: negative\n\n"
            "Classify the sentiment of the next text as 'positive', 'negative', or 'neutral'."
        ),
    }

    system = system_prompts.get(pattern, system_prompts["bullet_explainer"])

    url = f"{base_url}/chat/completions"
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user_input},
        ],
    }
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    response = requests.post(url, json=payload, headers=headers, timeout=30)
    response.raise_for_status()
    data = response.json()
    return data["choices"][0]["message"]["content"]


def main() -> None:
    print("Prompt Engineering Lab - 15 Minute LLM Patterns")
    print("Patterns: [1] bullet_explainer  [2] step_by_step  [3] few_shot_classifier")
    print("Type 'quit' to exit.\n")

    pattern_map = {
        "1": "bullet_explainer",
        "2": "step_by_step",
        "3": "few_shot_classifier",
    }

    while True:
        pattern_choice = input("Select pattern (1/2/3): ").strip()
        if pattern_choice.lower() in {"quit", "exit"}:
            break
        pattern = pattern_map.get(pattern_choice)
        if not pattern:
            print("Invalid choice. Please enter 1, 2, or 3.\n")
            continue

        user_input = input("Enter your prompt: ").strip()
        if user_input.lower() in {"quit", "exit"}:
            break
        if not user_input:
            continue

        try:
            answer = chat_with_pattern(user_input, pattern)
        except Exception as exc:  # noqa: BLE001
            print(f"Error calling model: {exc}")
            continue

        print(f"\n--- Model Response ({pattern}) ---")
        print(answer)
        print("\n")


if __name__ == "__main__":
    main()

