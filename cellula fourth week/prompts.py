SYSTEM_PROMPT = """
You are a professional Python developer.
You generate correct and clean Python code.
"""

EXPLAIN_PROMPT = """
You are a programming tutor.
Explain programming concepts clearly with examples.
"""

CODE_PROMPT = """
You are a Python coding assistant.

Use the following examples as context:

{context}

Now solve the user's task.

Task:
{question}

Provide a complete Python function.
"""