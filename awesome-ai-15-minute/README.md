awesome-ai-15-minute
=====================

**AI labs in 15 minutes** — a growing collection of small, production-minded Python labs you can build in under 15 minutes each.

Each project:
- focuses on **one real-world AI concept**
- uses **Python** and modern AI tooling
- keeps code under **100 lines**
- uses language and skills common in AI engineering job descriptions

This repository is the **main hub** that links to all individual 15-minute labs.

## Repository Categories

- **LLM Projects** (see [MODULE-CODE-COMPARISON.md](../docs/MODULE-CODE-COMPARISON.md) for what changes between labs)
  - `hello-llm` — first-token “hello world” for large language models
  - `prompt-engineering`
  - `ai-text-summarizer`
  - `ai-language-translator`
  - `sentiment-analysis-llm`
  - `ai-email-writer`
  - `ollama-docker` — local models with Ollama
  - `hello-llm/compare_models.py` — compare two models on one prompt

- **AI Agents**
  - `research-agent`
  - `web-browsing-agent`
  - `data-analysis-agent`
  - `workflow-automation`
  - `multi-agent-collaboration`
  - `autonomous-task-planner`

- **Machine Learning**
  - classic ML tasks like classification, regression, and clustering

- **Computer Vision**
  - image classification, object detection, and visual search

- **Speech AI**
  - speech-to-text, text-to-speech, and audio understanding

- **AI Infrastructure**
  - vector databases, monitoring, observability, and guardrails

- **AI Production Systems**
  - deployment, scaling, containerization, and APIs

For each project repository, see:

- `README.md` — step-by-step 15-minute guide
- `app.py` — main example (under 100 lines)
- `requirements.txt` — minimal dependencies
- `sample_data/` — small, open, or synthetic data
- `architecture.png` — simple diagram of the system

## How to Use This Hub

1. **Pick a 15-minute lab** from the categories above.
2. Open that repository and follow the `README`.
3. Use the **Experiment ideas** section in each lab to extend the project.

This structure is inspired by popular “Awesome” style repositories and is designed to be:

- beginner-friendly for self-learners
- useful for working engineers
- friendly to **recruiters** and **hiring managers** scanning GitHub portfolios

## Running Labs in PyCharm / IntelliJ

You can run any 15‑minute lab directly from an IDE:

1. **Open the workspace**
   - In PyCharm or IntelliJ (with the Python plugin), choose **Open** and select `ai-engineering-learning-path`.
2. **Configure the interpreter**
   - Set a Python 3.10+ interpreter for the project.
3. **Configure shared environment variables**
   - Create `.env` in the workspace root with:

     ```text
     OPENAI_API_KEY=sk-or-PASTE_YOUR_KEY_HERE
     OPENAI_BASE_URL=https://openrouter.ai/api/v1
     OPENAI_MODEL=meta-llama/llama-3.2-3b-instruct
     ```

4. **Install dependencies and run a lab**
   - Open the built‑in terminal and run:

     ```bash
     cd hello-llm
     python -m pip install -r requirements.txt
     python app.py
     ```

   - Or right‑click `app.py` in a lab folder (e.g. `hello-llm/app.py`) and choose **Run 'app'**.

You can repeat the same pattern for any other lab (`prompt-engineering`, `ai-text-summarizer`, etc.) by changing the folder name.

## Contributing 15-Minute Labs

You can contribute new labs that follow this format:

1. One concept per repo.
2. Under 100 lines of core code.
3. Uses only **open models** and **public/synthetic data**.
4. Includes:
   - what you will build
   - why this matters in industry
   - skills demonstrated
   - architecture overview
   - how to run in 5 minutes
   - experiment ideas

See existing labs (like `hello-llm`) for a template you can clone.

## License

All content in this hub is released under the **MIT License**. Individual project repositories may also include their own `LICENSE` file.

