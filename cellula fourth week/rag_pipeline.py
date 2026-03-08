from vector_db import vectordb
from transformers import pipeline
from prompts import CODE_PROMPT

generator = pipeline("text-generation", model="microsoft/phi-2", max_new_tokens=200)

def retrieve_examples(query, k=1):
    docs = vectordb.similarity_search_with_score(query, k=k)
    return docs 

def learn_new_knowledge(query):
    print("\n[Organism] I don't recognize this coding challenge.")
    solution = input("Please teach me the correct solution: ")
    
    vectordb.add_texts(texts=[query], metadatas=[{"solution": solution}])
    print("[Organism] Knowledge acquired! I will remember this.")

def generate(query):
    results = retrieve_examples(query)
    doc, score = results[0]
    
 
    if score > 0.6: 
        learn_new_knowledge(query)
        results = retrieve_examples(query)
        doc = results[0][0]

    context = doc.metadata.get("solution")
    prompt = CODE_PROMPT.format(context=context, question=query)
    return generator(prompt)[0]["generated_text"]