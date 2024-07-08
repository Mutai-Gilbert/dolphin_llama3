from query_llm import query_llm

def get_dark_web_info(query):
    prompt = f"Provide detailed information on the following dark web query: {query}"
    response = query_llm(prompt)
    return response

if __name__ == "__main__":
    query = input("Enter your dark web query: ")
    info = get_dark_web_info(query)
    print(info)
