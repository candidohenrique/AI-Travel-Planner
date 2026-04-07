from agents.travel_agent import planejar_viagem
from settings import defined_language
import os


mensagem = defined_language()
idioma = mensagem['language_selected']
os.system('cls')    


print(mensagem['welcome'])
while True:
    print(mensagem['menu']['title'])
    print(mensagem['menu']['options'])
    try:
        escolha = int(input(mensagem['menu']['choice']))
    except ValueError:
        print(mensagem['value_error'])
        continue

    if escolha == 1:
        destino = input(mensagem['destination'])
        duracao = int(input(mensagem['duration']))

        plano = planejar_viagem(destino, duracao, idioma)
        print(plano)
    elif escolha == 2:
        break
    else:
        print(mensagem['invalid_option'])