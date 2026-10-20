"""
Verify all labs: syntax check + offline smoke tests (mocked HTTP).

Usage:
    python scripts/verify_labs.py
    python scripts/verify_labs.py --report
    python scripts/verify_labs.py --live   # requires real .env API key
"""

from __future__ import annotations

import argparse
import importlib.util
import os
import py_compile
import sys
from pathlib import Path
from typing import Callable
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]

LAB_APPS = [
    "hello-llm/app.py",
    "prompt-engineering/app.py",
    "sentiment-analysis-llm/app.py",
    "ai-email-writer/app.py",
    "ai-language-translator/app.py",
    "ai-text-summarizer/app.py",
]


def load_module(app_path: Path, module_name: str):
    spec = importlib.util.spec_from_file_location(module_name, app_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load {app_path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def mock_response(*_args, **_kwargs):
    class Resp:
        def raise_for_status(self) -> None:
            return None

        def json(self):
            return {"choices": [{"message": {"content": "mock-ok"}}]}

    return Resp()


def line_count(path: Path) -> int:
    return len(path.read_text(encoding="utf-8").splitlines())


def compile_all() -> None:
    for rel in LAB_APPS:
        path = ROOT / rel
        if not path.exists():
            raise FileNotFoundError(path)
        py_compile.compile(str(path), doraise=True)


def smoke_tests() -> None:
    os.environ.setdefault("OPENAI_API_KEY", "test-key-for-offline-smoke")
    os.environ.setdefault("OPENAI_BASE_URL", "https://example.invalid/v1")
    os.environ.setdefault("OPENAI_MODEL", "test-model")

    cases: list[tuple[str, str, Callable]] = [
        ("hello-llm", "hello_llm", lambda m: m.chat_once("Hi")),
        (
            "prompt-engineering",
            "prompt_engineering",
            lambda m: m.chat_with_pattern("Explain APIs", "bullet_explainer"),
        ),
        ("sentiment-analysis-llm", "sentiment", lambda m: m.classify_sentiment("I love this.")),
        ("ai-email-writer", "email", lambda m: m.draft_email("Thank the team", tone="friendly")),
        (
            "ai-language-translator",
            "translator",
            lambda m: m.translate("Hello world", "French", tone="neutral"),
        ),
        ("ai-text-summarizer", "summarizer", lambda m: m.summarize("Long text here.", style="short")),
    ]

    with patch("requests.post", side_effect=mock_response):
        for folder, mod_name, call in cases:
            app_path = ROOT / folder / "app.py"
            mod = load_module(app_path, mod_name)
            result = call(mod)
            if result != "mock-ok":
                raise AssertionError(f"{folder}: expected mock-ok, got {result!r}")


def live_ping() -> None:
    """One real API call via hello-llm if credentials are configured."""
    from dotenv import load_dotenv

    load_dotenv(ROOT / ".env")
    key = os.getenv("OPENAI_API_KEY", "")
    if not key or "PASTE_YOUR_KEY" in key:
        print("Skipping live ping: set a real OPENAI_API_KEY in .env")
        return

    mod = load_module(ROOT / "hello-llm" / "app.py", "hello_llm_live")
    answer = mod.chat_once("Reply with exactly: LIVE_OK")
    print(f"Live hello-llm response (first 120 chars): {answer[:120]!r}")


def print_report() -> None:
    rows = []
    for rel in LAB_APPS:
        path = ROOT / rel
        rows.append((path.parent.name, line_count(path)))
    width = max(len(n) for n, _ in rows)
    print(f"{'Module':<{width}}  app.py lines")
    print("-" * (width + 16))
    for name, lines in rows:
        print(f"{name:<{width}}  {lines}")
    print("\nSee docs/MODULE-CODE-COMPARISON.md for what differs between modules.")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--report", action="store_true", help="Print line counts only")
    parser.add_argument("--live", action="store_true", help="Optional live API ping")
    args = parser.parse_args()

    if args.report:
        print_report()
        return 0

    print("Compiling lab app.py files...")
    compile_all()
    print("Running offline smoke tests (mocked HTTP)...")
    smoke_tests()
    print("All offline checks passed.")

    if args.live:
        print("Running live API ping...")
        live_ping()

    return 0


if __name__ == "__main__":
    sys.exit(main())
