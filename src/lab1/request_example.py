import requests as r

url = "https://ab3.army/"
response = r.get(url)

print(response.text)
