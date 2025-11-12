from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter 

# Load documentation from directory
loader = PyPDFDirectoryLoader("cooking_docs", mode="single")
documents = loader.load()

# Split into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200 ) 
chunks = splitter.split_documents(documents)

from langchain_huggingface import HuggingFaceEndpointEmbeddings
from langchain_community.vectorstores import FAISS

# Create embeddings and vector store
embedder = HuggingFaceEndpointEmbeddings(model="BAAI/bge-base-en-v1.5", task="feature-extraction", )
vector_store = FAISS.from_documents(chunks, embedder)

query = "How do I cook salmon with herbs?"
# Similarity search
relevant_docs = vector_store.similarity_search(query, k=3)

# Create a context string
context = "\n\n".join(doc.page_content for doc in relevant_docs) 
