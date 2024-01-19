import requests
import json
import args


#downloads a large list of general forecast data for 12 or 1 hour long periods
def downloadData(coordinates: list, dataType: str) -> list:
    
    lat = coordinates[0]
    lon = coordinates[1]
  
    responseObject = requests.get(f"https://api.weather.gov/points/{lat},{lon}")

    webLink = responseObject.json()['properties'][dataType]

    forecastData = requests.get(webLink).json()['properties']['periods']
    
    return forecastData

#returns specified types of weather data over a specified number of 1 or 12 hour periods
def sortData(forecastData: list, periods: int, dataTypes: list) -> list:
    
    x = 0
    allTheForecasts = []
    while x < len(dataTypes):

        generalForecasts = []
        WeatherDataType = args.dataTypes[dataTypes[x]]
        index = 0
        while index < periods:
                
            detailedForecast = forecastData[index][WeatherDataType]

            generalForecasts.append(detailedForecast)
            index += 1
        
        allTheForecasts.append(generalForecasts)
        x += 1    
    return generalForecasts


def getRain(rainData: list, periods: int) -> list:

    rainForecasts = []
    index = 0 
    while index < periods:
        
        rainForecasts.append(rainData[index]['value'])
        index += 1
        
    return rainForecasts

def getHumidity(humidityData: list, periods: int) -> list:
    humidityForecasts = []
    index = 0 
    while index < periods:
        
        humidityForecasts.append(humidityData[index]['value'])
        index += 1
    return humidityForecasts


def getDewpoint(dewData: list, periods: int) -> list:
    dewForecasts = []
    index = 0 
    while index < periods:
        
        dewForecasts.append(dewData[index]['value'])
        index += 1
    return dewForecasts


#returns a list of forecast data associated with certain times.
def writeTime(times: list, dataType: list, units: str = "") -> list:

    writtenTimes = []
    index = 0
    while index < len(times):
        tempstring = f"{times[index][11:16]}: {dataType[index]} {units}"
        writtenTimes.append(tempstring)
        index += 1
    return writtenTimes

