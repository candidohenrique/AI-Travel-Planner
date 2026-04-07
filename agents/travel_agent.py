from config import GEMINI_API_KEY
from google import genai

client = genai.Client(api_key=GEMINI_API_KEY)


def planejar_viagem(destino, duracao, idioma='en'):
    if idioma == 'pt':
        prompt = f"Planeje uma viagem para {destino} com duração de {duracao} dias. Inclua sugestões de atividades, restaurantes e pontos turísticos."
    else:
        prompt = f"Plan a trip to {destino} for {duracao} days. Include suggestions for activities, restaurants, and tourist attractions."
    response = client.models.generate_content(
        model="gemini-3-flash-preview", contents=prompt
    )
    return response.text