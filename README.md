# 🤖 Desafío Alura Agente - ONE IA FOR TECH

Agente de Inteligencia Artificial conversacional basado en la arquitectura **RAG (Retrieval-Augmented Generation)**, diseñado para actuar como una base de conocimiento corporativa centralizada para los colaboradores de **Atenea Online**.

---

## 🏗️ 1. Descripción de la Arquitectura Montada
El sistema procesa documentos corporativos en formato PDF y permite consultar su contenido mediante lenguaje natural utilizando la siguiente estructura:
1. **Carga y Extracción:** Utiliza `PyPDF` para leer el contenido del documento corporativo (`documento_empresa.pdf`).
2. **Segmentación (Chunking):** Se emplea `RecursiveCharacterTextSplitter` para dividir el texto en fragmentos (*chunks*) manejables de 1000 caracteres con un solapamiento de 200 caracteres.
3. **Indexación Vectorial:** Los fragmentos se transforman en vectores numéricos mediante el modelo de embeddings de Google y se almacenan localmente en memoria con **FAISS**.
4. **Motor de Recuperación y Generación (LLM):** Al realizar una consulta, el sistema recupera los 3 fragmentos más relevantes y se los suministra como contexto estricto a **Google Gemini (gemini-1.5-flash)** para generar la respuesta.
5. **Interfaz de Usuario:** Desarrollada con **Streamlit** para ofrecer un chat web interactivo y amigable.

---

## 💡 2. Ejemplos de Preguntas y Respuestas

* **Pregunta:** ¿Cuáles son las reglas sobre conducta y comunicación en los foros?
  * **Respuesta del Agente:** No se tolera lenguaje ofensivo, discriminatorio o acoso. Está estrictamente prohibido usar los canales para promocionar productos de terceros o enlaces maliciosos.
* **Pregunta:** ¿Cuál es la política de entrega de proyectos?
  * **Respuesta del Agente:** Los proyectos deben entregarse dentro de los plazos establecidos en la plataforma. Las entregas fuera de fecha requieren justificación previa al tutor asignado.

---

## 🚀 3. Instrucciones para Correr el Proyecto Localmente

1. Clona este repositorio:
   ```bash
   git clone [https://github.com/TU_USUARIO/TU_REPOSITORIO.git](https://github.com/TU_USUARIO/TU_REPOSITORIO.git)

2. Instala las dependencias necesarias:
   pip install -r requirements.txt

3. Configura tu variable de entorno con la API Key de Google:
   export GOOGLE_API_KEY="tu_api_key_aqui"
   
4. Ejecuta la aplicación de Streamlit:
   streamlit run app.py
