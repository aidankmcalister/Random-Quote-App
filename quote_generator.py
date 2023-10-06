import json
import random


def get_random_quote():
    with open('quotes.json', 'r') as file:
        quotes = json.load(file)

    selected_quote = random.choice(quotes)

    quote_text = selected_quote["quote"]

    print(quote_text)
    return quote_text


get_random_quote()
