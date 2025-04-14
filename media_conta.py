import streamlit as st
import pytesseract
from PIL import Image
import re

# Caminho do Tesseract instalado no seu PC
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\skate\AppData\Local\Programs\Tesseract-OCR"  # Altere se necessário

st.title("Leitor de Conta de Energia")

uploaded_image = st.file_uploader("Envie a imagem da conta (parte do gráfico de consumo)", type=["jpg", "png", "jpeg"])

if uploaded_image:
    image = Image.open(uploaded_image)
    st.image(image, caption="Imagem enviada", use_column_width=True)

    st.subheader("Texto reconhecido (bruto):")
    text = pytesseract.image_to_string(image)
    st.text(text)

    # Extraindo apenas os números do texto
    numeros = re.findall(r'\d{2,4}', text)
    numeros = [int(n) for n in numeros]

    st.subheader("Números identificados:")
    st.write(numeros)

    if len(numeros) >= 12:
        ultimos_12 = numeros[-12:]
        media = sum(ultimos_12) / 12
        st.success(f"Média de consumo mensal: {media:.2f} kWh")
    else:
        st.warning("Menos de 12 números encontrados. Envie uma imagem mais nítida da conta.")