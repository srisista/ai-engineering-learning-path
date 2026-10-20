# Module code comparison — what actually changes?

All Python labs follow the same architecture:

1. **Shared plumbing** (~22 lines): load root `.env`, read `OPENAI_API_KEY`, `OPENAI_BASE_URL`, `OPENAI_MODEL`.
2. **Same HTTP call** (~15 lines): `POST {base_url}/chat/completions` with `messages` = system + user.
3. **Module-specific behavior** (~10–25 lines): system prompt, user message template, CLI questions.
4. **`main()` loop** (~15–30 lines): how you interact in the terminal.

The table below is the fastest way to see *where* each lab differs.

| Lab folder | `app.py` lines | Core function | Lines that define behavior |
|------------|----------------|---------------|----------------------------|
| `hello-llm` | 76 | `chat_once` | Generic system prompt; user text passed through unchanged |
| `prompt-engineering` | 106 | `chat_with_pattern` | `system_prompts` dict (3 patterns) |
| `sentiment-analysis-llm` | 75 | `classify_sentiment` | Fixed classifier system prompt |
| `ai-email-writer` | 82 | `draft_email` | Email system prompt + `tone` in user message |
| `ai-language-translator` | 88 | `translate` | Translator system prompt + `target_lang` / `tone` in user message |
| `ai-text-summarizer` | 85 | `summarize` | Summarizer system prompt + `style` in user message |

Regenerate line counts anytime:

```bash
python scripts/verify_labs.py --report
```

---

## Shared plumbing (identical across labs)

Every `app.py` starts with the same environment helpers:

```8:22:hello-llm/app.py
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
```

The HTTP request shape is also the same; only `messages` content changes.

---

## Email writer vs language translator (the meaningful diff)

These two labs are often confused because both “transform text.” The **API call is identical**; only prompts and parameters differ.

### AI Email Writer — `draft_email`

```24:40:ai-email-writer/app.py
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
```

### AI Language Translator — `translate`

```24:41:ai-language-translator/app.py
def translate(text: str, target_lang: str, tone: str = "neutral") -> str:
    api_key = get_api_key()
    base_url = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1").rstrip("/")
    model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    system = (
        "You are a professional translator. Preserve meaning and important terminology. "
        "Adjust style to the requested tone."
    )
    user_prompt = (
        f"Translate the following text into {target_lang} with a {tone} tone.\n\n{text}"
    )

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user_prompt},
        ],
    }
```

| Aspect | Email writer | Translator |
|--------|--------------|------------|
| **System role** | Email author with greeting/sign-off | Professional translator |
| **User inputs** | `instruction` + `tone` | `text` + `target_lang` + `tone` |
| **Output shape** | Full email | Translated text |
| **Lines unique to behavior** | ~4 (system + user template) | ~4 (system + user template) |

---

## Text summarizer (same pattern, different prompt)

```24:40:ai-text-summarizer/app.py
def summarize(text: str, style: str = "executive") -> str:
    api_key = get_api_key()
    base_url = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1").rstrip("/")
    model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    system = (
        "You are a professional summarization engine. "
        "Produce clear, faithful summaries optimized for busy readers."
    )
    user_prompt = f"Summarize the following text in a {style} style:\n\n{text}"
```

---

## Sentiment analysis (classification constraint)

```24:40:sentiment-analysis-llm/app.py
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
```

User content is **raw text** (no wrapper), unlike email/translate/summarize.

---

## Prompt engineering (multiple system prompts)

The variable part is the `system_prompts` dictionary and pattern selector in `main()` — see `prompt-engineering/app.py` lines 32–45 and 72–76.

---

## Hello LLM vs model comparison

- **`hello-llm/app.py`**: interactive chat with a generic assistant system prompt.
- **`hello-llm/compare_models.py`**: reuses `chat_once` but swaps `OPENAI_MODEL` for two models on the same prompt (Model Swap lab).

---

## Mental model for learners

> **One API. Many products.** Change the system message and how you wrap the user input — that is the core skill of LLM application engineering in these labs.
