Build an AI Chatbot in 15 Minutes
=================================

This project is a **minimal LLM chatbot** designed as a 15‑minute, production‑minded exercise in **AI application development** and **LLM integration**.

It focuses on:

- one Python entrypoint: `app.py`
- one configuration file: `.env`
- one hosted LLM endpoint: **OpenAI‑compatible HTTP API (OpenRouter example)**

The pattern you implement here is the same core loop used in real‑world **AI copilots, internal chat tools, and support assistants**.

---

## 1. What You Will Build

You will build a **terminal‑based AI chatbot** that:

- reads a user question from standard input
- sends the question to a hosted LLM over HTTPS
- prints the model’s response back to the terminal

This repo is intentionally small so you can focus on the **LLM request/response flow**, not on UI or framework complexity.

---

## 2. Skills Demonstrated

- Python
- Machine Learning
- Large Language Models (LLMs)
- Prompt Engineering
- RESTful API Integration
- AI Application Development
- AI System Design

These keywords align with common **AI Engineer**, **ML Engineer**, and **LLM Engineer** job descriptions.

---

## 3. High‑Level Architecture

At a high level, the application:

- accepts user input from the terminal
- sends it as a JSON request to an OpenAI‑compatible `/v1/chat/completions` endpoint
- renders the first model reply back to the terminal

For a detailed sequence diagram and component responsibilities, see `LOW_LEVEL_DESIGN.md`.

---

## 4. Prerequisites

- Python 3.10+ installed
- `pip` available
- Git (optional, for cloning)
- An OpenRouter account and API key (`sk-or-...`)

---

## 5. Step‑by‑Step Setup

### 5.1 Clone and enter the project

```bash
git clone https://github.com/<your-org>/hello-llm.git
cd hello-llm
```

### 5.2 Install Python dependencies

```bash
python -m pip install -r requirements.txt
```

### 5.3 Generate an OpenRouter API key

1. Go to `https://openrouter.ai` and sign up.
2. After login, open **Dashboard → API Keys**.
3. Click **Create Key**, name it (e.g. `hello-llm`), and copy the key that starts with `sk-or-`.
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

## 6. Run the 15‑Minute Chatbot

From the project directory:

```bash
python app.py
```

You should see:

```text
Hello LLM - minimal chatbot
Type 'quit' to exit.

You:
```

Example interaction:

```text
You: What is machine learning?
Assistant: <model answer here>
```

Type `quit` or `exit` to stop the program.

---

## 7. Challenge Tasks (for 15‑minute extensions)

Use these as small, focused exercises to deepen your skills:

1. **Prompt Engineering Challenge**  
   - Add a system prompt that forces the model to answer in bullet points.  
   - Compare outputs with and without the system prompt.

2. **Error Handling Challenge**  
   - Detect and print a clear message when the API returns 401/429/500.  
   - Log raw error details to the console for debugging.

3. **Multi‑Turn Memory Challenge**  
   - Extend `app.py` to keep a short history of the last 3 messages.  
   - Send the full conversation to the model each time.

4. **Model Swap Challenge**  
   - Run `python compare_models.py "Your question here"` (or use `--models model-a,model-b`).  
   - Try at least two different models on OpenRouter.  
   - Record qualitative differences in latency and answer quality.

5. **Evaluation Challenge**  
   - Create a small list of test questions in `sample_data/example_prompts.txt`.  
   - Run them through the chatbot and manually score response quality.

Each challenge should still be completable in ~15 minutes and stays under ~100 lines of Python.

---

## 8. License

MIT License

