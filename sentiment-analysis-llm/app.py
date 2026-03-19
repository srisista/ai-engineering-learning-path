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


def classify_sentiment(text: str) -> str:
    api_key = get_api_key()
    base_url = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1").rstrip("/")
    model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    system = (
        "You are a sentiment analysis service. "
        "Given a piece of text, respond with a single label: "
        "'positive', 'negative', or 'neutral'."
    )

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": text},
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
    return data["choices"][0]["message"]["content"].strip()


def main() -> None:
    print("Sentiment Analysis with LLM - 15 Minute Lab")
    print("Classify text as positive / negative / neutral. Type 'quit' to exit.\n")

    while True:
        text = input("Enter text to classify: ").strip()
        if text.lower() in {"quit", "exit"}:
            break
        if not text:
            continue

        try:
            label = classify_sentiment(text)
        except Exception as exc:  # noqa: BLE001
            print(f"Error calling model: {exc}")
            continue

        print(f"Predicted sentiment: {label}\n")


if __name__ == "__main__":
    main()

