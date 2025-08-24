from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
load_dotenv()

print("="*50)
print("Chat Prompt - GemAi - LangChain")
print("="*50)

system = ("system", "you are an assistant that answers questions in a {style} style")
user = ("user", "{question}")

chat_prompt = ChatPromptTemplate([system, user])

messages = chat_prompt.format_messages(style="funny", question="Who is Alan Turing?")

for msg in messages:
    print(f"{msg.type}: {msg.content}")

model = init_chat_model(model="gemini-2.5-flash", model_provider="google_genai")
result = model.invoke(messages)
print(result.content)