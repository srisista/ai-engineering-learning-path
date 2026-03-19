Low-Level Design: AI Language Translator
=======================================

This document describes the internals of the **ai-language-translator** 15‑minute lab.

---

## 1. Responsibilities

Primary responsibility:

> Translate English text into a target language using an LLM, while respecting a requested tone (formal, casual, neutral).

Out of scope:

- full localization pipeline (pluralization, ICU, etc.)
- persistence or glossary management beyond basic prompts

---

## 2. Components

### 2.1 User Interface Layer

- **Terminal**
  - Prompts for target language and tone.
  - Collects source text.
  - Displays translated text.

### 2.2 Application Layer (`app.py`)

- `main()`:
  - Prints a short banner.
  - Reads `target`, `tone`, and `text` from the user.
  - Calls `translate(text, target_lang, tone)`.
  - Handles exceptions from the integration layer and continues the loop.

- `translate(text, target_lang, tone)`:
  - Builds a system prompt for translation quality and style.
  - Constructs a user message specifying target language and tone.

### 2.3 Integration Layer

- **HTTP client (`requests`)**
  - Reads configuration from environment variables.
  - Sends a chat completion request to `{OPENAI_BASE_URL}/chat/completions`.
  - Parses `choices[0].message.content` as the translated text.

### 2.4 Configuration Layer

- **`.env`**
  - `OPENAI_API_KEY`
  - `OPENAI_BASE_URL`
  - `OPENAI_MODEL`
  - Loaded via `python-dotenv` inside `get_api_key()`.

---

## 3. Data Flow

```text
User enters target language, tone, and text
        │
        ▼
main()
  - call translate(text, target, tone)
        │
        ▼
translate()
  - load .env (OPENAI_*)
  - build system + user messages
  - POST to {OPENAI_BASE_URL}/chat/completions
        │
        ▼
Hosted LLM API
  - authenticate via API key
  - run model
  - return translated text in choices[0].message.content
        │
        ▼
translate()
  - return translated text
        │
        ▼
main()
  - print translation
```

---

## 4. Key Functions

### 4.1 `get_api_key() -> str`

- Loads `.env`.
- Retrieves `OPENAI_API_KEY`.
- Raises `RuntimeError` if missing.

### 4.2 `translate(text: str, target_lang: str, tone: str) -> str`

- Inputs:
  - `text`: the English source text.
  - `target_lang`: human‑readable target language name.
  - `tone`: one of `formal`, `casual`, `neutral` (freeform string).
- Behavior:
  - Embeds `target_lang` and `tone` into a natural‑language instruction.
  - Sends a single chat completion request.
  - Returns the translated text from the first choice.

### 4.3 `main() -> None`

- Implements a simple CLI loop for experimentation.

---

## 5. Configuration and Security

- `.env` must not be committed to version control.
- API key is never logged.
- HTTPS is used for all requests.

Example `.env`:

```text
OPENAI_API_KEY=sk-or-PASTE_YOUR_KEY_HERE
OPENAI_BASE_URL=https://openrouter.ai/api/v1
OPENAI_MODEL=meta-llama/llama-3.2-3b-instruct
```

---

## 6. Extension Ideas

- Add support for detecting the source language automatically.
- Add a simple glossary mechanism to preserve specific terms.
- Add evaluation prompts that ask the LLM to critique or back‑translate its own output.

