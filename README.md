# 📄 LLM Document Reviewer & Q&A (Qwen3 + Streamlit)

An **AI-powered document review assistant** that allows users to upload documents, receive an automatic summary, and ask any questions about the content.  
Built with **Streamlit** for the frontend and powered by **Qwen3 LLM** for natural language understanding.

---

## 📖 Overview
This project demonstrates how **Large Language Models (LLMs)** like **Qwen3** can be applied to **document analysis and review**.  

- Upload a document (e.g., PDF or text)  
- The AI generates a **brief summary** of the content  
- Ask **any question** about the document and get instant answers  

This makes it useful for:
- Reviewing research papers  
- Analyzing legal/financial documents  
- Quickly extracting key insights from long reports  

---

## 🤖 About Qwen3
[**Qwen3**](https://github.com/QwenLM/Qwen) is a **state-of-the-art open-source LLM** developed by Alibaba Cloud.  
- Supports **multi-turn conversations** with strong reasoning and comprehension.  
- Optimized for **efficiency and scalability**.  
- Excels in tasks like **document understanding, summarization, and Q&A**.  

👉 I chose Qwen3 for this project because it is **lightweight, powerful, and open-source**, making it ideal for experimenting with real-world applications like **document review assistants**.

---

## 🔥 Demo  

### Document Upload, Summary & Q&A  
<img width="1512" height="982" alt="Image" src="https://github.com/user-attachments/assets/828361ec-6bb0-4d7a-9278-6562d24820d1" />

*(Tip: you can add more screenshots or even a GIF to show the workflow — upload → summary → Q&A)*  

---

## 🛠 Tech Stack
- **Python 3.10+**  
- **Streamlit** – Interactive frontend  
- **Qwen3 LLM** – Core reasoning engine for document understanding  
- **LangChain (optional)** – For document parsing & embeddings  
- **FAISS / ChromaDB** – Vector database for efficient document search (if included)  

---

## ✨ Features
- 📂 Upload and process documents  
- 📝 Automatic document summarization  
- ❓ Ask any question about the uploaded document  
- ⚡ Instant and accurate responses powered by **Qwen3**  
- 🎨 User-friendly interface with Streamlit  

---

## 🚀 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/LLM-DocumentReviewer.git
   cd LLM-DocumentReviewer
