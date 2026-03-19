AI Text Summarizer in 15 Minutes
================================

This project is a **minimal LLM-based text summarizer** designed as a 15‑minute exercise in **summarization**, **prompt design**, and **LLM API integration**.

It focuses on:

- one Python entrypoint: `app.py`
- one configuration file: `.env`
- one hosted LLM endpoint: OpenAI‑compatible HTTP API (OpenRouter example)

---

## 1. What You Will Build

You will build a **terminal‑based summarization tool** that:

- reads input text from the terminal
- lets you choose a summary style (executive, bullet, short)
- sends the request to an LLM
- prints the summary

This pattern mirrors how real systems turn long documents into **concise executive summaries**.

---

## 2. Skills Demonstrated

- Python
- Machine Learning
- Large Language Models (LLMs)
- Prompt Engineering
- Text Summarization
- RESTful API Integration
- AI Application Development

---

## 3. High‑Level Architecture

At a high level, the application:

- accepts raw text from the terminal
- wraps it in a style‑aware summarization prompt
- sends it as a JSON request to `/v1/chat/completions`
- prints the first model reply as the summary

For a detailed sequence diagram and data flow, see `LOW_LEVEL_DESIGN.md`.

---

## 4. Prerequisites

- Python 3.10+ installed
- `pip` available
- Git (optional, for cloning)
- An OpenRouter account and API key (`sk-or-...`), or another OpenAI‑compatible provider

---

## 5. Step‑by‑Step Setup (Local Config + Commands)

### 5.1 Configure shared `.env` (workspace root)

In the workspace root (`ai-engineering-learning-path/.env`):

```text
OPENAI_API_KEY=sk-or-PASTE_YOUR_KEY_HERE
OPENAI_BASE_URL=https://openrouter.ai/api/v1
OPENAI_MODEL=meta-llama/llama-3.2-3b-instruct
```

This single `.env` file is used by all Phase 1 projects (including `ai-text-summarizer`).

### 5.2 Clone and enter the project

```bash
git clone https://github.com/<your-org>/ai-text-summarizer.git
cd ai-text-summarizer
```

### 5.3 Install Python dependencies

```bash
python -m pip install -r requirements.txt
```

### 5.4 Generate an OpenRouter API key

1. Go to `https://openrouter.ai` and sign up.
2. After login, open **Dashboard → API Keys**.
3. Click **Create Key**, name it (e.g. `ai-text-summarizer`), and copy the key that starts with `sk-or-`.
4. In the **Models** section, choose a model, e.g.:
   - `meta-llama/llama-3.2-3b-instruct`

### 5.4 Configure `.env`

In the project root, create a file named `.env`:

```text
OPENAI_API_KEY=sk-or-PASTE_YOUR_KEY_HERE
OPENAI_BASE_URL=https://openrouter.ai/api/v1
OPENAI_MODEL=meta-llama/llama-3.2-3b-instruct
```

**Important:** If both the root `.env` and a local `.env` exist, local values override root values.

- No quotes, no extra spaces.
- The line must start exactly with `OPENAI_API_KEY=sk-or-...`.
- You can swap in another provider (e.g. OpenAI) by changing `OPENAI_BASE_URL` and `OPENAI_MODEL`.

---

## 6. Run the Summarizer

From the project directory:

```bash
python app.py
```

You should see:

```text
AI Text Summarizer - 15 Minute Lab
Styles: [1] executive  [2] bullet  [3] short
Type 'quit' to exit.

Select style (1/2/3):
```

Example interaction:

```text
Select style (1/2/3): 1
Paste text to summarize (single line) and press Enter:
> Our product increased user engagement by 45% over the last quarter...

--- Summary ---
<executive-style summary>
```

Type `quit` or `exit` to stop the program.

### 6.1 Summary Styles (1 / 2 / 3)

The three style options map to:

- **1 – Executive**: multi‑paragraph summary suitable for managers and stakeholders.
- **2 – Bullet**: key points as a bullet list for fast scanning.
- **3 – Short**: very brief TL;DR (usually 1–2 sentences).

Example outputs for the same input text:

- **Executive (1)**:  
  “The AI‑Text‑Summarizer condenses complex text into concise, high‑quality summaries using advanced NLP and machine learning. It increases productivity by reducing reading time while preserving key information, and is useful across business, education, and research workflows.”

- **Bullet (2)**:  
  - Condenses complex text into concise summaries  
  - Uses NLP and machine learning  
  - Increases productivity and understanding  
  - Applicable to business, education, and research  

- **Short (3)**:  
  “AI‑Text‑Summarizer quickly turns long text into concise summaries that preserve the main ideas.”

---

## 7. Challenge Tasks

Use these quick tasks to practice:

1. **Multi‑paragraph support**  
   - Read text from a `.txt` file instead of a single line.

2. **Section‑aware summaries**  
   - Add a mode that summarizes text into “Overview / Risks / Next Steps” sections.

3. **Length control**  
   - Add an option for approximate summary length (short/medium/long).

---

## 8. License

MIT License

