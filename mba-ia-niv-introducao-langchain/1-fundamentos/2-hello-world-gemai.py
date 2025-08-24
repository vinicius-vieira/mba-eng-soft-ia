from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
load_dotenv()

print("="*50)
print("Hello World - GemAi - LangChain")
print("="*50)

gemini = init_chat_model(model="gemini-2.5-flash", model_provider="google_genai")
answer_gemini = gemini.invoke("Hello World")
print(answer_gemini.content)