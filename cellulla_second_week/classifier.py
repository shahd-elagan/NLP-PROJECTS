from transformers import pipeline

classifier = pipeline("text-classification")

def classify_text(text):

    result = classifier(text)

    label = result[0]["label"]
    score = result[0]["score"]

    return label, score