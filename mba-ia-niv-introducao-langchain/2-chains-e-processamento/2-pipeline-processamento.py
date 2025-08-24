from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

print("="*50)
print("Pipeline - OpenAI - LangChain")
print("="*50)

template_translate = PromptTemplate(
    input_variables=["initial_text"],
    template="Translate the following text to English:\n ```{initial_text}````"
)

template_summary = PromptTemplate(
    input_variables=["text"],
    template="Summarize the following text in 4 words:\n ```{text}```"
)

llm_en = ChatOpenAI(model="gpt-5-nano", temperature=0)

translate = template_translate | llm_en | StrOutputParser()
pipeline = {"text": translate} | template_summary | llm_en | StrOutputParser()

# Solicita o texto em Português ao usuário
initial_text = input("Digite o texto em Português, vou traduzir para ingles e sumarizar em 4 palavras: \n")

result = pipeline.invoke({"initial_text": initial_text})

print("\nResultado Final: ")
print(result)