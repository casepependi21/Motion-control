import streamlit as st
import requests

st.set_page_config(page_title="Toko Bang Mien - Dashboard Pro", layout="centered")

# CSS Styling untuk tampilan Premium
st.markdown("""
    <style>
    .stApp { background-color: #f4f7f6; }
    div[data-testid="stForm"] { border: 1px solid #dcdcdc; padding: 20px; border-radius: 10px; background-color: white; }
    </style>
""", unsafe_allow_html=True)

st.title("🚀 Motion Control Dashboard")

# Mengambil API Key
try:
    API_KEY = st.secrets["API_KEY"]
except:
    st.error("API Key belum diset di Secrets!")
    st.stop()

# Form Input
with st.form("apimart_form"):
    st.subheader("Input Configuration")
    
    col1, col2 = st.columns(2)
    with col1:
        model = st.selectbox("Model", ["kling-v2-6-motion-control"])
        orientasi = st.selectbox("Orientasi Karakter", ["image", "video"])
        suara_asli = st.selectbox("Pertahankan Suara Asli", ["yes", "no"])
    
    with col2:
        mode = st.selectbox("Mode", ["std", "pro"])
        watermark = st.checkbox("Watermark", value=True)
    
    prompt = st.text_area("Prompt", placeholder="Strange Things")
    img_url = st.text_input("Gambar Referensi (URL)")
    vid_url = st.text_input("Video Referensi (URL)")
    
    submitted = st.form_submit_button("Run")

# Logika Proses
if submitted:
    if not prompt or not img_url:
        st.warning("Mohon isi Prompt dan Gambar Referensi!")
    else:
        headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
        payload = {
            "model": model,
            "prompt": prompt,
            "image_url": img_url,
            "video_url": vid_url if vid_url else None,
            "mode": mode,
            "character_orientation": orientasi,
            "keep_original_sound": suara_asli,
            "watermark_info": {"enabled": watermark}
        }
        
        with st.spinner('Menjalankan proses...'):
            try:
                res = requests.post("https://api.apimart.ai/v1/videos/generations", json=payload, headers=headers)
                if res.status_code == 200:
                    st.success("Berhasil! Video sedang diproses.")
                    st.json(res.json())
                else:
                    st.error(f"Gagal: {res.json()}")
            except Exception as e:
                st.error(f"Error: {e}")
