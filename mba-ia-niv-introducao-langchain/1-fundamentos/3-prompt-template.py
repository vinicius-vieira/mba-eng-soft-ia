from langchain.prompts import PromptTemplate

print("="*50)
print("Prompt - LangChain")
print("="*50)

template = PromptTemplate(
    input_variables=["name"],
    template="Hi, I'm {name}! Tell me a joke with my name!"
)

text = template.format(name="Vinicius")
print(text)