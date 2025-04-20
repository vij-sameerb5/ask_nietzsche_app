#  Ask Nietzsche – AI Philosophy Chatbot'

**Ask Nietzsche** is an AI-powered chatbot that answers your deepest existential, moral, and philosophical questions in the style of **Friedrich Nietzsche**, blending historical insight with modern AI. Built using Streamlit and OpenAI's language models, this app aims to make Nietzsche's philosophy accessible, conversational, and oddly motivating.

## ✨ Features

- 🗣️ Ask any life/philosophy-related question
- 📜 Choose between "Classic Nietzsche" (authentic quotes) or "Modern Nietzsche" (AI-generated responses)
- 🧠 Smart prompt engine trained on Nietzsche's core ideas (e.g., Will to Power, Eternal Recurrence)
- 📚 Quote retrieval using embeddings (vector search coming soon)
- 🕰️ Long-term memory agent (in progress)
- 🔧 Modular agent-based architecture MVP Phase

## 📦 Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Backend**: Python, OpenAI API
- **AI Agent Framework**: LangChain (planned)
- **Data**: Nietzsche’s public domain texts + curated quote DB
- **Optional**: FAISS for vector-based quote retrieval (for smart responses)

## 🚀 Getting Started

### 1. Clone the Repository

    ```bash
        git clone https://github.com/vij-sameerb5/ask-nietzsche.git
        cd ask-nietzsche

    ```bash
      pip install -r requirements.txt

      ```bash
      streamlit run ask_nietzsche.py

🚀 What’s Happened So Far
MVP Scaffold

Built a Streamlit app (ask_nietzsche.py) with Classic (quote lookup) and Modern (LLM‑generated) modes.

Created modular agents: PromptDesigner, ContextAgent, ResponseGenerator, CriticAgent, MemoryAgent.

Modern Mode Integration

Hooked up a Hugging Face Llama 2 Chat‑HF model via transformers.from_pretrained(...).

Installed SentencePiece and authenticated with your HF token.

Gating & Download Errors

Hit 403 errors because Llama 2 Chat‑HF is gated—needed to request access on Hugging Face.

Tried a direct download script (snapshot_download) but still lacked permissions.

Performance Tuning

Tried bitsandbytes 8‑bit quant on MPS (failed—unsupported on Apple GPUs).

Reviewed three paths to get fast, free inference.

🔧 What We’re Doing Right Now
You chose Option C: run a quantized GGML binary via llama-cpp-python:

Converted the PyTorch Llama 2 Chat‑HF weights into a 4‑bit GGML file (.ggml.q4_0.bin).

Installed the llama-cpp-python binding.

Rewired ResponseGenerator to load that local GGML file and generate on CPU in ~1–3 s per reply.

Your Streamlit app now uses this pure‑local, zero‑API‑fee backend.

🔄 The Three Options We Discussed

Option	How It Works	Speed	Cost	Pros / Cons
A) GPT‑3.5‑Turbo	OpenAI API calls for each reply	~0.5–1 s	$0.002/1K tokens	Fastest iteration; pay‑per‑use fees
B) Smaller HF Model	Use a lighter public model (e.g. Mistral 7B) on MPS	~3–5 s	$0 (once cached)	No gating; simpler transformers code
C) GGML Quant (you chose)	Load a Q4_0 binary via llama-cpp-python	~1–3 s	$0	Fully local; no GPU required
🏁 Next Steps
Verify that “Modern Nietzsche” now returns a true continuation in Nietzsche’s tone.

Tweak sampling (temperature, top_p, max_tokens) in your llama_cpp call to get the voice and length you like.

Polish your PromptDesigner or add follow‑up prompts to enrich the dialogue.

Expand your quotes.json and tests so Classic mode covers more topics.

Deploy (Streamlit Cloud or Hugging Face Spaces) and share your Nietzsche chat with the world!

Let me know how the CPU‑quantized model feels, and we can adjust any final parameters together.







