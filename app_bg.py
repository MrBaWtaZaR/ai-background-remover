import streamlit as st
from rembg import remove
from PIL import Image
import io

# --- Configuração da Página ---
st.set_page_config(layout="centered", page_title="AI Background Remover")

# --- Título ---
st.title("🤖 AI Background Remover")
st.markdown("Faça o upload de uma imagem e a IA removerá o fundo para você.")

# --- Seção de Upload ---
uploaded_file = st.file_uploader("Escolha uma imagem...", type=["png", "jpg", "jpeg", "webp"])

if uploaded_file is not None:
    # 1. Carregar a imagem
    input_image = Image.open(uploaded_file)
    
    st.image(input_image, caption="Sua imagem original", use_container_width=True)
    
    # 2. Processar a imagem (Remover o fundo)
    with st.spinner("🤖 A IA está trabalhando... Removendo o fundo..."):
        output_image = remove(input_image)
    
    st.image(output_image, caption="Imagem com fundo removido", use_container_width=True)

    # 3. Preparar a imagem para Download
    buf = io.BytesIO()
    output_image.save(buf, format="PNG")
    byte_im = buf.getvalue()

    # 4. Criar o botão de Download
    st.download_button(
        label="Download Imagem (Fundo Transparente)",
        data=byte_im,
        file_name=f"{uploaded_file.name.split('.')[0]}_sem_fundo.png",
        mime="image/png"
    )

else:
    st.info("Por favor, faça o upload de uma imagem (JPG, PNG, WEBP).")

# --- NOSSA NOVA PARTE: O RODAPÉ ---
st.markdown("---")
st.caption("Feito com ❤️ por **Victor William** para o Portfólio.")