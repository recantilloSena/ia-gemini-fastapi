# Proyecto básico de Uso de gemini-flash en un back end de python
- Setear la variable de ambiente GEMINI_API_KEY
- Se recomienda el uso de PYDANTIC para controlar las respuestas de la IA Generativa



1. python -m venv venv
2. .\venv\Scripts\activate
3. pip install fastapi "uvicorn[standard]" google-genai pydantic
4. $env:GEMINI_API_KEY="TU_CLAVE_API_AQUI"
5. uvicorn main:app --reload