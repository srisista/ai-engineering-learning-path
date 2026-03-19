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


def summarize(text: str, style: str = "executive") -> str:
    api_key = get_api_key()
    base_url = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1").rstrip("/")
    model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    system = (
        "You are a professional summarization engine. "
        "Produce clear, faithful summaries optimized for busy readers."
    )
    user_prompt = f"Summarize the following text in a {style} style:\n\n{text}"

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user_prompt},
        ],
    }
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    url = f"{base_url}/chat/completions"
    response = requests.post(url, json=payload, headers=headers, timeout=30)
    response.raise_for_status()
    data = response.json()
    return data["choices"][0]["message"]["content"]


def main() -> None:
    print("AI Text Summarizer - 15 Minute Lab")
    print("Styles: [1] executive  [2] bullet  [3] short\nType 'quit' to exit.\n")

    style_map = {"1": "executive", "2": "bullet-point", "3": "short"}

    while True:
        style_choice = input("Select style (1/2/3): ").strip()
        if style_choice.lower() in {"quit", "exit"}:
            break
        style = style_map.get(style_choice, "executive")

        print("Paste text to summarize (single line) and press Enter:")
        text = input("> ").strip()
        if text.lower() in {"quit", "exit"}:
            break
        if not text:
            continue

        try:
            summary = summarize(text, style=style)
        except Exception as exc:  # noqa: BLE001
            print(f"Error calling model: {exc}")
            continue

        print("\n--- Summary ---")
        print(summary)
        print("\n")


if __name__ == "__main__":
    main()

