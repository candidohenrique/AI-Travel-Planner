from agents.travel_agent import plan_trip
from settings import defined_language
import os


messages = defined_language()
idioma = messages['language_selected']
os.system('cls' if os.name == 'nt' else 'clear')

print(messages['welcome'])

while True:
    print(messages['menu']['title'])
    print(messages['menu']['options'])
    
    try:
        choise = int(input(messages['menu']['choice']))
    except ValueError:
        print(messages['value_error'])
        continue

    if choise == 1:
        destination = input(messages['destination'])
        duration = int(input(messages['duration']))

        plan_trip = plan_trip(destination, duration, language)
        print(plan_trip)

    elif choise == 2:
        break
    else:
        print(messages['invalid_option'])