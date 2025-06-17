# app/vectorstore/build.py
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
import os

def build_vectorstore(documents, persist_directory="./app/data/vector_db"):
    embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-base-en-v1.5")
    
    if os.path.exists(persist_directory):
        Chroma(persist_directory=persist_directory, embedding_function=embeddings).delete_collection()

    vectorstore = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory=persist_directory
    )

    return vectorstore
