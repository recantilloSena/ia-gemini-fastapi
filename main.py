from fastapi import FastAPI
from google import genai
from google.genai import types
from pydantic import BaseModel
import json

app = FastAPI()

# 1. Definimos la estructura de datos deseada con Pydantic
class Tip(BaseModel):
    tips: int
    detalle: str

@app.get("/chat/{tema}")
def chat_gemini(tema: str):
    client = genai.Client()
    
    response = client.models.generate_content(
        model="gemini-2.5-flash", # Asegúrate de usar un modelo válido actual
        contents=f"Eres un desarrollador de software y necesito que me des 3 tips para aprender el tema: {tema}",
        # 2. Obligamos al modelo a devolver un JSON basado en el esquema (Lista de Tips)
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=list[Tip],
            temperature=0.2, # Una temperatura baja ayuda a mantener la precisión del formato
        ),
    )
    
    # 3. response.text es un string en formato JSON. 
    # Lo parseamos con json.loads para que FastAPI lo devuelva como un JSON real (y no un string escapado)
    try:
        data = json.loads(response.text)
        return data
    except json.JSONDecodeError:
        return {"error": "El modelo no devolvió un JSON válido"}


