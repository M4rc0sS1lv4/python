import json
import requests
from bs4 import BeautifulSoup
import time


while True:
    page = requests.get("https://www.worldometers.info/coronavirus/country/brazil/")
    soup = BeautifulSoup(page.text, 'html.parser')

    container = soup.findAll("div", {"class": "maincounter-number"})
    casos = container[0].text.strip()
    mortes = container[1].text.strip()
    recuperados = container[2].text.strip()

    brasil = ("Total de casos no Brasil 🇧🇷: \n" + \
                  "Casos confirmados: " + casos + "\n" + \
                  "Óbitos: " + mortes + "\n" \
                  "Recuperações: " + recuperados + "\n""\n")

    page = requests.get("https://www.worldometers.info/coronavirus")
    soup = BeautifulSoup(page.text, 'html.parser')

    container = soup.findAll("div", {"class": "maincounter-number"})
    casos = container[0].text.strip()
    mortes = container[1].text.strip()
    recuperados = container[2].text.strip()

    mundo = ("Total de casos no Mundo 🌎: \n" + \
                  "Casos confirmados: " + casos + "\n" + \
                  "Óbitos: " + mortes + "\n" \
                  "Recuperações: " + recuperados + "\n""\n")

    hashtags = ("#covid19 #stayhome #covid #vacina")

    print(brasil)
    print(mundo)

    url = "https://hooks.zapier.com/hooks/catch/9372019/ox6dgp0/"
    data = {'value1': brasil, 'value2': mundo, 'value3:': hashtags}
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(url, data=json.dumps(data), headers=headers)

    print(r.text)
    print("dormindo por 60 minutos")
    time.sleep(3600)