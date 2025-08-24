from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

print("="*50)
print("Hello World - OpenAi - LangChain")
print("="*50)
model = ChatOpenAI(model="gpt-5-nano", max_retries=0, max_tokens=50, temperature=0.5)
message = model.invoke("Hello World")

print(message.content)