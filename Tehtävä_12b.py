import requests

kaupunki = input("Anna paikkakunta: ")

api_key = "aaa3edc1b3f51da71c696da4d2390849"

url = f"https://api.openweathermap.org/data/2.5/weather?q={kaupunki}&appid={api_key}"
response = requests.get(url)
data = response.json()

if response.status_code != 200:
    print(f"Virhe API:sta. Status code: {response.status_code}")
    print(data)
else:
    sailytila = data["weather"][0]["description"]
    lampotila_c = data["main"]["temp"] - 273.15
    print(f"Sää: {sailytila}")
    print(f"Lämpötila: {lampotila_c:.1f} °C")