# app/rag/conversation_chain.py

from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferWindowMemory

def create_conversation_chain(llm, vectorstore):
    memory = ConversationBufferWindowMemory(memory_key="chat_history", return_messages=True)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 10})
    
    return ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory
    )
