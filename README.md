# 📚 Flashcard Generator App

An interactive Streamlit app that uses a lightweight LLM (`flan-t5-small`) to generate educational flashcards from user-provided **text** or **PDF** content.

---

## 🚀 Features

- 🔁 Generate multiple Q&A flashcards from any text input.
- 📄 Upload PDF files for automatic flashcard generation.
- 📌 Simple, responsive Streamlit interface.
- 💡 Built using Hugging Face Transformers (`flan-t5-small`).

---

## 🖥️ Tech Stack

- Python 3.10+
- [Streamlit](https://streamlit.io/)
- [Transformers](https://huggingface.co/docs/transformers/index)
- PyPDF2

---

## 📸 Demo

![App Screenshot](screenshot.png)

---

## 🛠️ Installation

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
python -m venv venv
venv\Scripts\activate  # On Windows
# Or source venv/bin/activate for macOS/Linux

pip install -r requirements.txt
