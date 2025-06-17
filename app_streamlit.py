import streamlit as st
import time
from app.data_loader.document_loader import load_documents, split_documents
from app.build_vectorstore.build_vectorstore import build_vectorstore
from app.llama_llm.model import load_ollama_model
from app.RAG.conversation_chain import create_conversation_chain

# Streamlit UI
st.set_page_config(page_title="UN Speech Q&A Assistant", layout="wide")

st.title("💬 United Nations Speech Analysis Assistant")
st.write("Enter your question to retrieve insights from UN General Debate speeches.")

# Load documents and setup the model
with st.spinner("🔄 Loading data and initializing model..."):
    docs = load_documents("./app/data/raw/un-general-debates.csv", limit=10)
    chunks = split_documents(docs)
    vectorstore = build_vectorstore(chunks)
    llm = load_ollama_model("llama3.2")
    conversation_chain = create_conversation_chain(llm, vectorstore)

# Initialize session chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input question
if query := st.chat_input("Enter your question..."):
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)

    # Answer from LLM
    with st.chat_message("assistant"):
        with st.spinner("🧠 Processing..."):
            start = time.time()
            result = conversation_chain.invoke({"question": query})
            duration = time.time() - start

            answer = result["answer"]
            st.success(f"✅ Answer generated in {duration:.2f} seconds")
            st.markdown(answer)

            # Show source documents if available
            if "source_documents" in result:
                with st.expander("📚 Source Documents"):
                    for i, doc in enumerate(result["source_documents"], 1):
                        st.markdown(f"**Source #{i}:**\n```\n{doc.page_content[:300]}...\n```")

    st.session_state.messages.append({"role": "assistant", "content": answer})
