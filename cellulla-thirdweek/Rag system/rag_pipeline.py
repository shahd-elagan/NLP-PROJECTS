from config import *
from rag.loaders.pdf_loader import load_pdfs
from rag.loaders.text_loader import load_texts
from rag.embeeding import EmbeddingModel
from rag.vectore_store import VectorStore
from rag.generator import Generator

def chunk_text(text, chunk_size, overlap):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap

    return chunks

class RAGPipeline:
    def __init__(self):
        # 1️ Load documents
        pdf_docs = load_pdfs(PDF_DIR)
        text_docs = load_texts(TEXT_DIR)

        all_docs = pdf_docs + text_docs

        # 2️ Chunk documents
        self.chunks = []
        for doc in all_docs:
            self.chunks.extend(
                chunk_text(doc, CHUNK_SIZE, CHUNK_OVERLAP)
            )

        # 3️ Embeddings
        self.embedder = EmbeddingModel(EMBEDDING_MODEL)
        embeddings = self.embedder.embed(self.chunks)

        # 4️ Vector DB
        self.vector_store = VectorStore(embeddings)

        # 5 Generator
        self.generator = Generator(GENERATION_MODEL)

    def ask(self, question):
        q_embedding = self.embedder.embed([question])[0]
        indices = self.vector_store.search(q_embedding, TOP_K)

        context = "\n".join([self.chunks[i] for i in indices])
        return self.generator.generate(context, question)
