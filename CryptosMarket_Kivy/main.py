from kivy.app import App
from kivy.lang import Builder
import requests
Gui  = Builder.load_file("Window.kv")
class CryptoMarket (App):
    def build(self):
        self.icon = 'Icone.png'
        return Gui
    def on_start(self):
        self.root.ids["moeda1"].text = f"Dólar: R${self.pegar_cotação('USD')}"
        self.root.ids["moeda2"].text = f"Bitcoin: R${self.pegar_cotação('BTC')}"
        self.root.ids["moeda3"].text = f"Ethereum: R${self.pegar_cotação('ETH')}"
        self.root.ids["moeda4"].text = f"Litecoin: R${self.pegar_cotação('LTC')}"
    def pegar_cotação(self, moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        pedido_requisição = requests.get(link)
        dic_requisição = pedido_requisição.json()
        cotação = dic_requisição [f"{moeda}BRL"]["bid"]
        return cotação
CryptoMarket().run()