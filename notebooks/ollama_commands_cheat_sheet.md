# 🐳🦙 Ollama in Docker – Cheat Sheet

A quick reference for working with LLaMA models using [Ollama](https://ollama.com/).

<div align="center">
  <a href="https://ollama.com">
    <img alt="ollama" width="240" src="https://github.com/ollama/ollama/assets/3325447/0d0b44e2-8f4a-4e99-9b52-a5c1c741c8f7">
  </a>
</div>

[🦙 Ollama GitHub Repo](https://github.com/ollama/ollama)

## 🐳 Docker Commands for Ollama

| Command                                     | Description |
|---------------------------------------------|-------------|
| Command	Description                         
| `docker exec -it ollama bash`                 |	Access terminal inside the running container
| `docker exec -it ollama ollama run llama3:8b` |	Run the llama3:8b model directly from host via Docker 
| `docker start ollama`                         |	Start the Ollama container                            
| `docker stop ollama`                          |	Stop the Ollama container                              
| `docker logs -f ollama`                       |	View real-time logs of the Ollama container         
| `docker ps`                                   |	Show running containers                                         
| `docker ps -a`                                |	Show all containers (including stopped ones)                 
| `docker rm ollama`                            |	Remove the Ollama container (must be stopped)            
| `docker volume ls`                           |	List Docker volumes (to see if model data is persistent) 


---

## 🚀 Running Models in Docker

| Command | Description |
|--------|-------------|
| `ollama run llama3` | Start chat interface with llama3 model |
| `ollama list` | List all downloaded models |
| `ollama pull llama3` | Download the llama3 model |
| `ollama show llama3` | Show metadata and info about llama3 |




---

## 🔧 Model Management

| Command | Description |
|--------|-------------|
| `ollama create my-model -f Modelfile` | Create a custom model using a Modelfile |
| `ollama show llama3` | Show details of the llama3 model |
| `ollama rm llama3` | Remove the llama3 model |




---

## ⚙️ System & Runtime

| Command | Description |
|--------|-------------|
| `ollama serve` | Start the Ollama server manually |
| `docker run -it --gpus all -p 11434:11434 ollama/ollama run llama3` | Run Ollama in Docker with GPU support (Linux + NVIDIA only) |




---

## 📡 API Access

**Endpoint:**
```
POST http://localhost:11434/api/generate
```

**Example Payload:**
```json
{
  "model": "llama3",
  "prompt": "What is the capital of Hungary?"
}
```



---

## 🧪 Examples

| Command | Description |
|--------|-------------|
| `ollama run llama3` | Start chat interface |
| `ollama run llama3 --prompt "Explain gravity in simple terms"` | Start with an initial prompt |




---

## 🧪 Advanced

| Command | Description |
|--------|-------------|
| `ollama create my-model -f Modelfile` | Build custom models (inside container) |
| `ollama run llama3 --prompt "Hello"` | Start with custom prompt |




---

## 🧹 Cleanup

| Command | Description |
|--------|-------------|
| `ollama list \| awk '{print $1}' \| xargs -n1 ollama rm` | Remove all downloaded models |






Happy experimenting! 🚀






---
## 🤝 Contributors

<table style="font-family: Arial, sans-serif; line-height: 1.6;">
  <tr>
    <td><strong>János Rostás</strong></td>
    <td>
      👨‍💻 Electronic & Computer Engineer (Final Year Student)<br>
      🧠 Passionate about AI, LLMs, and RAG systems<br>
      🐳 Docker & Linux Power User<br>
      🔧 Raspberry Pi Builder | Automation Fanatic<br>
      💻 Git & GitHub DevOps Explorer<br>
      📦 Loves tinkering with Ollama, containerized models, and APIs<br>
      🌐 <a href="https://janosrostas.co.uk" target="_blank">janosrostas.co.uk</a><br>
      🔗 <a href="https://www.linkedin.com/in/janos-rostas/" target="_blank">LinkedIn</a><br>
      🐙 <a href="https://github.com/Janos11" target="_blank">GitHub</a> |
      🐋 <a href="https://hub.docker.com/u/janos11" target="_blank">Docker Hub</a>
    </td>
  </tr>
  <tr>
    <td><strong>ChatGPT</strong></td>
    <td>
      🤖 AI Pair Programmer by OpenAI<br>
      💡 Collaborates on brainstorming, prototyping, and debugging<br>
      📚 Built on a foundation of global programming knowledge<br>
      🔍 Assists with everything from low-level scripting to high-level LLM orchestration
    </td>
  </tr>
</table>



