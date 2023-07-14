import requests
import tkinter as tk
from tkinter import messagebox

class Clima:
    
    def __init__(self, ciudad, api_key):
        self.ciudad = ciudad
        self.api_key = api_key

    def obtener_clima(self):
        # Construye la URL para la API del clima utilizando la ciudad y la clave de API
        url = f"http://api.openweathermap.org/data/2.5/weather?q={self.ciudad}&appid={self.api_key}"
        # Realiza una solicitud GET a la URL y obtiene la respuesta en formato JSON
        resp = requests.get(url)
        respDict = resp.json()
      
        if respDict["cod"] == 200:
            # Extrae la descripción del clima, temperatura y humedad del diccionario de respuesta
            descripcion = respDict["weather"][0]["description"] #clima actual
            temp = round(respDict["main"]["temp"] - 273)  # redondea la temperatura
            humedad = respDict["main"]["humidity"]
            # Muestra el resultado de la descripcion, la temperatura y la humedad 
            resultado = f"Clima en {self.ciudad}: {descripcion}\nTemperatura: {temp}°C\nHumedad: {humedad}%"
            return resultado
        else:
            return "No se detectó el clima en esta ciudad." 

def buscar():
    # Obtiene la ciudad ingresada en la entrada de texto
    ciudad = entry.get()
    # Crea una instancia de la clase Clima y llama al método obtener_clima()
    api = Clima(ciudad, api_key)
    resultado = api.obtener_clima()
    # Muestra una ventana emergente con la información del clima
    messagebox.showinfo("Resultados", resultado)

vent = tk.Tk() 
vent.title("Clima Grapity")
vent.geometry("300x200")

# Etiqueta para mostrar "Ciudad:"
label_ciudad = tk.Label(vent, text="Ciudad:")
label_ciudad.pack()

# Entrada de texto para ingresar la ciudad
entry = tk.Entry(vent)
entry.pack()

# Botón para buscar el clima
boton = tk.Button(vent, text="Buscar", command=buscar)
boton.pack()

api_key = "6da6abb09cfaab04706972174c0d3c3d"

vent.mainloop()
