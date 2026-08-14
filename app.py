import streamlit as st
import ollama

# 🎨 CONFIGURACIÓN DE LA PÁGINA WEB
st.set_page_config(page_title="Mi IA Local", page_icon="🤖", layout="centered")

st.title("🤖 Mi Asistente de IA Local")
st.write("Interactúa con los modelos corriendo en tu Docker de Ollama de forma privada.")

# 🎛️ BARRA LATERAL: SELECCIÓN DE MODELO
st.sidebar.title("Configuración")
modelo_seleccionado = st.sidebar.selectbox(
    "Elige el cerebro de la IA:",
    ["qwen2.5:7b", "llama3.1"]
)

st.sidebar.markdown("---")
st.sidebar.info("💡 Desarrollado localmente con Python, Streamlit y Docker.")

# 🧠 INICIALIZAR EL HISTORIAL EN LA MEMORIA DE STREAMLIT
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system", 
            "content": "Eres un asistente de IA local atento y experto. Responde siempre en español de forma nativa."
        }
    ]

# 💬 MOSTRAR LOS MENSAJES ANTERIORES EN LA INTERFAZ
# Ignoramos el mensaje de sistema para que no ensucie la vista del usuario
for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

# 👤 ENTRADA DE TEXTO DEL USUARIO
if prompt := st.chat_input("Escribe tu mensaje aquí..."):
    
    # 1. Mostrar inmediatamente el mensaje del usuario en la pantalla
    with st.chat_message("user"):
        st.write(prompt)
    
    # 2. Guardarlo en el historial de la sesión
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 3. Llamar a Ollama de forma visual usando un contenedor de carga (spinner)
       # 3. Llamar a Ollama en modo Streaming (tiempo real)
    with st.chat_message("assistant"):
        try:
            # Activamos el parámetro stream=True en la petición de Ollama
            response_stream = ollama.chat(
                model=modelo_seleccionado, 
                messages=st.session_state.messages,
                stream=True
            )
            
            # Función generadora interna para que Streamlit vaya atrapando palabra por palabra
            def generar_palabras():
                for chunk in response_stream:
                    yield chunk['message']['content']
            
            # Mostramos la respuesta con efecto máquina de escribir en tiempo real
            respuesta_ia = st.write_stream(generar_palabras())
            
            # 4. Guardar la respuesta final de la IA en el historial de la sesión
            st.session_state.messages.append({"role": "assistant", "content": respuesta_ia})
            
        except Exception as e:
            st.error(f"❌ Error al conectar con Docker: {e}")
