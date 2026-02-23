from transformers import pipeline

class Generator:
    def __init__(self, model_name):
        self.pipe = pipeline(
            "text2text-generation",
            model=model_name
        )

    def generate(self, context, question):
        prompt = f"""
        Use the context below to answer the question.

        Context:
        {context}

        Question:
        {question}
        """
        output = self.pipe(prompt, max_length=256)
        return output[0]["generated_text"]
