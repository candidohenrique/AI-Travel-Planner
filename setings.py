import json

def defined_language():
	while True:
		print("Welcome! Plase select your langauge.")
		print("1 - Portuguese \n2 - English \n3 - Exit")

		try:
			escolha = int(input("Choice: "))
		except ValueError:
			print("The choice must be informed with an interim number")
			continue

		if escolha == 1:
			with open('language/pt.json', 'r', encoding='utf-8') as arquivo:
				idioma = json.load(arquivo)
			return idioma
		elif escolha == 2:
			with open('language/en.json', 'r', encoding='utf-8') as arquivo:
				idioma = json.load(arquivo)
			return idioma
		elif escolha == 3:
			break
		else:
			return 'Option invalidates, please try again.'