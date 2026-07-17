import requests

# 1. Masukkan API Key Anda di sini
API_KEY = "sk-za7vEbfl0Ed9VpVTF4OJAfVKZGUIF7YRyHCyEBG60hCJsKDQ" 

def main():
    print("=== TOKO BANG MIEN CLI ===")
    prompt = input("Masukkan Prompt: ")
    img_url = input("Masukkan URL Gambar: ")
    vid_url = input("Masukkan URL Video: ")

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

    print("\nSedang mengirim data ke server...")
    try:
        response = requests.post("https://api.apimart.ai/v1/videos/generations", json=payload, headers=headers)
        data = response.json()
        
        if response.status_code == 200:
            task_id = data["data"][0]["task_id"]
            print(f"\n✅ BERHASIL!")
            print(f"Task ID: {task_id}")
            print("Video Anda sedang diproses.")
        else:
            print(f"\n❌ GAGAL: {data}")
    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main()

