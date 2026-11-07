from pathlib import Path
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_qdrant import QdrantVectorStore
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq


load_dotenv()

pdf_path = Path(__file__).parent/"sample.pdf"
loader = PyPDFLoader(file_path=str(pdf_path))
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len
).split_documents(docs)


embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vector_store = QdrantVectorStore.from_documents(
     documents=splitter,
     embedding=embeddings,
     collection_name="rag_collection",
     url="http://localhost:6333")

print("Indexing completed. Number of chunks indexed:", len(splitter))
