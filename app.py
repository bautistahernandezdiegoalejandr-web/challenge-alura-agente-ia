import streamlit as st
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

# Configurar API Key de forma segura desde los secretos de Streamlit
if "GOOGLE_API_KEY" in st.secrets:
    os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]

# Configuración de la página en Streamlit
st.set_page_config(page_title="Agente IA - Atenea Online", page_icon="🤖")
st.title("🤖 Asistente Virtual Corporativo (Atenea Online)")
st.write("Pregúntame cualquier duda sobre las normativas y documentos de la empresa.")

# 1. Cargar y procesar el PDF de forma automática al iniciar la app
@st.cache_resource
def inicializar_rag():
    pdf_path = "documento_empresa.pdf"
    loader = PyPDFLoader(pdf_path)
    documentos = loader.load()
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    documentos_procesados = text_splitter.split_documents(documentos)
    
    embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")
    vector_store = FAISS.from_documents(documentos_procesados, embeddings)
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})
    
    # Usamos gemini-1.5-flash optimizado para la API actual
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.3)
    
    system_prompt = (
        "Eres un asistente virtual corporativo útil y amable para Atenea Online. "
        "Usa los siguientes fragmentos de contexto recuperado para responder a la pregunta. "
        "Si no sabes la respuesta basada en el contexto, di que no tienes esa información."
        "\n\n{context}"
    )
    prompt = ChatPromptTemplate.from_messages([("system", system_prompt), ("human", "{input}")])
    
    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    return create_retrieval_chain(retriever, question_answer_chain)

# Inicializamos el RAG
try:
    rag_chain = inicializar_rag()
    st.success("✅ Base de conocimiento cargada correctamente.")
except Exception as e:
    st.error(f"Error al cargar el documento: {e}")

# 2. Interfaz de Chat
pregunta_usuario = st.text_input("¿Qué te gustaría consultar hoy?", value="¿Cuáles son las normas de conducta y comunicación establecidas para los foros de la comunidad y canales de la plataforma?")

if st.button("Enviar Pregunta"):
    if pregunta_usuario:
        with st.spinner("Buscando respuesta..."):
            try:
                # Invocación segura pasando el input correctamente
                respuesta = rag_chain.invoke({"input": pregunta_usuario})
                st.markdown(f"### Respuesta:")
                st.write(respuesta.get("answer", str(respuesta)))
            except Exception as err:
                st.error(f"Ocurrió un error al procesar tu consulta: {err}")
    else:
        st.warning("Por favor escribe una pregunta.")
