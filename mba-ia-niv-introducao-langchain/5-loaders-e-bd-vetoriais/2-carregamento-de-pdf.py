from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

print("="*50)
print("Carregamento de pdf - LangChain")
print("="*50)


current_dir = Path(__file__).parent
pdf_path = current_dir / "gpt5.pdf"

docs = PyPDFLoader(str(pdf_path)).load()

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)

chunks = splitter.split_documents(docs)

print("Leu e quebrou o pdf em {} pedaços".format(len(chunks)))
print("Exemplo de 3 pedaços:\n")
print(chunks[0])
print("-"*50)
print(chunks[1])
print("-"*50)
print(chunks[2])
