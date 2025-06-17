# app/scripts/main.py

# from app.models.ollama_llm import load_ollama_model


# from app.rag.conversation_chain import create_conversation_chain
# from app.vectorstore.build import build_vectorstore
# from app.data_loader.document_loader import load_documents, split_documents
import time
from app.build_vectorstore.build_vectorstore import build_vectorstore
from app.data_loader.document_loader import load_documents,  split_documents
from app.RAG.conversation_chain import create_conversation_chain
from app.llama_llm.model import load_ollama_model




def run():
    docs = load_documents("./app/data/raw/un-general-debates.csv", limit=10)
    chunks = split_documents(docs)
    vectorstore = build_vectorstore(chunks)

    # Load model từ Ollama
    llm = load_ollama_model("llama3.2")

    # Tạo RAG chain
    conversation = create_conversation_chain(llm, vectorstore)


    """Test query with timing"""
    query = "How was racism mentioned in the speech? Answer in English"
    start_time = time.time()
    result = conversation.invoke({"question": query})
    end_time = time.time()
    
    print(f"Query processed in {end_time - start_time:.2f} seconds")
    print("Answer:", result["answer"])


if __name__ == "__main__":
    run()
