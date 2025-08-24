from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

print("="*50)
print("Chat Prompt - OpenAi - LangChain")
print("="*50)

system = ("system", "you are an assistant that answers questions in a {style} style")
user = ("user", "{question}")

chat_prompt = ChatPromptTemplate([system, user])

messages = chat_prompt.format_messages(style="funny", question="Who is Alan Turing?")

for msg in messages:
    print(f"{msg.type}: {msg.content}")

model = ChatOpenAI(model="gpt-5-nano",  max_retries=0, max_tokens=50, temperature=0.5)
result = model.invoke(messages)
print(result.content)