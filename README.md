# 🧠 UN Speech Q&A Assistant

A conversational AI assistant that helps explore over four decades of United Nations General Debate speeches from 1970 to 2016.

Powered by **Retrieval-Augmented Generation (RAG)**, this app allows users to ask questions and gain insights into world leaders' statements during UN General Assemblies.

---

## 📂 Dataset Overview

- **Source**: [UN General Debate Corpus (UNGDC)]  
- **Authors**: Alexander Baturo, Niheer Dasandi, Slava Mikhaylov  
- **Published in**: _Research & Politics_, 2017

The dataset contains speeches from **UN member states** delivered at the General Debate from **1970 to 2016**. Each record includes:

- Full speech text (in English)  
- Country  
- Year and session  
- OCR-processed, cleaned text  

---

## 🔍 Use Cases

This project enables rich exploration and analysis of:

- 📈 Sentiment trends over time  
- 🌍 Regional and temporal topic shifts  
- ✍️ Linguistic and stylistic differences  
- 🏛️ Country-specific foreign policy themes  

You can ask natural questions like:

- “What did France say about climate change in 2015?”  
- “How has the tone of US speeches changed since the Cold War?”  
- “Which countries mentioned nuclear disarmament most?”  

---

## 💡 Project Purpose

To build an AI-powered virtual assistant that uses **natural language** to answer user questions about the UN General Debate speeches.

---

## 🛠️ Tech Stack

- **Python** 🐍  
- **LangChain** for Retrieval-Augmented Generation  
- **Ollama + LLaMA3.2 model** (local or remote)  
- **Streamlit** for interactive UI  
- **ChromaDB** as vector store  
- **scikit-learn**, **transformers**, **sentence-transformers** for embedding and NLP

---

## 🚀 How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/your-username/un-speech-assistant.git
cd un-speech-assistant
