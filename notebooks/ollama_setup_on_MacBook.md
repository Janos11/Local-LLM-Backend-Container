# 🦙 Ollama Setup

<div align="center">
  <a href="https://ollama.com">
    <img alt="ollama" width="240" src="https://github.com/ollama/ollama/assets/3325447/0d0b44e2-8f4a-4e99-9b52-a5c1c741c8f7">
  </a>
</div>

[🦙 Ollama GitHub repo](https://github.com/ollama/ollama)

This guide provides step-by-step instructions to set up and run Ollama, a platform for locally running large language models (LLMs), using Docker.

---

## Prerequisites

- Docker installed on your system.
- Docker Compose installed for managing the container.




---
## Step 1: Set Up the Ollama Docker Container

Create a docker-compose.yml file to define the Ollama service configuration. 
You can find a sample configuration in the Ollama GitHub repository or create a basic one as follows:
[docker-compose.yml](../docker-compose.yml)

`docker compose up -d`
This command pulls the Ollama Docker image and starts the container.



---
## Step 2: Verify the Container is Running

Check if the container is running by listing active containers:

- get port number `docker ps` 
- in browser `http://localhost:11434`
- command line: `curl http://localhost:11434/api/tags`

This should return a JSON response indicating the service is operational.



---
## Step 3: Pull and Run Models

Pull a model into the container. For example, to pull the llama3 model:

`docker exec -it ollama ollama pull llama3`

`docker exec -it ollama ollama pull llama3:8b` - 4.7 GB

`docker exec -it ollama ollama pull llama3:70b`


---
## Step 4: Run a model using the ollama run command. For example:

`docker exec -it ollama ollama run llama3`

You can switch between models by running different ollama run commands, such as:

`docker exec -it ollama ollama run llama3:8b`<br/>
`docker exec -it ollama ollama run mistral`

Models are cached in the container’s volume (/root/.ollama), allowing you to switch between them without re-downloading.





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
