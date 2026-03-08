def route_query(query):
    query_lower = query.lower()

    explain_keywords = ["explain", "how does", "what is", "walk through", "describe"]
    if any(word in query_lower for word in explain_keywords):
        return "explain"
        

    generate_keywords = ["write", "generate", "create", "implement", "code", "function"]
    if any(word in query_lower for word in generate_keywords):
        return "generate"
        

    return "explain"