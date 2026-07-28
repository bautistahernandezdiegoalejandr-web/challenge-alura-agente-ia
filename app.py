import streamlit as st
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# Configurar API Key de forma segura desde los secretos de Streamlit
if "GOOGLE_API_KEY" in st.secrets:
    os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]

# Configuración de la página en Streamlit
st.set_page_config(page_title="Agente IA - Atenea Online", page_icon="🤖")
st.title("🤖 Asistente Virtual Corporativo (Atenea Online)")
st.write("Pregúntame cualquier duda sobre las normativas y documentos de la empresa.")

# 1. Cargar y procesar el PDF (Renombramos la función para limpiar la caché de Streamlit)
@st.cache_resource
def cargar_base_conocimiento():
    pdf_path = "documento_empresa.pdf"
    loader = PyPDFLoader(pdf_path)
    documentos = loader.load()
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    documentos_procesados = text_splitter.split_documents(documentos)
    
    # Modelo de embeddings oficial y actualizado
    embeddings = GoogleGenerativeAIEmbeddings(model="text-embedding-004")
    vector_store = FAISS.from_documents(documentos_procesados, embeddings)
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})
    
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.3)
    
    template = (
        "Eres un asistente virtual corporativo útil y amable para Atenea Online. "
        "Usa los siguientes fragmentos de contexto recuperado para responder a la pregunta. "
        "Si no sabes la respuesta basada en el contexto, di que no tienes esa información.\n\n"
        "Contexto:\n{context}\n\n"
        "Pregunta: {input}"
    )
    prompt = ChatPromptTemplate.from_template(template)
    
    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)
    
    rag_chain = (
        {"context": retriever | format_docs, "input": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    return rag_chain

# Inicializamos el RAG con la nueva función
try:
    rag_chain = cargar_base_conocimiento()
    st.success("✅ Base de conocimiento cargada correctamente.")
except Exception as e:
    st.error(f"Error al cargar el documento: {e}")
    rag_chain = None

# 2. Interfaz de Chat
pregunta_usuario = st.text_input("¿Qué te gustaría consultar hoy?", value="¿Cuáles son las normas de conducta y comunicación establecidas para los foros de la comunidad y canales de la plataforma?")

if st.button("Enviar Pregunta"):
    if pregunta_usuario:
        if rag_chain is not None:
            with st.spinner("Buscando respuesta..."):
                try:
                    respuesta = rag_chain.invoke(pregunta_usuario)
                    st.markdown("### Respuesta:")
                    st.write(respuesta)
                except Exception as err:
                    st.error(f"Ocurrió un error al procesar tu consulta: {err}")
        else:
            st.error("La base de conocimiento no está inicializada debido al error anterior.")
    else:
        st.warning("Por favor escribe una pregunta.")
