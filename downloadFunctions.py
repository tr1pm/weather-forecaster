import requests
import json

#downloads a large list of general forecast data for 12 or 1 hour long periods
def downloadData(coordinates: list, dataType: str) -> list:
    
    lat = coordinates[0]
    lon = coordinates[1]
  
    responseObject = requests.get(f"https://api.weather.gov/points/{lat},{lon}")

    webLink = responseObject.json()['properties'][dataType]

    forecastData = requests.get(webLink).json()['properties']['periods']
    
    return forecastData

#returns a specified type of weather data over a specified number of 1 or 12 hour periods
def sortData(forecastData: list, periods: int, weatherdataType: str) -> list:
    
    generalForecasts = []
    index = 0
    while index < periods:
            
        detailedForecast = forecastData[index][weatherdataType]

        generalForecasts.append(detailedForecast)
        index += 1
        
    return generalForecasts


def getRain(rainData: list, periods: int) -> list:

    rainForecasts = []
    index = 0 
    while index < periods:
        
        rainForecasts.append(rainData[index]['value'])
        index += 1
    return rainForecasts

#returns a list of forecast data associated with certain times.
def writeTime(times: list, dataType: list, units: str = "") -> list:

    writtenTimes = []
    index = 0
    while index < len(times):
        tempstring = f"{times[index][11:16]}: {dataType[index]} {units}"
        writtenTimes.append(tempstring)
        index += 1
    return writtenTimes

