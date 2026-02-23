import os  # for file path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # folder finding 

PDF_DIR = os.path.join(BASE_DIR, "data", "pdfs")
TEXT_DIR = os.path.join(BASE_DIR, "data", "texts")

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
GENERATION_MODEL = "google/flan-t5-base"

CHUNK_SIZE = 400
CHUNK_OVERLAP = 50
TOP_K = 4


#pip install -r requirements.txt


