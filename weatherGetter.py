import requests
import json

def forecaster(coords: list) -> str:
    lat = coords[0]
    lon = coords[1]
    #naptown (38.99 lat, -76.49 lon)
    location = requests.get(f"https://api.weather.gov/points/{lat},{lon}")

    link1 = location.json()['properties']["forecast"]

    forecastData = requests.get(link1).json()['properties']['periods']

    hours = 0
    fcs = []

    while hours != 2:
        current = forecastData[hours]
            
        #temperature = current['temperature']
        #windSpeed = current['windSpeed']
        #windDirection = current['windDirection']
        detailedForecast = current['detailedForecast']

        fcs.append(detailedForecast)
        hours += 1
        
    stringy = (" ".join(fcs))
    return stringy

def hourlyforecaster(coords: list) -> str:
    lat = coords[0]
    lon = coords[1]
    #naptown (38.99 lat, -76.49 lon)
    location = requests.get(f"https://api.weather.gov/points/{lat},{lon}")

    link2 = location.json()['properties']["forecastHourly"]
    #I like the way the data flows from requests --> JSON --> Iterating
    hourlyforecastData = requests.get(link2).json()['properties']['periods']

    import time
    hour = time.localtime(time.time())[3]
    minutes = time.localtime(time.time())[4]
    x = 0
    hfcs = []

    #The loop and writing is better but i totally forgot how to read
    #the api data. It is close tho. very close
    for loop in range(12):
        current = hourlyforecastData[x]
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
    
    





