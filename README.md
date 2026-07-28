# 🤖 Desafío Alura Agente - ONE IA FOR TECH

Agente de Inteligencia Artificial conversacional basado en la arquitectura **RAG (Retrieval-Augmented Generation)**, diseñado para actuar como una base de conocimiento corporativa centralizada para los colaboradores de **Atenea Online**.

---

## 🏗️ 1. Descripción de la Arquitectura Montada

El sistema procesa documentos corporativos en formato PDF y permite realizar consultas en lenguaje natural mediante la siguiente estructura:

1. **Carga y Extracción:** Lee el contenido del documento corporativo (`documento_empresa.pdf`) mediante `PyPDFLoader`.
2. **Segmentación (Chunking):** Emplea `RecursiveCharacterTextSplitter` para dividir el texto en fragmentos (*chunks*) de 1000 caracteres con un solapamiento de 200 caracteres.
3. **Indexación Vectorial (Embeddings Locales):** Genera representaciones vectoriales de los fragmentos utilizando el modelo local `all-MiniLM-L6-v2` (`HuggingFaceEmbeddings` vía `sentence-transformers`) y los almacena en memoria con **FAISS**.
4. **Motor de Recuperación y Generación (LLM):** Recupera los fragmentos más relevantes y los suministra como contexto estricto al modelo **Llama 3.3 70B Versatile** a través de la infraestructura de **Groq** (`langchain-groq`).
5. **Interfaz de Usuario:** Desarrollada con **Streamlit** para ofrecer un chat web interactivo y rápido.

---

## 🛠️ 2. Tecnologías Utilizadas

* **Codigo:** Python
* **Framework de IA:** LangChain
* **Modelo de Lenguaje (LLM):** Meta Llama 3.3 70B (`llama-3.3-70b-versatile` vía Groq API)
* **Embeddings:** HuggingFace `sentence-transformers/all-MiniLM-L6-v2`
* **Base de Datos Vectorial:** FAISS
* **Interfaz / Hosting:** Streamlit & Streamlit Community Cloud

---

## 💡 3. Ejemplos de Preguntas y Respuestas

* **Pregunta:** ¿Cuáles son las normas de conducta y comunicación establecidas para los foros de la comunidad y canales de la plataforma?
* **Respuesta del Agente:** No se tolera el lenguaje ofensivo, discriminatorio o acoso. Está estrictamente prohibido usar los canales para promocionar productos de terceros, esquemas de negocios o enlaces maliciosos.

* **Pregunta:** ¿Cuál es la política de entrega de proyectos?
* **Respuesta del Agente:** Los proyectos deben entregarse dentro de los plazos establecidos en la plataforma. Las entregas fuera de fecha requieren una justificación previa dirigida al tutor asignado.

---

## 🚀 4. Instrucciones para Ejecutar el Proyecto Localmente

1. **Clona este repositorio:**
   ```bash
   git clone [https://github.com/bautistahernandezdiegoalejandr-web/challenge-alura-agente-ia.git](https://github.com/bautistahernandezdiegoalejandr-web/challenge-alura-agente-ia.git)
   cd challenge-alura-agente-ia

2. **Instala las dependencias necesarias:**
   pip install -r requirements.txt

3. **Configura tu variable de entorno:**
   Obtén una API Key gratuita en Groq Console y ejecútala en tu terminal:
   export GROQ_API_KEY="tu_groq_api_key_aqui"

4. **Ejecuta la aplicación de Streamlit:**
   streamlit run app.py

5. **Despliegue en Streamlit Community Cloud:**
   .Conecta este repositorio en Streamlit Share.
   .En la configuración avanzada (Advanced Settings > Secrets), agrega tu clave de Groq:
    GROQ_API_KEY = "tu_groq_api_key_aqui"
   .Guarda el cambio realizado.

6. **Haz clic en Deploy!.:**

## 🌐 5. Aplicación en Línea y Demostración

* **Enlace de la aplicación desplegada:** [Agente IA - Atenea Online](https://challenge-alura-agente-ia-4tcj6jzuwxm34eksgxcdtj.streamlit.app/)

### 📸 Capturas de Pantalla del Funcionamiento

<img width="1353" height="1078" alt="image" src="https://github.com/user-attachments/assets/b552c59b-2894-4169-8a23-c5b9bd848c8a" />

<img width="1353" height="1072" alt="image" src="https://github.com/user-attachments/assets/babd5f39-f765-4e19-87ad-af14f8fe73a7" />

<img width="1356" height="1075" alt="image" src="https://github.com/user-attachments/assets/73f28742-ced4-48ae-a0e3-42d1be5f9b90" />

<img width="1354" height="1073" alt="image" src="https://github.com/user-attachments/assets/a5d1d059-8d5a-4d8a-8c05-48c2927a454d" />




