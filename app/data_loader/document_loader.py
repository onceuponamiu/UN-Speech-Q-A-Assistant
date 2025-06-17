# app/data_loader/document_loader.py
import pandas as pd
from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_documents(csv_path, limit=None):
    df = pd.read_csv(csv_path)
    if limit:
        df = df.head(limit)

    documents = []
    for _, row in df.iterrows():
        page_content = f"Session: {row['session']}\nYear: {row['year']}\nCountry: {row['country']}\nSpeech:\n{str(row['text']).strip()}"
        metadata = {"session": row["session"], "year": row["year"], "country": row["country"]}
        documents.append(Document(page_content=page_content, metadata=metadata))
    return documents

def split_documents(documents, chunk_size=2000, chunk_overlap=50):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ". ", " ", ""]
    )
    return splitter.split_documents(documents)
