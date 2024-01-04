import requests
import json

#returns a general forecast for every 12-hour period specified (maximum of 14 periods)
def forecaster(coordinates: list, periods: int) -> str:
    
    lat = coordinates[0]
    lon = coordinates[1]
  

    responseObject = requests.get(f"https://api.weather.gov/points/{lat},{lon}")

    link1 = responseObject.json()['properties']["forecast"]

    forecastData = requests.get(link1).json()['properties']['periods']

    index = 0
    generalForecasts = []

    while index < periods:
            
        detailedForecast = forecastData[index]['detailedForecast']

        generalForecasts.append(detailedForecast)
        index += 1
        
    forecast = (" ".join(generalForecasts))
    return forecast