AI Email Writer in 15 Minutes
=============================

This project is a **minimal AI email drafting assistant** designed as a 15‑minute exercise in **prompt-to-email generation** and **LLM integration**.

It focuses on:

- one Python entrypoint: `app.py`
- one configuration file: `.env`
- one hosted LLM endpoint: OpenAI‑compatible HTTP API (OpenRouter example)

---

## 1. What You Will Build

You will build a **terminal‑based email writer** that:

- accepts a short description or bullet points about an email you need
- lets you choose a tone (professional, friendly, concise)
- generates a full email draft (greeting, body, sign‑off)

This pattern is common in **productivity tools**, **sales outreach**, and **support workflows**.

---

## 2. Skills Demonstrated

- Python
- Large Language Models (LLMs)
- Prompt Engineering
- Business Email Generation
- RESTful API Integration
- AI Application Development

---

## 3. High‑Level Architecture

At a high level, the application:

- reads configuration and credentials from `.env`
- accepts tone + email description from the terminal
- sends a formatted prompt to `/v1/chat/completions`
- prints the generated email draft

For low‑level design details, see `LOW_LEVEL_DESIGN.md`.

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
git clone https://github.com/<your-org>/ai-email-writer.git
cd ai-email-writer
```

### 5.2 Install Python dependencies

```bash
python -m pip install -r requirements.txt
```

### 5.3 Generate an OpenRouter API key

1. Go to `https://openrouter.ai` and sign up.
2. After login, open **Dashboard → API Keys**.
3. Click **Create Key**, name it (e.g. `ai-email-writer`), and copy the key that starts with `sk-or-`.
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

## 6. Run the Email Writer

From the project directory:

```bash
python app.py
```

You should see:

```text
AI Email Writer - 15 Minute Lab
Turn bullet points into a polished email. Type 'quit' to exit.

Tone (professional / friendly / concise):
```

Example interaction:

```text
Tone (professional / friendly / concise): professional
Describe the email you want (bullet points or short description):
> Follow up with a recruiter after an interview and thank them.

--- Draft Email ---
<generated email draft>
```

Type `quit` or `exit` to stop the program.

### 6.1 Tone Options (professional / friendly / concise)

- **professional**  
  - Clear, polite, and business‑oriented.  
  - Example use: follow‑up with a recruiter, communication with clients or managers.

- **friendly**  
  - Warm, approachable, and slightly informal.  
  - Example use: internal team updates, notes to colleagues, community messages.

- **concise**  
  - Short and to the point, minimal small talk.  
  - Example use: quick status updates, direct requests, or reminders.

For the same instruction (“Follow up with a recruiter after an interview and thank them”):

- **professional** → longer, well‑structured email with formal greeting and sign‑off.  
- **friendly** → slightly more relaxed tone, still polite, more conversational language.  
- **concise** → very brief email focusing only on the key message and thanks.

---

## 7. Challenge Tasks

1. **Signature management**  
   - Add a configurable name/title/signature block from `.env`.

2. **Reply / forward modes**  
   - Extend prompts to generate replies to existing emails.

3. **Content review mode**  
   - Allow pasting a full email and ask the model to rewrite for clarity or tone.

---

## 8. License

MIT License

