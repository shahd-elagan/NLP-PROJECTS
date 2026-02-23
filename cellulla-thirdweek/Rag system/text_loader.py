import os

def load_texts(text_dir):
    documents = []

    for file in os.listdir(text_dir):
        if file.endswith(".txt"):
            path = os.path.join(text_dir, file)
            with open(path, "r", encoding="utf-8") as f:
                text = f.read().strip()
                if text:
                    documents.append(text)

    return documents
