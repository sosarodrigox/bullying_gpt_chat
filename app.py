import streamlit as st
import streamlit.components.v1 as components

# Configuración de la página
st.set_page_config(page_title="Mi GPT Embebido", layout="wide")

# Título de la aplicación
st.title("Mi GPT Embebido en Streamlit")

# Instrucciones
st.write("Interactúa con tu GPT personalizado aquí:")

# URL del GPT compartido en la tienda de GPTs de OpenAI
gpt_url = (
    "https://chat.openai.com/c/gpt-3.5-turbo"  # Reemplaza esto con la URL de tu GPT
)

# HTML para el iframe
iframe_html = f"""
<iframe src="{gpt_url}" width="100%" height="600px" style="border:none;"></iframe>
"""

# Embeber el iframe en la aplicación Streamlit
components.html(iframe_html, height=600)

# Información adicional
st.write("Utiliza el chat embebido para interactuar con el GPT.")
