from langchain_openai import ChatOpenAI

LOCAL_BASE_URL = "http://localhost:12434/engines/v1"

def get_llm():
    llm =  ChatOpenAI(
        base_url=LOCAL_BASE_URL,
        api_key='docker',
        model = 'ai/llama3.2',
        max_completion_tokens=2000
    )

    return llm
 