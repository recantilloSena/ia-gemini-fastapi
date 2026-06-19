from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Estoy en Colombia, Estudio en el SENA. Que prpgrama es el mejor si quiero ganar dinero.?",
)

print(response.text)