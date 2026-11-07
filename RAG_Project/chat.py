from dotenv import load_dotenv
import os
import groq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_qdrant import QdrantVectorStore

load_dotenv()

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectore_store = QdrantVectorStore.from_existing_collection(
    embedding=embeddings,
    collection_name="rag_collection",
    url="http://localhost:6333"
)


user_query = "What is the main topic of the document?"

search_results = vectore_store.similarity_search(query=user_query, k=3)

context = "\n\n".join(
    f"Page Content: {r.page_content}\n"
    f"Page Number: {r.metadata.get('page_label')}\n"
    f"File Location: {r.metadata.get('source')}"
    for r in search_results
)

system_prompt = f"""
You are a helpful AI assistant who answers user queries based on the
available context retrieved from a PDF file along with page content and page number.
You should only answer based on the following context and navigate the
user to open the right page number to know more.

Context:
{context}
"""

client = groq.Client(api_key = os.getenv('Groq_API'))

response = client.chat.completions.create(
    model = "openai/gpt-oss-120b",
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_query}
    ]

)

print("\n🤖", response.choices[0].message.content)