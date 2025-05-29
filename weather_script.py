import requests

API_KEY = '6ad6ff8d9adb4f2e691e4d243c75382c'  # Replace with your OpenWeatherMap API key
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    return response.json()

if __name__ == '__main__':
    city = input("Enter city name: ")
    try:
        weather = get_weather(city)
        print(f"Weather in {city}: {weather['weather'][0]['description']}")
        print(f"Temperature: {weather['main']['temp']}°C")
        print(f"Humidity: {weather['main']['humidity']}%")
        print(f"Wind Speed: {weather['wind']['speed']} m/s")
    except requests.HTTPError as e:
        print(f"Failed to fetch weather data: {e}")