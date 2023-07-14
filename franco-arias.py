import requests

class Clima:
    
    def __init__(self, ciudad, api_key):
        self.ciudad = ciudad
        self.api_key = api_key

    def obtener_clima(self):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={self.ciudad}&appid={self.api_key}"
        resp = requests.get(url)
        respDict = resp.json()
      
        if respDict["cod"]== 200:
            descripcion = respDict["weather"][0]["description"] #clima actual
            temp = round(respDict["main"]["temp"] -1)  # redondea la temperatura
            humedad = respDict["main"]["humidity"]
            resultado = f"Clima en {self.ciudad}: {descripcion}\nTemperatura: {temp - 273}°C\nHumedad: {humedad}%"
            print(resultado)
        else:
            print("No se detectó el clima en esta ciudad.") 

ciudad = input("Ingrese Ciudad: ")
api_key = "6da6abb09cfaab04706972174c0d3c3d"
api = Clima(ciudad, api_key)
api.obtener_clima()