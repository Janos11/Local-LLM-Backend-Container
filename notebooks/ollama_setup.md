# Ollama setup

<div align="center">
  <a href="https://ollama.com">
    <img alt="ollama" width="240" src="https://github.com/ollama/ollama/assets/3325447/0d0b44e2-8f4a-4e99-9b52-a5c1c741c8f7">
  </a>
</div>

[GitHub repo](https://github.com/ollama/ollama)

How to get started with locally run LLM, guide

## 1. Get the ollama docker container

start wit docker .yml file:
[docker-compose.yml](../docker-compose.yml)

`docker compose up -d`

2. Test if the container is running

- get port number `docker ps` 
- in browser `http://localhost:11434`
- command line: `curl http://localhost:11434/api/tags`

3. Get a model

`docker exec -it ollama ollama pull llama3`

`docker exec -it ollama ollama pull llama3:8b` - 4.7 GB

`docker exec -it ollama ollama pull llama3:70b`

🔄 Switching Models (in one container)

You don't need two containers. Instead, run commands like:

- `ollama run llama3`
- `ollama run llama3:8b`
- `ollama run mistral`
- 
Each model stays cached inside your container’s volume (/root/.ollama), and you can switch between them freely using CLI or API.

📦 Docker volume: Ollama will download, store, and reuse models.


