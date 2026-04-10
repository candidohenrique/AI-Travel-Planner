from config import GEMINI_API_KEY
from google import genai
client = genai.Client(api_key=GEMINI_API_KEY)


def plan_trip(destination, duration, idioma='pt'):
    if idioma == 'pt':
        prompt = f"Planeje uma viagem para {destination} com duração de {duration} dias. Inclua sugestões de atividades, restaurantes e pontos turísticos."
    else:
        prompt = f"Plan a trip to {destination} for {duration} days. Include suggestions for activities, restaurants, and tourist attractions."
    response = client.models.generate_content(
        model="gemini-3-flash-preview", contents=prompt
    )
    return response.text