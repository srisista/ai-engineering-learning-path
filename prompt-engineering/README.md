Build Better Prompts in 15 Minutes
==================================

This project is a **prompt engineering lab** designed as a 15‑minute exercise in **LLM behavior control**, **system prompts**, and **few‑shot patterns**.

It focuses on:

- one Python entrypoint: `app.py`
- one configuration file: `.env`
- one hosted LLM endpoint: OpenAI‑compatible HTTP API (OpenRouter example)

The same integration pattern works with providers like OpenAI, OpenRouter, or any service exposing `/v1/chat/completions`.

---

## 1. What You Will Build

You will build a **terminal‑based prompt engineering playground** that lets you:

- choose a prompt pattern (bullet explainer, step‑by‑step reasoning, few‑shot classifier)
- send your own text through that pattern
- observe how the LLM’s behavior changes with each pattern

This is a practical way to demonstrate **prompt engineering skills** on your portfolio.

---

## 2. Skills Demonstrated

- Python
- Large Language Models (LLMs)
- Prompt Engineering
- Few‑Shot Learning
- RESTful API Integration
- AI Application Development
- AI System Design

---

## 3. High‑Level Architecture

At a high level, the application:

- accepts a pattern choice and user input from the terminal
- constructs a different **system prompt** and message set per pattern
- sends the resulting messages to `/v1/chat/completions`
- prints the model reply, labeled by the selected pattern

For a detailed sequence diagram and data flow, see `LOW_LEVEL_DESIGN.md`.

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
git clone https://github.com/<your-org>/prompt-engineering.git
cd prompt-engineering
```

### 5.2 Install Python dependencies

```bash
python -m pip install -r requirements.txt
```

### 5.3 Generate an OpenRouter API key

1. Go to `https://openrouter.ai` and sign up.
2. After login, open **Dashboard → API Keys**.
3. Click **Create Key**, name it (e.g. `prompt-engineering`), and copy the key that starts with `sk-or-`.
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

## 6. Run the Prompt Engineering Lab

From the project directory:

```bash
python app.py
```

You should see:

```text
Prompt Engineering Lab - 15 Minute LLM Patterns
Patterns: [1] bullet_explainer  [2] step_by_step  [3] few_shot_classifier
Type 'quit' to exit.

Select pattern (1/2/3):
```

Example interaction:

```text
Select pattern (1/2/3): 1
Enter your prompt: Explain retrieval augmented generation.

--- Model Response (bullet_explainer) ---
<model answer in bullet points>
```

Type `quit` or `exit` to stop the program.

### 6.1 Pattern Options (1 / 2 / 3)

The menu shorthand maps to:

- **1 – `bullet_explainer`**  
  - System prompt: senior AI engineer, respond in concise bullet points.  
  - Example input:  
    `Explain retrieval augmented generation.`  
  - Example behavior:  
    - what RAG is  
    - why it reduces hallucinations  
    - when to use it in production

- **2 – `step_by_step`**  
  - System prompt: careful tutor, always reason step‑by‑step first.  
  - Example input:  
    `How does vector search work?`  
  - Example behavior:  
    1. defines embeddings  
    2. explains vector space and distance  
    3. walks through retrieval and ranking

- **3 – `few_shot_classifier`**  
  - System prompt: includes labeled examples for sentiment before your text.  
  - Example input:  
    `I’m not sure this product is worth the price.`  
  - Example behavior:  
    - returns a single label such as `negative` or `neutral`, following the few‑shot pattern.

---

## 7. Prompt Patterns Implemented

The following patterns are intentionally simple but useful in real systems:

1. **Bullet Explainer (`bullet_explainer`)**
   - System prompt: act as a senior AI engineer; respond in concise bullet points.
   - Use when you want **structured, scannable summaries**.

2. **Step‑by‑Step Tutor (`step_by_step`)**
   - System prompt: act as a careful tutor; reason step by step first.
   - Use when you want **transparent reasoning** or explanations.

3. **Few‑Shot Classifier (`few_shot_classifier`)**
   - System prompt: includes labeled examples (positive/negative) before your text.
   - Use when you want **simple sentiment or label classification** without fine‑tuning.

Each pattern is implemented as a different system message in `app.py`, so the only change between runs is the **prompt**, not the code.

---

## 8. Challenge Tasks (for 15‑minute extensions)

Use these small tasks to turn this lab into a strong portfolio artifact:

1. **Add a JSON‑only output pattern**  
   - Create a pattern that forces the model to respond with strict JSON (e.g. `{"summary": "...", "risk_level": "high"}`).

2. **Add a role‑playing pattern**  
   - Create a pattern where the model acts as a hiring manager reviewing a resume snippet.

3. **Add temperature and max_tokens controls**  
   - Expose `temperature` and `max_tokens` as simple numeric inputs before each call.

4. **Add evaluation prompts**  
   - Store prompts in `sample_data/example_prompts.txt` and run them through each pattern to compare outputs.

Each of these can be implemented in ~15 minutes and keeps the codebase under ~100 lines.

---

## 9. License

MIT License

