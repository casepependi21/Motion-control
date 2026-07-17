import streamlit as st
import requests

# Konfigurasi Halaman
st.set_page_config(page_title="Toko Bang Mien", layout="centered")

st.title("🚀 Toko Bang Mien Video Generator")

# Mengambil API Key dari Secrets Streamlit Cloud
try:
    API_KEY = st.secrets["API_KEY"]
except KeyError:
    st.error("API_KEY belum diatur di Streamlit Secrets! Silakan atur melalui dashboard Settings > Secrets.")
    st.stop()

# Input UI
prompt = st.text_area("Masukkan Prompt Video", placeholder="Contoh: pemandangan gunung yang indah")
img_url = st.text_input("URL Gambar", placeholder="https://contoh.com/gambar.jpg")
vid_url = st.text_input("URL Video (Opsional)", placeholder="https://contoh.com/video.mp4")

# Logika Generate
if st.button("Generate Video"):
    if not prompt or not img_url:
        st.warning("Mohon isi Prompt dan URL Gambar!")
    else:
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
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
        
        with st.spinner('Sedang menghubungi server...'):
            try:
                response = requests.post("https://api.apimart.ai/v1/videos/generations", json=payload, headers=headers)
                data = response.json()
                
                if response.status_code == 200:
                    task_id = data["data"][0]["task_id"]
                    st.success(f"✅ Video berhasil diproses!")
                    st.info(f"Task ID Anda: {task_id}")
                    st.write("Simpan ID di atas untuk mengecek status video Anda nanti.")
                else:
                    st.error(f"Gagal membuat video: {data}")
            except Exception as e:
                st.error(f"Terjadi kesalahan koneksi: {e}")

# Footer
st.markdown("---")
st.caption("Toko Bang Mien - Generator Video Otomatis")
