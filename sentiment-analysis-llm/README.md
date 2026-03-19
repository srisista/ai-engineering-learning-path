Sentiment Analysis with LLM in 15 Minutes
=========================================

This project is a **minimal LLM-based sentiment classifier** designed as a 15‑minute exercise in **classification**, **prompt engineering**, and **LLM API integration**.

It focuses on:

- one Python entrypoint: `app.py`
- one configuration file: `.env`
- one hosted LLM endpoint: OpenAI‑compatible HTTP API (OpenRouter example)

---

## 1. What You Will Build

You will build a **terminal‑based sentiment analysis tool** that:

- accepts free‑form text from the terminal
- sends it to an LLM with a sentiment‑classification prompt
- prints a single label: `positive`, `negative`, or `neutral`

This is a classic pattern for **customer feedback analysis** and **review mining**.

---

## 2. Skills Demonstrated

- Python
- Machine Learning
- Large Language Models (LLMs)
- Text Classification
- Prompt Engineering
- RESTful API Integration
- AI Application Development

---

## 3. High‑Level Architecture

At a high level, the application:

- reads configuration and API credentials from `.env`
- accepts a text input from the user
- sends the text to `/v1/chat/completions` with a classification-oriented prompt
- prints the returned label

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
git clone https://github.com/<your-org>/sentiment-analysis-llm.git
cd sentiment-analysis-llm
```

### 5.2 Install Python dependencies

```bash
python -m pip install -r requirements.txt
```

### 5.3 Generate an OpenRouter API key

1. Go to `https://openrouter.ai` and sign up.
2. After login, open **Dashboard → API Keys**.
3. Click **Create Key**, name it (e.g. `sentiment-analysis-llm`), and copy the key that starts with `sk-or-`.
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

## 6. Run the Sentiment Classifier

From the project directory:

```bash
python app.py
```

You should see:

```text
Sentiment Analysis with LLM - 15 Minute Lab
Classify text as positive / negative / neutral. Type 'quit' to exit.

Enter text to classify:
```

Example interaction:

```text
Enter text to classify: I love this product, it saved me so much time!
Predicted sentiment: positive
```

Type `quit` or `exit` to stop the program.

---

## 7. Challenge Tasks

1. **Confidence prompts**  
   - Ask the model to also provide a confidence score (e.g. `0–1`) in its response.

2. **Aspect-based sentiment**  
   - Extend the prompt to classify sentiment separately for price, quality, and usability.

3. **Batch classification**  
   - Read multiple lines from a file and output labels for each line.

---

## 8. License

MIT License

