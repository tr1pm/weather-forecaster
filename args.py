#used for downloadData
#Gotta have a set of cooridnates
coordinates = []

forecastTypes = [
    "forecast",
    "forecastHourly"
]


#All usable arguments for sortData()
dataTypes = [
    "name",
    "startTime",
    "endTime",
    "isDaytime",
    "temperature",
    "temperatureUnit",
    "temperatureTrend",
    "windSpeed",
    "windDirection",
    "icon",
    "shortForecast",
    "detailedForecast"
    "probabilityOfPrecipitation",
    "dewpoint",
    "relativeHumidity",
]

#These are for getRain(), getHumidity(), and getDewpoint()
c3 = "unitCode"
c4 = "value"