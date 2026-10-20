# ollama-docker — local open models

Run [Ollama](https://ollama.com/) in Docker so you can pull and chat with open-weight models on your own machine (no cloud API key required for inference).

## Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (or Docker Engine + Compose)

## Start Ollama

From this folder:

```bash
docker compose up -d
```

The API listens on **http://localhost:11434**.

## Pull and run a model

```bash
docker exec -it ollama ollama pull llama3.2
docker exec -it ollama ollama run llama3.2 "Explain what an LLM is in two sentences."
```

## Point Python labs at Ollama (optional)

Ollama exposes an OpenAI-compatible endpoint. In your root `.env` you can use:

```text
OPENAI_BASE_URL=http://localhost:11434/v1
OPENAI_MODEL=llama3.2
OPENAI_API_KEY=ollama
```

(`OPENAI_API_KEY` can be any non-empty string for local Ollama.)

Then run any lab, for example:

```bash
cd ../hello-llm
python app.py
```

## Stop

```bash
docker compose down
```

Data is kept in the `ollama-data` Docker volume.
