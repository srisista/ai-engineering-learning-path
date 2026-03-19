Contributing
============

Thanks for helping build **AI projects in 15 minutes**.

This ecosystem is designed to be:

- beginner-friendly
- useful in industry
- legally safe (open data + open models)
- small enough to finish quickly (under 100 lines of core code)

## What to Contribute

You can contribute:

- a new 15-minute lab repository (recommended)
- improvements to existing labs (README clarity, bug fixes, better prompts)
- new experiment ideas or evaluation tips

## 15-Minute Lab Requirements

Your contribution should follow these rules:

1. **One concept per lab** (e.g. embeddings, RAG, prompt engineering, guardrails).
2. **Under 100 lines** of core Python in `app.py` (excluding blank lines).
3. Uses only:
   - **public datasets**
   - **synthetic data**
   - **open models** (or OpenAI-compatible APIs that can serve open models like LLaMA/Mistral)
4. README must include:
   - What you will build
   - Why this matters in industry
   - Skills demonstrated (ATS-friendly)
   - Architecture overview
   - How to run in 5 minutes
   - Experiment ideas
5. Prefer minimal dependencies and fast setup.

## Standard Repository Structure

```text
project-name/
├── README.md
├── app.py
├── requirements.txt
├── sample_data/
└── architecture.png
```

## Legal Safety Checklist

Before you submit:

- confirm your `sample_data/` is public or synthetic
- avoid proprietary datasets or copied docs
- do not commit secrets (`.env`, API keys)

## Submitting a Contribution

1. Fork the repository (or create your lab repo in your own namespace).
2. Use the `README_TEMPLATE.md` as a starting point.
3. Open a pull request with:
   - a short summary of the concept
   - how to run
   - what you tested

## Code of Conduct

Be kind, constructive, and helpful. We’re building a learning ecosystem.

