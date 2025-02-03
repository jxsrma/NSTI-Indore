import requests

url = "https://www.google.com/"
# url = "https://www.microsoft.com/en-in"
# url = "https://quotes.toscrape.com/"

response = requests.get(url)
print("Response: ", response)
print()
print()
print()
# print("Status: ", response.status_code)
print()
print()
print()
# print("Headers: ", response.headers)
print()
print()
print()
print("Content: ", response.text)
# print("Content: ", response.content)
print()
print()
print()
print("Cookies: ", response.cookies.keys())
