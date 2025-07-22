# 🧠 Agentic RAG Chatbot

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/AmanDataverse/Agentic_RAG_chatbot)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/project-active-success)]()

A multi-format, document-based **Retrieval-Augmented Generation (RAG)** chatbot enhanced with a modular **agentic architecture** and **Model Communication Protocol (MCP)**. Developed to demonstrate proficiency in real-world AI tooling, scalable system design, and intelligent QA workflows for enterprise use cases.

---

## 📌 Problem Statement

Organizations deal with large volumes of unstructured documents. Extracting knowledge from such formats often requires contextual understanding, not just keyword search. This system enables natural language querying over documents of varied formats using LLMs, retrieval systems, and modular agents.

---

## 🚀 Key Features

✅ Upload PDFs, DOCX, PPTX, TXT, CSV, Markdown  
✅ Agent-based architecture: Ingestion, Retrieval, and LLM Response  
✅ FAISS-based similarity search  
✅ Real-time Q&A using Streamlit chatbot UI  
✅ Displays **retrieved chunks** for transparency  
✅ Modular, testable, and extensible codebase  
✅ Supports OpenAI / Groq APIs

---

## 🧰 Tech Stack

| Layer           | Technology                              |
|-----------------|------------------------------------------|
| UI              | `Streamlit`                              |
| Backend         | `Python` (OOP-based modular agents)      |
| Embeddings      | `SentenceTransformers (MiniLM-L6-v2)`    |
| Vector Database | `FAISS`                                  |
| LLM APIs        | `OpenAI`, `Groq`                         |
| Document Parsing| `PyMuPDF`, `python-docx`, `python-pptx`  |

---

## 📊 Workflow

```mermaid
flowchart TD
  A[User Uploads File] --> B[Text Chunking]
  B --> C[Embedding]
  C --> D[Indexing]
  D --> E[User Asks Question]
  E --> F[Top-K Retrieval]
  F --> G[LLM Answer + Sources]
```

## 📁 Project Structure

```text
agentic_rag_chatbot/
│
├── 🧠 agents/               → Core logic for:
│     ├── ingestion_agent.py       (Document chunking)
│     ├── retrieval_agent.py       (Similarity search using FAISS)
│     └── llm_response_agent.py    (Response generation using LLMs)
│
├── 📂 data/                → Stores uploaded files
├── 📂 db/                  → FAISS index and pickled vector store
├── 🖥️ ui/                  → Streamlit frontend for user interaction
├── 🧰 utils/               → Utility scripts (MCP protocol, helpers)
│
├── 📄 .env                 → Environment variables (API keys etc.)
├── 📦 requirements.txt     → List of Python dependencies
├── 📘 README.md            → Project documentation
└── 🚫 .gitignore           → Files/directories to be ignored by Git

```
```
```
## 🎬 Demo Video

```
[![Watch the demo]](media/Demo_Agentic_RAG_CHATBOT.mp4)

```