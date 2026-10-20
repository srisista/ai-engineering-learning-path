"""
Compare two models on the same prompt (Model Swap lab).

Usage (from repo root with .env configured):

    cd hello-llm
    python compare_models.py "What is prompt engineering?"
    python compare_models.py "I got promoted!" --models meta-llama/llama-3.2-3b-instruct,openai/gpt-4o-mini
"""

from __future__ import annotations

import argparse
import os
import sys

from dotenv import load_dotenv
from pathlib import Path

# Reuse hello-llm's API helper
from app import chat_once


def load_root_env() -> None:
    load_dotenv()
    root_env = Path(__file__).resolve().parents[1] / ".env"
    if root_env.exists():
        load_dotenv(root_env, override=False)


def ask_with_model(question: str, model: str) -> str:
    previous = os.environ.get("OPENAI_MODEL")
    os.environ["OPENAI_MODEL"] = model
    try:
        return chat_once(question).strip()
    finally:
        if previous is None:
            os.environ.pop("OPENAI_MODEL", None)
        else:
            os.environ["OPENAI_MODEL"] = previous


def main() -> None:
    load_root_env()
    default_a = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    parser = argparse.ArgumentParser(description="Compare two LLM models on one prompt.")
    parser.add_argument("prompt", nargs="?", default="Explain sentiment analysis in one paragraph.")
    parser.add_argument(
        "--models",
        default=f"{default_a},gpt-4o-mini",
        help="Comma-separated model IDs (OpenRouter or your provider).",
    )
    args = parser.parse_args()
    models = [m.strip() for m in args.models.split(",") if m.strip()]
    if len(models) < 2:
        print("Provide at least two models via --models", file=sys.stderr)
        sys.exit(1)

    print(f"Prompt: {args.prompt}\n")
    for model in models[:2]:
        print(f"=== {model} ===")
        try:
            print(ask_with_model(args.prompt, model))
        except Exception as exc:  # noqa: BLE001
            print(f"Error: {exc}")
        print()


if __name__ == "__main__":
    main()
