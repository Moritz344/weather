import rich
import requests
import json
from rich.table import Table
from rich.panel import Panel
from rich.box import Box
from rich.console import Console

api_key = "FUCK"

lat = "49.2464496"
lon = "8.344604"

request_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
response = requests.get(request_url)




console = Console()
def handler(r):
    if response.status_code == 200:
        data = r.json()
        #print(data)
    else:
        print(response)


    wetter = data["weather"][0]["main"]   
    country = data["sys"]["country"]
    city = data["name"]
    desc = data["weather"][0]["description"]

    temp = data["main"]["temp"]
    temp_celsius = temp - 273.15
    temp_rounded = round(temp_celsius)

    
    if country == "DE":
        country = "Germany"

    if wetter == "Rain":
        wetter_icon = "\U0001F327"
    else:
        wetter_icon = "\U000026C1"

    city_icon = "\U0001F3D9"
    desc_icon = "\U0001F4C4"
    country_icon = "\U0001F30D"   
    def table(country,city,wetter,temp_rounded):
        content = f" {country_icon} {country}\n {city_icon}  {city}\n {wetter_icon}  {wetter}\n {desc_icon} {desc}\n \U0001F321  {temp_rounded}"
        panel = Panel(content,width=30)

        console.print(panel)

    table(country,city,wetter,temp_rounded)
handler(response)
