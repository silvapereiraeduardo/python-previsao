import requests

def obter_previsao(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        clima = dados["current_weather"]
        print(f"🌡️ Temperatura: {clima['temperature']}°C")
        print(f"💨 Vento: {clima['windspeed']} km/h")
    else:
        print("❌ Erro ao obter previsão do tempo.")

if __name__ == "__main__":
    # Porto Alegre (latitude, longitude)
    obter_previsao(-30.0331, -51.23)
