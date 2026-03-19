AI Language Translator in 15 Minutes
====================================

This project is a **minimal LLM-based language translator** designed as a 15‑minute exercise in **machine translation**, **tone control**, and **LLM API integration**.

It focuses on:

- one Python entrypoint: `app.py`
- one configuration file: `.env`
- one hosted LLM endpoint: OpenAI‑compatible HTTP API (OpenRouter example)

---

## 1. What You Will Build

You will build a **terminal‑based translation tool** that:

- accepts a target language and tone (formal, casual, neutral)
- accepts English text as input
- uses an LLM to generate a translation in the requested style

This pattern is common in **localization pipelines**, **content workflows**, and **multilingual applications**.

---

## 2. Skills Demonstrated

- Python
- Machine Translation
- Large Language Models (LLMs)
- Prompt Engineering
- RESTful API Integration
- AI Application Development

---

## 3. High‑Level Architecture

At a high level, the application:

- reads configuration and API credentials from `.env`
- collects target language, tone, and source text from the terminal
- sends a translation request to `/v1/chat/completions`
- prints the translated text

For a detailed low‑level design, see `LOW_LEVEL_DESIGN.md`.

---

## 4. Prerequisites

- Python 3.10+ installed
- `pip` available
- Git (optional, for cloning)
- An OpenRouter account and API key (`sk-or-...`), or another OpenAI‑compatible provider

---

## 5. Step‑by‑Step Setup

### 5.1 Clone and enter the project

```bash
git clone https://github.com/<your-org>/ai-language-translator.git
cd ai-language-translator
```

### 5.2 Install Python dependencies

```bash
python -m pip install -r requirements.txt
```

### 5.3 Generate an OpenRouter API key

1. Go to `https://openrouter.ai` and sign up.
2. After login, open **Dashboard → API Keys**.
3. Click **Create Key**, name it (e.g. `ai-language-translator`), and copy the key that starts with `sk-or-`.
4. In the **Models** section, choose a model, e.g.:
   - `meta-llama/llama-3.2-3b-instruct`

### 5.4 Configure `.env`

In the project root, create a file named `.env`:

```text
OPENAI_API_KEY=sk-or-PASTE_YOUR_KEY_HERE
OPENAI_BASE_URL=https://openrouter.ai/api/v1
OPENAI_MODEL=meta-llama/llama-3.2-3b-instruct
```

**Important:**  

- No quotes, no extra spaces.
- The line must start exactly with `OPENAI_API_KEY=sk-or-...`.
- You can swap in another provider (e.g. OpenAI) by changing `OPENAI_BASE_URL` and `OPENAI_MODEL`.

---

## 6. Run the Translator

From the project directory:

```bash
python app.py
```

You should see:

```text
AI Language Translator - 15 Minute Lab
Examples: en→fr, en→de, en→es. Type 'quit' to exit.

Target language (e.g. French, German, Spanish):
```

Example interaction:

```text
Target language (e.g. French, German, Spanish): French
Tone (formal / casual / neutral): formal
Enter text to translate and press Enter:
> Thank you for your interest in our product. We will follow up shortly.

--- Translation ---
<translated French text in a formal tone>
```

Type `quit` or `exit` to stop the program.

---

## 7. Challenge Tasks

1. **Bidirectional translation**  
   - Detect the source language automatically and translate both ways.

2. **Glossary preservation**  
   - Add a simple glossary (e.g. product names) that must not be translated.

3. **Batch translation**  
   - Read multiple lines from a file and translate each line.

---

## 8. License

MIT License

