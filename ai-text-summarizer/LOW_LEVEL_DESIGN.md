Low-Level Design: AI Text Summarizer
====================================

This document describes the internals of the **ai-text-summarizer** 15‑minute lab.

---

## 1. Responsibilities

Primary responsibility:

> Convert arbitrary input text into a concise summary using a hosted LLM.

Out of scope:

- storage of documents or summaries
- web UI or authentication flows beyond API key usage

---

## 2. Components

### 2.1 User Interface Layer

- **Terminal (stdin/stdout)**
  - Prompts the user for a summary style and input text.
  - Displays the resulting summary.

### 2.2 Application Layer (`app.py`)

- `main()`:
  - Prints banner and available styles.
  - Reads style choice and text to summarize.
  - Calls `summarize(text, style)`.
  - Handles and reports errors without crashing.

- `summarize(text, style)`:
  - Constructs a style‑aware user prompt.
  - Delegates to integration layer for the LLM call.

### 2.3 Integration Layer

- **HTTP client (`requests`)**
  - Builds `messages` list for `/v1/chat/completions`:
    - system: instructions for high‑quality, faithful summaries.
    - user: includes desired style and the raw text.
  - Parses `choices[0].message.content` from the JSON response.

### 2.4 Configuration Layer

- **`.env`**
  - `OPENAI_API_KEY`
  - `OPENAI_BASE_URL`
  - `OPENAI_MODEL`
  - Loaded via `python-dotenv` in `get_api_key()`.

---

## 3. Data Flow

```text
User enters style + text
        │
        ▼
main()
  - resolve style string ("executive", "bullet-point", "short")
  - call summarize(text, style)
        │
        ▼
summarize()
  - load .env (OPENAI_*)
  - build system + user messages
  - POST to {OPENAI_BASE_URL}/chat/completions
        │
        ▼
Hosted LLM API
  - authenticate via API key
  - run model (OPENAI_MODEL)
  - return summary text in choices[0].message.content
        │
        ▼
summarize()
  - return summary string
        │
        ▼
main()
  - print summary
```

---

## 4. Key Functions

### 4.1 `get_api_key() -> str`

- Loads environment variables from `.env`.
- Retrieves `OPENAI_API_KEY`.
- Raises `RuntimeError` if the key is missing.

### 4.2 `summarize(text: str, style: str) -> str`

- Inputs:
  - `text`: raw text to summarize.
  - `style`: one of `executive`, `bullet-point`, `short`.
- Behavior:
  - Builds a prompt instructing the LLM to summarize in the given style.
  - Sends a chat completion request.
  - Returns the first choice’s message content.

### 4.3 `main() -> None`

- Implements an interactive CLI loop for quick experimentation.

---

## 5. Configuration and Security

- `.env` holds all secrets and must not be committed to version control.
- API key is never printed or logged.
- Only HTTPS base URLs are recommended.

Example `.env`:

```text
OPENAI_API_KEY=sk-or-PASTE_YOUR_KEY_HERE
OPENAI_BASE_URL=https://openrouter.ai/api/v1
OPENAI_MODEL=meta-llama/llama-3.2-3b-instruct
```

---

## 6. Extension Ideas

- Add support for multi‑paragraph input from files.
- Add summary quality controls (e.g. “very short”, “detailed”).
- Log summaries to a file for later analysis.
- Add basic evaluation prompts (e.g. ask the LLM to critique its own summary).

