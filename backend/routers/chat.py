import os
from fastapi import APIRouter
from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from langchain_community.vectorstores.faiss import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_community.llms import HuggingFaceHub

from pydantic import BaseModel


from dotenv import load_dotenv

load_dotenv()

class Query(BaseModel):
    question: str

router = APIRouter(
    prefix="/chat",
    tags=["chat"],
    responses={404: {"description": "Not found"}},
)

embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-base")
vectordb = None
conversation_chain = None
aaa = "=============================================================================="

@router.post("/")
async def userChat(query : Query):
    global vectordb
    global conversation_chain
    if not vectordb:
        vectordb = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    
    if not conversation_chain:
        llm = HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature":1})

        memory = ConversationBufferMemory(
            memory_key='chat_history', return_messages=True)
        
        conversation_chain = ConversationalRetrievalChain.from_llm(
            llm=llm,
            retriever=vectordb.as_retriever(),
            memory=memory,
        )

    res = conversation_chain({"question": query.question})
    return {"response" : res['chat_history'][-1]}