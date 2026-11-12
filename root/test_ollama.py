from langchain_ollama import ChatOllama
from dotenv import load_dotenv

load_dotenv()

model = ChatOllama(
    model="llama3.2",
    temperature=0,
)

result = model.invoke("whats capital of india?")
print(result)

""""
o/p:
content='The capital of India is New Delhi.' additional_kwargs={} response_metadata={'model': 'llama3.2', 'created_at': '2026-11-08T22:28:03.3411439Z', 'done': True, 'done_reason': 'stop', 'total_duration': 5139158600, 'load_duration': 3860319800, 'prompt_eval_count': 31, 'prompt_eval_duration': 366982000, 'eval_count': 9, 'eval_duration': 897313000, 'logprobs': None, 'model_name': 'llama3.2', 'model_provider': 'ollama'} id='lc_run--01a1bd46-8678-7226-a32b-fb17fd997729-0' tool_calls=[] invalid_tool_calls=[] usage_metadata={'input_tokens': 31, 'output_tokens': 9, 'total_tokens': 40}
(.envr) PS D:\PythonApp\LangChainPrompts> 
"""