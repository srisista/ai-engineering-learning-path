import os
from pathlib import Path

from dotenv import load_dotenv
import requests


def load_env() -> None:
    """Load environment from local .env and shared root .env (if present)."""
    # Local .env (project-specific overrides)
    load_dotenv()
    # Shared .env at workspace root (one level up)
    root_env = Path(__file__).resolve().parents[1] / ".env"
    if root_env.exists():
        load_dotenv(root_env, override=False)


def get_api_key() -> str:
    load_env()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("Set OPENAI_API_KEY in a .env file before running.")
    return api_key


def chat_once(question: str) -> str:
    """
    Minimal OpenAI-compatible chat completion call.
    Works with providers like OpenAI or OpenRouter.
    """
    api_key = get_api_key()
    base_url = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1").rstrip("/")
    model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    url = f"{base_url}/chat/completions"
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": question},
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
    # Keep the banner ASCII-only for Windows consoles.
    print("Hello LLM - minimal chatbot")
    print("Type 'quit' to exit.\n")

    while True:
        question = input("You: ").strip()
        if not question:
            continue
        if question.lower() in {"quit", "exit"}:
            break

        try:
            answer = chat_once(question)
        except Exception as exc:  # noqa: BLE001
            print(f"Error calling model: {exc}")
            continue

        print(f"\nAssistant: {answer}\n")


if __name__ == "__main__":
    main()

