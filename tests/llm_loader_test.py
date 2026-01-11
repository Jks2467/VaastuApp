from utils.llm import get_llm

llm = get_llm()

messages = [
            {
                "role": "user",
                "content": "What is the capital of Indonesia?"
            }
]

resp = llm.invoke(messages)
print(resp.content)

# python -m tests.llm_loader_test