# Build an AI Chatbot in 15 Minutes

⏱ Time required: 15 minutes  
💻 Lines of code: <100  
🎯 Concept: [INSERT CONCEPT — e.g., Retrieval Augmented Generation (RAG)]

One-sentence value prop (SEO-friendly): Build a **beginner-friendly, industry-relevant** AI project in Python that demonstrates **[CONCEPT]** using **open datasets** and **open / OpenAI-compatible models**.

## What You Will Build

In this 15-minute lab, you will build **[PROJECT NAME]**:

- [Bullet 1: what it does]
- [Bullet 2: what it does]
- [Bullet 3: what it does]

Deliverables:

- `app.py` — main runnable example (under 100 lines)
- `requirements.txt` — minimal dependencies
- `sample_data/` — small public or synthetic data
- `architecture.png` — a simple architecture diagram (optional but recommended)

## Why This Matters in Industry

**[CONCEPT]** is used in real products to improve:

- **Accuracy** and **relevance** (reducing hallucinations when applicable)
- **Developer velocity** (faster prototyping and iteration)
- **User experience** (natural language interfaces)

Common real-world use cases:

- [Use case 1: e.g., customer support automation]
- [Use case 2: e.g., knowledge base search / internal copilots]
- [Use case 3: e.g., analytics summarization / document understanding]

## Skills Demonstrated

- Python
- Machine Learning
- Large Language Models
- Prompt Engineering
- Vector Databases
- AI Application Development
- AI System Design

Optional (add if relevant):

- Retrieval Augmented Generation (RAG)
- Embeddings
- Semantic Search
- Evaluation (LLM evals)
- Observability and Monitoring
- Guardrails and Safety
- Deployment (Docker, APIs)

## Architecture Overview

High-level flow:

1. [Step 1]
2. [Step 2]
3. [Step 3]

Minimal architecture:

- **Input**: [CLI / Web / API]
- **Core**: [Prompt template / Retriever / Model call]
- **Data**: [sample_data / vector index / cache]
- **Output**: [terminal output / JSON response]

## How to Run in 5 Minutes

1. **Clone and enter the repo**

```bash
git clone https://github.com/<your-org>/<repo-name>.git
cd <repo-name>
```

2. **Create & activate a virtual environment (recommended)**

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Configure environment variables**

Create a `.env` file:

```text
# If you use an OpenAI-compatible provider for open models
OPENAI_API_KEY=your_key_here
OPENAI_BASE_URL=https://api.openai.com/v1
OPENAI_MODEL=<model-name>
```

Notes:

- Use **open datasets**, **public data**, or **synthetic data** only.
- Prefer **open models** (e.g., LLaMA, Mistral) served via an OpenAI-compatible API when possible.

5. **Run**

```bash
python app.py
```

## Experiment Ideas

- **Quality**: try alternative prompt templates and compare outputs.
- **Cost**: switch models and reduce token usage.
- **Reliability**: add retries + timeouts + basic error handling.
- **Evaluation**: add a tiny set of test prompts and check answer quality.
- **Productization**: wrap the script into a FastAPI endpoint.

## Repository Structure

```text
<repo-name>/
├── README.md
├── app.py
├── requirements.txt
├── sample_data/
└── architecture.png
```

## Suggested GitHub Topics

- artificial-intelligence
- machine-learning
- deep-learning
- generative-ai
- llm
- python
- prompt-engineering
- rag
- vector-search
- embeddings
- ai-agents

## Contribution Guide (15-Minute Projects)

PRs welcome — especially new 15-minute labs.

Guidelines:

1. One concept per repo.
2. Keep `app.py` **under 100 lines** (excluding blank lines).
3. Use only **open datasets** and **open / OpenAI-compatible models**.
4. Ensure the README includes:
   - What you will build
   - Why this matters in industry
   - Skills demonstrated
   - Architecture overview
   - How to run in 5 minutes
   - Experiment ideas

## License

MIT License

