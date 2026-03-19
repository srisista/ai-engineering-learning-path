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


def draft_email(instruction: str, tone: str = "professional") -> str:
    api_key = get_api_key()
    base_url = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1").rstrip("/")
    model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    system = (
        "You are an assistant that writes clear, concise, and professional emails. "
        "Always include greeting, body, and sign-off."
    )
    user_prompt = f"Write an email with a {tone} tone based on this instruction:\n\n{instruction}"

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
    print("AI Email Writer - 15 Minute Lab")
    print("Turn bullet points into a polished email. Type 'quit' to exit.\n")

    while True:
        tone = input("Tone (professional / friendly / concise): ").strip() or "professional"
        if tone.lower() in {"quit", "exit"}:
            break

        print("Describe the email you want (bullet points or short description):")
        instruction = input("> ").strip()
        if instruction.lower() in {"quit", "exit"}:
            break
        if not instruction:
            continue

        try:
            email = draft_email(instruction, tone=tone)
        except Exception as exc:  # noqa: BLE001
            print(f"Error calling model: {exc}")
            continue

        print("\n--- Draft Email ---")
        print(email)
        print("\n")


if __name__ == "__main__":
    main()

