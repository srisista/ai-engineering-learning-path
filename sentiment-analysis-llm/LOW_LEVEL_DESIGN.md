Low-Level Design: Sentiment Analysis LLM
=======================================

This document describes the internals of the **sentiment-analysis-llm** 15‑minute lab.

---

## 1. Responsibilities

Primary responsibility:

> Classify a single text input into one of three sentiment labels: `positive`, `negative`, or `neutral` using a hosted LLM.

Out of scope:

- dataset storage and labeling
- training or fine‑tuning models

---

## 2. Components

### 2.1 User Interface Layer

- **Terminal**
  - Prompts the user for text.
  - Displays the predicted sentiment label.

### 2.2 Application Layer (`app.py`)

- `main()`:
  - Prints banner and instructions.
  - Reads input text in a loop.
  - Calls `classify_sentiment(text)`.
  - Handles and prints errors without exiting the process.

- `classify_sentiment(text)`:
  - Builds a classification‑oriented system prompt.
  - Delegates to the integration layer for the HTTP call.

### 2.3 Integration Layer

- **HTTP client (`requests`)**
  - Reads configuration via environment variables.
  - Sends a chat completion request to `{OPENAI_BASE_URL}/chat/completions`.
  - Parses `choices[0].message.content` as the sentiment label.

### 2.4 Configuration Layer

- **`.env`**
  - `OPENAI_API_KEY`
  - `OPENAI_BASE_URL`
  - `OPENAI_MODEL`
  - Loaded via `python-dotenv` in `get_api_key()`.

---

## 3. Data Flow

```text
User enters text
        │
        ▼
main()
  - call classify_sentiment(text)
        │
        ▼
classify_sentiment()
  - load .env (OPENAI_*)
  - build system + user messages
  - POST to {OPENAI_BASE_URL}/chat/completions
        │
        ▼
Hosted LLM API
  - authenticate via API key
  - run model
  - return label in choices[0].message.content
        │
        ▼
classify_sentiment()
  - trim whitespace and return label
        │
        ▼
main()
  - print label
```

---

## 4. Key Functions

### 4.1 `get_api_key() -> str`

- Loads `.env`.
- Retrieves `OPENAI_API_KEY`.
- Raises `RuntimeError` if missing.

### 4.2 `classify_sentiment(text: str) -> str`

- Inputs:
  - `text`: arbitrary user text.
- Behavior:
  - Embeds guidelines in the system prompt to constrain outputs.
  - Sends a single chat completion request.
  - Returns the stripped message content as the label.

### 4.3 `main() -> None`

- Implements an interactive CLI for quick testing.

---

## 5. Configuration and Security

- `.env` must not be committed to version control.
- API key is not logged.
- HTTPS is used for all outbound requests.

Example `.env`:

```text
OPENAI_API_KEY=sk-or-PASTE_YOUR_KEY_HERE
OPENAI_BASE_URL=https://openrouter.ai/api/v1
OPENAI_MODEL=meta-llama/llama-3.2-3b-instruct
```

---

## 6. Extension Ideas

- Add confidence scores to the response via prompt engineering.
- Extend the label set (e.g. `very positive`, `very negative`) and adjust prompts.
- Log classified examples for manual review or future supervised training.

