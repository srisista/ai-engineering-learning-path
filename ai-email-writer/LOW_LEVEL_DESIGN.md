Low-Level Design: AI Email Writer
=================================

This document describes the internals of the **ai-email-writer** 15‑minute lab.

---

## 1. Responsibilities

Primary responsibility:

> Turn a short natural-language instruction or bullet points into a complete email draft using a hosted LLM.

Out of scope:

- sending emails
- contact management or scheduling

---

## 2. Components

### 2.1 User Interface Layer

- **Terminal**
  - Prompts for desired tone.
  - Collects email description or bullet points.
  - Displays the generated email draft.

### 2.2 Application Layer (`app.py`)

- `main()`:
  - Prints banner and instructions.
  - Reads `tone` and `instruction` from the user.
  - Calls `draft_email(instruction, tone)`.
  - Handles and reports errors from the integration layer.

- `draft_email(instruction, tone)`:
  - Builds a system prompt that enforces email structure (greeting, body, sign‑off).
  - Includes the requested tone in the user prompt.

### 2.3 Integration Layer

- **HTTP client (`requests`)**
  - Reads configuration from environment variables.
  - Sends a chat completion request to `{OPENAI_BASE_URL}/chat/completions`.
  - Parses `choices[0].message.content` as the email draft.

### 2.4 Configuration Layer

- **`.env`**
  - `OPENAI_API_KEY`
  - `OPENAI_BASE_URL`
  - `OPENAI_MODEL`
  - Loaded via `python-dotenv` in `get_api_key()`.

---

## 3. Data Flow

```text
User enters tone + instruction
        │
        ▼
main()
  - call draft_email(instruction, tone)
        │
        ▼
draft_email()
  - load .env (OPENAI_*)
  - build system + user messages
  - POST to {OPENAI_BASE_URL}/chat/completions
        │
        ▼
Hosted LLM API
  - authenticate via API key
  - run model
  - return email text in choices[0].message.content
        │
        ▼
draft_email()
  - return draft email
        │
        ▼
main()
  - print draft email
```

---

## 4. Key Functions

### 4.1 `get_api_key() -> str`

- Loads `.env`.
- Retrieves `OPENAI_API_KEY`.
- Raises `RuntimeError` if missing.

### 4.2 `draft_email(instruction: str, tone: str) -> str`

- Inputs:
  - `instruction`: high-level description or bullet points.
  - `tone`: text such as `professional`, `friendly`, or `concise`.
- Behavior:
  - Embeds `tone` and `instruction` into the user prompt.
  - Sends chat completion request.
  - Returns the first choice’s message content.

### 4.3 `main() -> None`

- Implements the CLI loop.

---

## 5. Configuration and Security

- `.env` must not be committed to version control.
- API key is never logged.
- HTTPS is recommended for all requests.

Example `.env`:

```text
OPENAI_API_KEY=sk-or-PASTE_YOUR_KEY_HERE
OPENAI_BASE_URL=https://openrouter.ai/api/v1
OPENAI_MODEL=meta-llama/llama-3.2-3b-instruct
```

---

## 6. Extension Ideas

- Add a configurable signature from `.env` (name, role, company).
+- Add input to specify subject line separately.
+- Add a “rewrite” mode to improve existing emails instead of drafting from scratch.

