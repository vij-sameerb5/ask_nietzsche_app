#  Ask Nietzsche – AI Philosophy Chatbot

**Ask Nietzsche** is an AI-powered chatbot that answers your deepest existential, moral, and philosophical questions in the style of **Friedrich Nietzsche**, blending historical insight with modern AI. Built using Streamlit and OpenAI's language models, this app aims to make Nietzsche's philosophy accessible, conversational, and oddly motivating.

## ✨ Features

- 🗣️ Ask any life/philosophy-related question
- 📜 Choose between "Classic Nietzsche" (authentic quotes) or "Modern Nietzsche" (AI-generated responses)
- 🧠 Smart prompt engine trained on Nietzsche's core ideas (e.g., Will to Power, Eternal Recurrence)
- 📚 Quote retrieval using embeddings (vector search coming soon)
- 🕰️ Long-term memory agent (in progress)
- 🔧 Modular agent-based architecture (MVP phase)

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
