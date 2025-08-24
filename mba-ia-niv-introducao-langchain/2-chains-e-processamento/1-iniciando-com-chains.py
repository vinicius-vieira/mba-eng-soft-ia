from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

print("="*50)
print("Chains Base - OpenAI - LangChain")
print("="*50)

question_template = PromptTemplate(
    input_variables=["name"],
    template="Hi, I'm {name}! Tell me a joke with my name!"
)

model = ChatOpenAI(model="gpt-5-nano", temperature=0.5)

chain = question_template | model

# solicita o nome do via console
name = input("Qual é o seu nome? ")

result = chain.invoke({"name": name})

print(result.content)