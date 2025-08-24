from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

print("="*50)
print("Carregamento usando webbaseloader - LangChain")
print("="*50)

loader = WebBaseLoader("https://www.langchain.com/")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)

chunks = splitter.split_documents(docs)

for chunk in chunks:
    print(chunk)
    print("-"*50)