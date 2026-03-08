from router import route_query
from rag_pipeline import generate
from prompts import EXPLAIN_PROMPT
from transformers import pipeline
from memory import memory

explainer = pipeline(
    "text-generation",
    model="microsoft/phi-2",
    max_new_tokens=200
)

def explain(query):
    prompt = EXPLAIN_PROMPT + "\nUser: " + query
    result = explainer(prompt)[0]["generated_text"]
    return result

def main():
    print("AI Coding Assistant (type 'exit' to stop)\n")

    while True:
        query = input("You: ")

        if query.lower() == "exit":
            break

        route = route_query(query)

        if route == "generate":
            response = generate(query)
        else:
            response = explain(query)

        print("\nAssistant:\n", response, "\n")

if __name__ == "__main__":
    main()