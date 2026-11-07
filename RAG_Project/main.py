from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

pdf_path = Path(__file__).parent/"sample.pdf"
loader = PyPDFLoader(file_path=str(pdf_path))
docs = loader.load()

# print(docs[0].metadata)

# Recursive Character Splitting

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len
)

chunks = splitter.split_documents(docs)
print(f"Number of chunks: {len(chunks)}")
