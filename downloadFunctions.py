import requests
import json
import time

#returns a big list of general forecast data for 12-hour long periods
def forecaster(coordinates: list, dataType: str) -> list:
    
    lat = coordinates[0]
    lon = coordinates[1]
  
    responseObject = requests.get(f"https://api.weather.gov/points/{lat},{lon}")

    link1 = responseObject.json()['properties'][dataType]

    forecastData = requests.get(link1).json()['properties']['periods']
    
    return forecastData

#Returns a specified type of weather data over a specified number of 12 hour periods, maximum 14
def forecasterr(forecastData: list, periods: int, weatherdataType: str) -> list:
    
    generalForecasts = []
    index = 0
    while index < periods:
            
        detailedForecast = forecastData[index][weatherdataType]

        generalForecasts.append(detailedForecast)
        index += 1
        
    return generalForecasts


def hourlyForecaster(forecastData: list, periods: int, weatherdataType: str) -> list:
    

    hour = time.localtime(time.time())[3]
    minutes = time.localtime(time.time())[4]
    
    
    
    hfcs = []
    index = 0
    for loop in range(periods):
        
        forecastData[index][weatherdataType]

        temperature = current['temperature']
        #shortForecast = current['shortForecast']
        precipitationChance = current["probabilityOfPrecipitation"]["value"]
        #windSpeed = current['windSpeed']
        #windDirection = current['windDirection']
        
        if (hour > 24):
            hour = 1
            
        if (hour > 12 ):
            hourly = (hour - 12)
            tempstring = f"{hourly:02d}:{minutes:02d} PM -- {temperature} Degrees -- {precipitationChance}% chance of rain"
        else:
            tempstring = f"{hour:02d}:{minutes:02d} AM -- {temperature} Degrees -- {precipitationChance}% chance of rain"
        hfcs.append(tempstring)
        hour += 1
        x += 1

    stringy2 = "\n".join(hfcs)

    return stringy2


def timewriter(forecasts: list) -> list:
    
    hour = time.localtime(time.time())[3]
    minutes = time.localtime(time.time())[4]

    hourlystuff = []


    index = 0
    while index < len(forecasts):
        
        if (hour > 24):
            hour = 1
            
        if (hour > 12 ):
            hourly = (hour - 12)
            tempstring = f"{hourly:02d}:{minutes:02d} PM -- {forecasts[index]} degrees"
        else:
            tempstring = f"{hour:02d}:{minutes:02d} AM -- {forecasts[index]} degrees"
        
        hourlystuff.append(tempstring)
        hour += 1
        index += 1
    return hourlystuff
    
