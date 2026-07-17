import streamlit as st
import requests

# Konfigurasi Halaman (Premium Look)
st.set_page_config(page_title="Toko Bang Mien - Pro", layout="centered")

# Custom CSS untuk tampilan lebih elegan
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    .css-1r6slb0 { border: 1px solid #e0e0e0; border-radius: 10px; padding: 20px; }
    .stButton>button { width: 100%; border-radius: 5px; font-weight: bold; background-color: #007bff; color: white; }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1 style='text-align: center; color: #1f1f1f;'>🚀 Toko Bang Mien</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666;'>Generator Video AI Profesional</p>", unsafe_allow_html=True)

# Mengambil API Key dari Secrets
try:
    API_KEY = st.secrets["API_KEY"]
except KeyError:
    st.error("⚠️ API Key belum diatur di Secrets!")
    st.stop()

# Layout Utama dengan Border
with st.container(border=True):
    st.subheader("📝 Input Detail Video")
    
    prompt = st.text_area("Deskripsi Video", placeholder="Contoh: Pendaki di puncak gunung saat sunrise...")
    
    # Menggunakan columns agar terlihat rapi
    col1, col2 = st.columns(2)
    with col1:
        img_url = st.text_input("URL Gambar Referensi")
    with col2:
        vid_url = st.text_input("URL Video Referensi (Opsional)")

    # Tombol Aksi
    if st.button("✨ Generate Video Sekarang"):
        if not prompt or not img_url:
            st.warning("Mohon lengkapi Prompt dan URL Gambar!")
        else:
            headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
            payload = {
                "model": "kling-v2-6-motion-control",
                "prompt": prompt,
                "image_url": img_url,
                "video_url": vid_url,
                "keep_original_sound": "yes",
                "character_orientation": "image",
                "mode": "std",
                "watermark_info": {"enabled": False}
            }
            
            with st.spinner('Memproses video di server...'):
                try:
                    response = requests.post("https://api.apimart.ai/v1/videos/generations", json=payload, headers=headers)
                    data = response.json()
                    
                    if response.status_code == 200:
                        task_id = data["data"][0]["task_id"]
                        st.success("✅ Video berhasil dikirim!")
                        st.code(f"Task ID: {task_id}")
                    else:
                        st.error(f"Gagal: {data}")
                except Exception as e:
                    st.error(f"Terjadi kesalahan: {e}")

# Footer
st.markdown("---")
st.caption("Toko Bang Mien © 2026 | Dibuat dengan Streamlit")
