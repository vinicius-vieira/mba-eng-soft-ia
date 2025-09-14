import os
from dotenv import load_dotenv

from langchain_openai import OpenAIEmbeddings
from langchain_postgres import PGVector
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.messages import trim_messages
from langchain_core.runnables import RunnableLambda

load_dotenv()

print("="*50)
print("Desafio LangChain - Parte 2: Pesquisa no pgVector (RAG)")
print("="*50)

for k in ("OPENAI_API_KEY", "PGVECTOR_URL","PGVECTOR_COLLECTION_R175"):
    if not os.getenv(k):
        raise RuntimeError(f"Environment variable {k} is not set")

embeddings = OpenAIEmbeddings(model=os.getenv("OPENAI_MODEL","text-embedding-3-small"))

store = PGVector(
    embeddings=embeddings,
    collection_name=os.getenv("PGVECTOR_COLLECTION_R175"),
    connection=os.getenv("PGVECTOR_URL"),
    use_jsonb=True,
)

prompt = ChatPromptTemplate.from_messages([
    ("system", ''' 
        CONTEXTO:
        {context}    
   
        REGRAS:            
        - Responda somente com base no CONTEXTO.
        - Se a informação não estiver explicitamente no CONTEXTO, responda:
            "Não tenho informações necessárias para responder sua pergunta."
        - Nunca invente ou use conhecimento externo.
        - Nunca produza opiniões ou interpretações além do que está escrito.

        EXEMPLOS DE PERGUNTAS FORA DO CONTEXTO:
        Pergunta: "Qual é a capital da França?"
        Resposta: "Não tenho informações necessárias para responder sua pergunta."

        Pergunta: "Quantos clientes temos em 2024?"
        Resposta: "Não tenho informações necessárias para responder sua pergunta."

        Pergunta: "Você acha isso bom ou ruim?"
        Resposta: "Não tenho informações necessárias para responder sua pergunta."
     
        PERGUNTA DO USUÁRIO:
        {input}
     
        RESPONDA A "PERGUNTA DO USUÁRIO"
    '''),
    MessagesPlaceholder("history"),
    ("human", "{input}"),
])

llm = ChatOpenAI(model=os.getenv("OPENAI_CHAT_MODEL", "gpt-5-nano"), temperature=0.2)

TOP_K = 10
HISTORY_RETURNS = 5
MAX_MESSAGES = HISTORY_RETURNS * 2 

def build_context_from_store(question: str) -> str:
    docs = store.similarity_search(question, k=TOP_K)
    if not docs:
        return ""
    parts = []
    for i, d in enumerate(docs, 1):
        meta = ", ".join(f"{k}: {v}" for k, v in (d.metadata or {}).items())
        parts.append(f"Trecho {i}:\n{d.page_content.strip()}\nMetadados: {meta}\n")
    return "\n\n".join(parts)


def prepare_inputs(payload: dict) -> dict:
    raw_history = payload.get("raw_history", [])
    trimmed = trim_messages(
        raw_history,
        token_counter=len,
        max_tokens=MAX_MESSAGES,
        strategy="last",
        start_on="human",
        include_system=True,
        allow_partial=False,
    )
    question = payload.get("input", "")
    context = build_context_from_store(question)
    return {"input": question, "history": trimmed, "context": context}


prepare = RunnableLambda(prepare_inputs)
chain = prepare | prompt | llm

session_store: dict[str, InMemoryChatMessageHistory] = {}


def get_session_history(session_id: str) -> InMemoryChatMessageHistory:
    if session_id not in session_store:
        session_store[session_id] = InMemoryChatMessageHistory()
    return session_store[session_id]


conversational_chain = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="raw_history",
)

config = {"configurable": {"session_id": "r175-chat"}}

print("\nDigite sua pergunta sobre a Resolução 175 (ou 'sair' para encerrar).\n")

while True:
    try:
        user_q = input("Você: ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\nEncerrando a conversa. Até mais!")
        break

    if not user_q:
        continue
    if user_q.lower() in {"sair", "exit", "quit"}:
        print("Encerrando a conversa. Até mais!")
        break

    resp = conversational_chain.invoke({"input": user_q}, config=config)
    print(f"\nEspecialista: {resp.content}\n")

    try:
        cont = input("Você tem mais dúvidas? (s/n): ").strip().lower()
    except (EOFError, KeyboardInterrupt):
        print("\nEncerrando a conversa. Até mais!")
        break
    if cont not in {"s", "sim", "y", "yes"}:
        print("Conversa encerrada. Obrigado!")
        break
