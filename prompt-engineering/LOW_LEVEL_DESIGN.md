Low-Level Design: prompt-engineering Lab
========================================

This document describes the internal design and data flow of the **prompt engineering** 15‑minute lab.

---

## 1. Responsibilities and Scope

Primary responsibility:

> Provide a simple CLI that lets a user select a prompt pattern and send text to an LLM using that pattern.

Out of scope:

- training or fine‑tuning models
- persistence of conversation history
- web UI or authentication flows beyond API key usage

---

## 2. Components

### 2.1 User Interface Layer

- **Terminal (stdin/stdout)**
  - Presents available patterns to the user.
  - Collects pattern choice and prompt text.
  - Displays the LLM response with a pattern label.

### 2.2 Application Layer

- **`app.py`**
  - `main()`:
    - prints banner and pattern menu
    - reads user input in a loop
    - maps numeric choices (1/2/3) to pattern IDs
    - calls `chat_with_pattern(user_input, pattern)`
    - prints success or error messages
  - `chat_with_pattern(question, pattern)`:
    - selects an appropriate **system prompt** based on the pattern
    - delegates to the integration layer (HTTP call)

### 2.3 Integration Layer

- **HTTP client (`requests`)**
  - Builds `messages` list with:
    - system message (pattern‑specific)
    - user message (raw input)
  - Sends `POST` to `{OPENAI_BASE_URL}/chat/completions`.
  - Parses `choices[0].message.content`.

### 2.4 Configuration Layer

- **`.env`**
  - `OPENAI_API_KEY`
  - `OPENAI_BASE_URL`
  - `OPENAI_MODEL`
  - Loaded via `python-dotenv` (`load_dotenv()` in `get_api_key()`).

---

## 3. Data Flow

### 3.1 Sequence (per interaction)

```text
User selects pattern and enters text
        │
        ▼
main() in app.py
  - resolve pattern ID ("1" → "bullet_explainer", etc.)
  - call chat_with_pattern(user_input, pattern)
        │
        ▼
chat_with_pattern()
  - load .env (OPENAI_* variables)
  - build system prompt from pattern map
  - construct messages[ ] list
  - POST to /v1/chat/completions
        │
        ▼
Hosted LLM API (OpenRouter)
  - authenticate via Authorization header
  - run chosen model (OPENAI_MODEL)
  - return JSON with choices[0].message.content
        │
        ▼
chat_with_pattern()
  - extract content and return string
        │
        ▼
main()
  - print pattern label and response
```

---

## 4. Pattern Definitions

Pattern selection is implemented as a simple mapping inside `chat_with_pattern`:

- `bullet_explainer`
  - System prompt instructs the model to explain concepts in **concise bullet points**.
  - Intended for **structured summaries**.

- `step_by_step`
  - System prompt instructs the model to act as a careful tutor and **reason step by step**.
  - Intended for **transparent reasoning** and explanations.

- `few_shot_classifier`
  - System prompt includes a couple of labeled sentiment examples before the user text.
  - Intended as a **few‑shot classification** pattern without model fine‑tuning.

These are implemented as static strings, keeping the code simple and deterministic.

---

## 5. Key Functions and Contracts

### 5.1 `get_api_key() -> str`

- Loads environment via `load_dotenv()`.
- Reads `OPENAI_API_KEY` from the environment.
- Raises `RuntimeError` with a clear message if the key is missing.

### 5.2 `chat_with_pattern(user_input: str, pattern: str) -> str`

- Inputs:
  - `user_input`: arbitrary user text.
  - `pattern`: one of `bullet_explainer`, `step_by_step`, `few_shot_classifier`.
- Behavior:
  - Resolves the system prompt based on `pattern`.
  - Constructs a `messages` list with system + user messages.
  - Sends an HTTP `POST` to `{OPENAI_BASE_URL}/chat/completions`.
  - Raises for HTTP errors; returns the first message content on success.

### 5.3 `main() -> None`

- Implements a simple REPL:
  - Loops until user types `quit`/`exit`.
  - Handles invalid pattern selections gracefully.
  - Catches and prints errors from `chat_with_pattern` without terminating the program.

---

## 6. Configuration and Security

- `.env` holds all secrets and must not be committed to version control.
- `OPENAI_API_KEY` is only read at runtime and never logged.
- All calls use HTTPS endpoints (e.g. `https://openrouter.ai/api/v1`).

Example `.env`:

```text
OPENAI_API_KEY=sk-or-PASTE_YOUR_KEY_HERE
OPENAI_BASE_URL=https://openrouter.ai/api/v1
OPENAI_MODEL=meta-llama/llama-3.2-3b-instruct
```

---

## 7. Extension Ideas

Possible low‑effort extensions that preserve the current design:

- Add more patterns (e.g. JSON‑only responses, role‑play interviewer, code reviewer).
- Add temperature and max tokens as additional config values.
- Log requests and responses to a file for offline comparison of patterns.
- Abstract the HTTP client into a separate module for multi‑provider support.

These extensions can be implemented without changing the fundamental data flow or public behavior of `app.py`.

