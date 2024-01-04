import requests
import json

#returns a big list of general forecast data for 12 or 1 hour long periods
def forecaster(coordinates: list, dataType: str) -> list:
    
    lat = coordinates[0]
    lon = coordinates[1]
  
    responseObject = requests.get(f"https://api.weather.gov/points/{lat},{lon}")

    webLink = responseObject.json()['properties'][dataType]

    forecastData = requests.get(webLink).json()['properties']['periods']
    
    return forecastData

#Returns a specified type of weather data over a specified number of 1 or 12 hour periods
def forecasterr(forecastData: list, periods: int, weatherdataType: str) -> list:
    
    generalForecasts = []
    index = 0
    while index < periods:
            
        detailedForecast = forecastData[index][weatherdataType]

        generalForecasts.append(detailedForecast)
        index += 1
        
    return generalForecasts


#returns a 
def timeWriter (times: list, data1: list, units: str = ""):

    writtenTimes = []
    index = 0
    while index < len(times):
        tempstring = f"{times[index][11:16]}: {data1[index]} {units}"
        writtenTimes.append(tempstring)
        index += 1
    return writtenTimes

