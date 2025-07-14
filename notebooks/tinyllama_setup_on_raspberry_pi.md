# Tiny Llama setup on Raspberry pi



---

<p align="center">
  <a href="https://ollama.com/library/tinyllama" target="_blank" rel="noopener noreferrer">
    <img src="../screenshots/tiny_llama.png" alt="Watch the demo on LinkedIn" width="300" />
  </a>
</p>

<p align="center">
  <a href="https://ollama.com/library/tinyllama" target="_blank" rel="noopener noreferrer">🦙 Tiny Llama GitHub Repo</a>
</p>




---
### 1.  Download `tinyllama` - 638MB

TinyLlama is a compact model with only 1.1B parameters. 
[Tiny Llama GitHub Repo](https://ollama.com/library/tinyllama)
```bash
docker exec -it ollama ollama run tinyllama
```



---

## ✅ What You Can Use TinyLlama For
|✅ Good At |	🚫 Not Great At |
|------------|------------|
|Completing simple sentences |	Accurate Q&A |
|Playing with prompt formats |	Factual knowledge |
|Testing infrastructure/setup |	Long-term memory / dialogue |

If you just need to demonstrate a local LLM running on a Pi (as proof of concept), TinyLlama is perfect. But if you want reliable responses, you’ll need a larger or better-tuned model (which your Pi likely can’t run alone).

## 💡 Next Steps
If you're curious to try better tiny models:

| Model       | Size     | Notes                             |
|-------------|----------|-----------------------------------|
| `phi-2`     | ~1.7 GB  | More coherent, still very light   |
| `qwen:1.5b` | ~2.0 GB  | Good multilingual support         |
| `mistral:7b`| ~4–5 GB  | Too big for Pi alone, great on GPU|
| `dolly:1b`  | ~1.5 GB  | Some instruction tuning           |

