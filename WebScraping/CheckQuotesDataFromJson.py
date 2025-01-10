import json

quotes = {}

with open('WebScraping\\quotes.json', 'r') as file:
    quotes = json.load(file)

print(quotes['76']['Quote'])
print(quotes['40']['Quote'])
