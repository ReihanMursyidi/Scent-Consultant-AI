import os
import json
import google.generativeai as genai
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("API Key Google tidak ditemukan. Pastikan file .env sudah dibuat.")

genai.configure(api_key=api_key)

model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    system_instruction="""
    Kamu adalah seorang 'Master Perfumer' (Ahli Parfum) profesional dengan pengalaman 20 tahun. 
    Tugasmu adalah menganalisis profil pengguna dan memberikan rekomendasi parfum yang sangat spesifik.
    Analisis hubungan antara kepribadian, momen, cuaca/waktu, dan kesan yang ingin ditampilkan.
    Jelaskan dengan bahasa yang elegan, sedikit puitis namun mudah dimengerti, layaknya seorang konsultan butik parfum mewah.
    """
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserPreferences(BaseModel):
    gender: str
    personality: str
    occasion: str
    time: str
    impression: str

@app.post("/consult-gemini")
async def consult_gemini(prefs: UserPreferences):
    try:
        prompt = f"""
        User Profile:
        - Gender: {prefs.gender}
        - Kepribadian: {prefs.personality}
        - Momen Penggunaan: {prefs.occasion}
        - Waktu Penggunaan: {prefs.time}
        - Kesan/Image yang diinginkan: {prefs.impression}
        
        Berdasarkan profil di atas, berikan rekomendasi parfum.
        
        PENTING: Responmu HARUS dalam format JSON murni tanpa markdown (```json).
        Struktur JSON harus seperti ini:
        {{
            "analisis_singkat": "Kalimat pembuka yang menganalisis profil user...",
            "notes_rekomendasi": {{
                "top_notes": "...",
                "heart_notes": "...",
                "base_notes": "..."
            }},
            "rekomendasi_parfum": [
                {{
                    "nama": "Nama Brand & Varian (Contoh: Dior Sauvage Elixir)",
                    "deskripsi_wangi": "Penjelasan singkat wanginya..."
                }},
                 {{
                    "nama": "Opsi Alternatif (Contoh: Tom Ford Oud Wood)",
                    "deskripsi_wangi": "Penjelasan singkat wanginya..."
                }}
            ],
            "tips_penggunaan": "Tips cara pakai untuk situasi ini..."
        }}
        """

        # Generate Content
        response = model.generate_content(prompt)
        
        # Membersihkan respon jika Gemini tidak sengaja menyertakan backticks markdown
        cleaned_text = response.text.replace("```json", "").replace("```", "").strip()
        
        # Parsing string JSON menjadi Dictionary Python
        result_json = json.loads(cleaned_text)

        return result_json

    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Terjadi kesalahan pada AI Consultant.")

if __name__ == "__main__":
    import uvicorn
    @app.get("/")
    def read_root():
        return {"status": "Server Berjalan Aman!", "pesan": "Buka file index.html untuk mulai konsultasi."}
    uvicorn.run(app, host="127.0.0.1", port=8000)