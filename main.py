# main.py

import os
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_groq import ChatGroq
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone, ServerlessSpec

from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# LOAD ENV

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")


# LOAD PDF 


def load_and_index():
    loader = PyPDFLoader("air-india-general-booking-policies.pdf")
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=60)
    chunks = splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()

    pc = Pinecone(api_key=PINECONE_API_KEY)
    INDEX_NAME = "rag-pdf-index"

    if INDEX_NAME not in pc.list_indexes().names():
        pc.create_index(name=INDEX_NAME,dimension=1536,metric="cosine",spec=ServerlessSpec(cloud="aws", region="us-east-1"))

    vector_db = PineconeVectorStore.from_documents(documents=chunks,embedding=embeddings,index_name=INDEX_NAME)

    return vector_db


# CREATE CHAIN

def create_rag_chain():

    embeddings = OpenAIEmbeddings()

    vector_db = PineconeVectorStore(index_name="rag-pdf-index",embedding=embeddings)

    retriever = vector_db.as_retriever(search_kwargs={"k": 5})

    prompt = ChatPromptTemplate.from_template("""You are a strict assistant.
                                              Answer ONLY using the context.
                                              Give a SHORT answer in ONE sentence.
                                              Do NOT explain.If answer not found, say "No answer found".
                                              Context:{context}
                                              Question:{question}""")

    llm = ChatGroq(model="llama-3.1-8b-instant",api_key=GROQ_API_KEY)

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    rag_chain = ({"context": retriever | format_docs,"question": RunnablePassthrough()}
        | prompt| llm| StrOutputParser())

    return rag_chain



rag_chain = create_rag_chain()

def ask_question(query: str):
    return rag_chain.invoke(query)