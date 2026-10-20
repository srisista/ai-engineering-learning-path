# AI Engineering Learning Path

Hands-on **15-minute Python labs** for students, early-career engineers, and curious professionals who want to understand what happens *behind* everyday AI tools — not just use them.

Each lab is a small, runnable program (under ~100 lines) focused on **one concept**: chat completions, prompts, sentiment, email drafting, translation, summarization, local models with Ollama, and comparing models.

## Quick start

1. Clone this repository and open it in your editor.
2. Copy `.env.example` to `.env` at the **repository root** and add your API key (OpenRouter-compatible keys work well):

   ```text
   OPENAI_API_KEY=sk-or-your-key
   OPENAI_BASE_URL=https://openrouter.ai/api/v1
   OPENAI_MODEL=meta-llama/llama-3.2-3b-instruct
   ```

3. Pick a lab folder, install dependencies, and run:

   ```bash
   cd hello-llm
   python -m pip install -r requirements.txt
   python app.py
   ```

4. Verify all labs compile and pass offline smoke tests (no API call):

   ```bash
   python scripts/verify_labs.py
   ```

## Starter labs (recommended order)

| # | Folder | What you learn |
|---|--------|----------------|
| 1 | [`hello-llm`](hello-llm/) | Your first LLM chat call |
| 2 | [`prompt-engineering`](prompt-engineering/) | System prompts and patterns |
| 3 | [`sentiment-analysis-llm`](sentiment-analysis-llm/) | Classification via prompts |
| 4 | [`ollama-docker`](ollama-docker/) | Run open models locally |
| 5 | [`hello-llm/compare_models.py`](hello-llm/compare_models.py) | Compare two models on the same question |

**Bonus labs:** [`ai-text-summarizer`](ai-text-summarizer/), [`ai-language-translator`](ai-language-translator/), [`ai-email-writer`](ai-email-writer/)

## What actually changes between modules?

Every lab shares the same **plumbing** (load `.env`, call `/chat/completions`). The **product behavior** is defined by a few lines: the system prompt, how the user message is built, and the CLI loop.

See **[docs/MODULE-CODE-COMPARISON.md](docs/MODULE-CODE-COMPARISON.md)** for a line-by-line comparison (e.g. email writer vs translator vs summarizer).

## Hub and contributing

The curated index and lab format live in [`awesome-ai-15-minute/README.md`](awesome-ai-15-minute/README.md).

## License

MIT — see [LICENSE](LICENSE).
