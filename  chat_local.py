import sys
import ollama

# ⚙️ CONFIGURACIÓN DEL MOTOR LOCAL
# Cambia "qwen2.5:7b" por "llama3.1" si prefieres el otro modelo que tienes en Docker
MODELO_LOCAL = "qwen2.5:7b"

# Aquí se irá guardando el historial para que la IA tenga memoria del chat
historial_conversacion = [
    {
        "role": "system",
        "content": "Eres un asistente de IA local, atento y conciso. Responde siempre en español de forma nativa.",
    }
]

print("====================================================")
print(f"🤖 Chatbot Local Iniciado (Modelo: {MODELO_LOCAL})")
print("Escribe tu mensaje y presiona Enter.")
print("Escribe 'salir' para terminar la conversación.")
print("====================================================\n")

while True:
    try:
        # 1. Leer el mensaje del usuario por teclado
        user_input = input("👤 Tú: ")

        # Condición para romper el bucle y cerrar el programa
        if user_input.lower() in ["salir", "exit", "quit"]:
            print("\n🤖 IA: ¡Hasta luego! Cerrando sesión local.")
            break

        # Si el usuario presiona enter vacío, ignoramos y continuamos
        if not user_input.strip():
            continue

        # 2. Agregar el mensaje del usuario al historial de memoria
        historial_conversacion.append({"role": "user", "content": user_input})

        print("🧠 Pensando...", end="", flush=True)

        # 3. Enviar TODO el historial acumulado al Docker de Ollama
        response = ollama.chat(model=MODELO_LOCAL, messages=historial_conversacion)

        # Limpiar el texto de "Pensando..." de la pantalla
        print("\r" + " " * 15 + "\r", end="", flush=True)

        # 4. Extraer la respuesta de la IA
        respuesta_ia = response["message"]["content"]

        # 5. Mostrar la respuesta en consola
        print(f"🤖 IA: {respuesta_ia}\n")

        # 6. Guardar la respuesta de la IA en el historial para que no sufra amnesia
        historial_conversacion.append({"role": "assistant", "content": respuesta_ia})

    except KeyboardInterrupt:
        # Permitir salir limpiamente presionando Ctrl + C
        print("\n\n🤖 IA: Conexión interrumpida por el teclado. ¡Adiós!")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error de conexión con Docker: ¿El contenedor está encendido?")
        print(f"Detalle técnico: {e}\n")
        break
