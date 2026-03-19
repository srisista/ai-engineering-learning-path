Low-Level Design: hello-llm Chatbot
===================================

This document describes the internal design and data flow of the `hello-llm` 15‑minute chatbot project.

It is intended for:

- AI engineers
- backend/ML engineers
- reviewers evaluating **LLM integration skills** and **system design thinking**

---

## 1. Responsibilities and Scope

The system is intentionally small and focuses on a single responsibility:

> Accept a user question in the terminal, send it to a hosted LLM over HTTP, and display the response.

Out of scope:

- authentication flows beyond API key usage
- long‑term conversation storage
- UI frameworks or frontend code

---

## 2. Components Overview

### 2.1 User Interface Layer

- **Terminal (stdin/stdout)**
  - Collects user input (`You:` prompt)
  - Displays model responses

### 2.2 Application Layer

- **`app.py`**
  - Reads configuration from `.env`
  - Manages the REPL loop (`while True`)
  - Delegates a single question to `chat_once(question)`
  - Handles basic error reporting

### 2.3 Integration Layer

- **HTTP client**
  - Uses `requests` to call an OpenAI‑compatible `/v1/chat/completions` endpoint.
  - Converts Python dicts to JSON payloads.
  - Parses JSON responses and extracts `choices[0].message.content`.

### 2.4 Configuration Layer

- **`.env`**
  - `OPENAI_API_KEY`
  - `OPENAI_BASE_URL`
  - `OPENAI_MODEL`
  - Loaded via `python-dotenv` inside `get_api_key()`.

---

## 3. Data Flow (Single Turn)

```text
┌───────────────────────────────────────────────┐
│  1. User types question in terminal          │
└─────────────────────┬─────────────────────────┘
                      │ stdin (text)
┌─────────────────────▼─────────────────────────┐
│ 2. main() in app.py                          │
│    - reads question                          │
│    - calls chat_once(question)               │
└─────────────────────┬─────────────────────────┘
                      │ function call
┌─────────────────────▼─────────────────────────┐
│ 3. chat_once(question)                        │
│    - loads .env via load_dotenv()            │
│    - reads OPENAI_API_KEY, BASE_URL, MODEL   │
│    - builds JSON payload (messages[ ])       │
│    - POST {base_url}/chat/completions        │
└─────────────────────┬─────────────────────────┘
                      │ HTTPS (JSON)
┌─────────────────────▼─────────────────────────┐
│ 4. Hosted LLM API (OpenRouter example)       │
│    - authenticates via Authorization header  │
│    - runs model: OPENAI_MODEL                │
│    - returns choices[0].message.content      │
└─────────────────────┬─────────────────────────┘
                      │ HTTPS (JSON)
┌─────────────────────▼─────────────────────────┐
│ 5. chat_once()                                │
│    - parses JSON                              │
│    - returns response text                    │
└─────────────────────┬─────────────────────────┘
                      │ return value (string)
┌─────────────────────▼─────────────────────────┐
│ 6. main() prints response to terminal         │
└───────────────────────────────────────────────┘
```

---

## 4. Key Functions and Contracts

### 4.1 `get_api_key() -> str`

- Loads environment variables from `.env`.
- Retrieves `OPENAI_API_KEY`.
- Fails fast with a clear error if the key is missing.

**Contract:**

- Returns a non‑empty API key string, or raises `RuntimeError`.

### 4.2 `chat_once(question: str) -> str`

- Inputs:
  - `question`: non‑empty user question.
- Behavior:
  - Reads `OPENAI_API_KEY`, `OPENAI_BASE_URL`, `OPENAI_MODEL`.
  - Constructs payload for `/v1/chat/completions`.
  - Handles HTTP errors via `raise_for_status()`.
  - Extracts and returns the first choice’s message content.

**Contract:**

- Returns a model response string on success.
- May raise `requests.HTTPError` (wrapped and surfaced in `main()`).

### 4.3 `main() -> None`

- Implements the interactive loop:
  - Prints banner.
  - Reads user input.
  - Handles exit commands (`quit`, `exit`).
  - Logs any errors from `chat_once` without crashing the loop.

---

## 5. Configuration and Environment

### 5.1 Required variables

- `OPENAI_API_KEY` — secret API key (not committed to Git).
- `OPENAI_BASE_URL` — usually `https://openrouter.ai/api/v1` or `https://api.openai.com/v1`.
- `OPENAI_MODEL` — model identifier, e.g. `meta-llama/llama-3.2-3b-instruct`.

### 5.2 Security Considerations

- `.env` must be excluded from version control.
- API key is only loaded at runtime and never logged.
- HTTPS is assumed for all requests (no plain HTTP).

---

## 6. Extension Points

Engineers can extend this design in several directions:

- **Conversation memory**: maintain a list of previous messages and send full history in each request.
- **Metrics and logging**: log latency, token usage (if provided), and error rates.
- **Abstraction layer**: wrap the HTTP integration in a separate module to support multiple providers.
- **Deployment**: wrap `chat_once` behind a FastAPI/Flask endpoint for web or product integration.

These extensions can be implemented without changing the fundamental data flow or external contracts described above.

