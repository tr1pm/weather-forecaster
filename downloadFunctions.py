import requests
import json

def forecaster(coordinates: list) -> str:
    lat = coordinates[0]
    lon = coordinates[1]
    #naptown (38.99 lat, -76.49 lon)
    responseObject = requests.get(f"https://api.weather.gov/points/{lat},{lon}")

    link1 = responseObject.json()['properties']["forecast"]

    forecastData = requests.get(link1).json()['properties']['periods']

    index = 0
    generalForecasts = []

    while index != 2:
        current = forecastData[index]
            
        detailedForecast = current['detailedForecast']

        generalForecasts.append(detailedForecast)
        index += 1
        
    forecast = (" ".join(generalForecasts))
    return forecast