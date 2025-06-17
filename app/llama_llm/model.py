# app/models/ollama_llm.py

from langchain_ollama import ChatOllama

def load_ollama_model(model_name="llama3.2"):
    return ChatOllama(
        model=model_name,
    )
