import requests
import json

#returns a big list of general forecast data for 12-hour long periods
def forecaster(coordinates: list) -> list:
    
    lat = coordinates[0]
    lon = coordinates[1]
  
    responseObject = requests.get(f"https://api.weather.gov/points/{lat},{lon}")

    link1 = responseObject.json()['properties']["forecast"]

    forecastData = requests.get(link1).json()['properties']['periods']
    
    return forecastData


def hourlyforecaster(coordinates: list) -> list:

    lat = coordinates[0]
    lon = coordinates[1]
 
    responseObject = requests.get(f"https://api.weather.gov/points/{lat},{lon}")

    link2 = responseObject.json()['properties']["forecastHourly"]

    hourlyforecastData = requests.get(link2).json()['properties']['periods']

    return hourlyforecastData


#Returns a specified type of weather data over a specified number of 12 hour periods, maximum 14
def forecasterr(forecastData: list, periods: int, weatherdataType: str) -> list:
    
    generalForecasts = []
    index = 0
    while index < periods:
            
        detailedForecast = forecastData[index][weatherdataType]

        generalForecasts.append(detailedForecast)
        index += 1
        
    return generalForecasts