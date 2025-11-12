import streamlit as st
from rembg import remove
from PIL import Image
import io

# --- Configuração da Página ---
st.set_page_config(layout="centered", page_title="Estúdio de Imagem IA")

# --- Título ---
st.title("🤖 Estúdio de Imagem IA")
st.markdown("Use as abas abaixo para escolher sua ferramenta.")

# --- Criação das Abas ---
tab1, tab2 = st.tabs(["1. Remover Fundo", "2. Comprimir Imagem"])

# --- CÓDIGO DA ABA 1: REMOVER FUNDO ---
with tab1:
    st.header("Remova o fundo de qualquer imagem")
    
    bg_uploader = st.file_uploader("Escolha uma imagem para remover o fundo...", type=["png", "jpg", "jpeg", "webp"], key="bg_remover")

    if bg_uploader is not None:
        input_image = Image.open(bg_uploader)
        st.image(input_image, caption="Sua imagem original", use_container_width=True)
        
        with st.spinner("🤖 A IA está trabalhando... Removendo o fundo..."):
            output_image = remove(input_image)
        
        st.image(output_image, caption="Imagem com fundo removido", use_container_width=True)

        buf = io.BytesIO()
        output_image.save(buf, format="PNG")
        byte_im = buf.getvalue()

        st.download_button(
            label="Download Imagem (Fundo Transparente)",
            data=byte_im,
            file_name=f"{bg_uploader.name.split('.')[0]}_sem_fundo.png",
            mime="image/png"
        )
    else:
        st.info("Por favor, faça o upload de uma imagem (JPG, PNG, WEBP).")

# --- CÓDIGO DA ABA 2: COMPRIMIR IMAGEM ---
with tab2:
    st.header("Reduza o tamanho de imagens sem perder (quase) nada")
    
    compress_uploader = st.file_uploader("Escolha uma imagem para comprimir...", type=["png", "jpg", "jpeg", "webp"], key="compressor")

    if compress_uploader is not None:
        img = Image.open(compress_uploader)
        
        st.image(img, caption="Sua imagem original", use_container_width=True)
        
        st.subheader("Opções de Compressão")
        quality_slider = st.slider("Qualidade (1 = Baixa, 100 = Alta)", 1, 100, 85)
        
        original_size = compress_uploader.size
        st.write(f"Tamanho original: **{original_size / 1024:.2f} KB**")
        
        if st.button("Comprimir Imagem"):
            with st.spinner("Compressão em andamento..."):
                buf = io.BytesIO()

                if img.mode != "RGB":
                    img = img.convert("RGB")
                    
                img.save(buf, format="JPEG", quality=quality_slider)
                
                byte_im = buf.getvalue()
                new_size = len(byte_im)
                
                st.success(f"Tamanho comprimido: **{new_size / 1024:.2f} KB**")
                
                st.image(byte_im, caption="Imagem comprimida", use_container_width=True)
                
                st.download_button(
                    label="Download Imagem Comprimida",
                    data=byte_im,
                    file_name=f"{compress_uploader.name.split('.')[0]}_comprimido.jpg",
                    mime="image/jpeg"
                )

    else:
        st.info("Por favor, faça o upload de uma imagem para reduzir o tamanho.")

# --- RODAPÉ ATUALIZADO ---
st.markdown("---")
# Lembre-se de trocar "SEU-USUARIO-AQUI" pelo seu usuário real do LinkedIn!
st.caption("Feito com ❤️ por **Victor William** | [GitHub](https://github.com/MrBaWtaZaR) | [LinkedIn](https://www.linkedin.com/in/victor-william-674624182/)")