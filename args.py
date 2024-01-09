#used for downloadData
#Gotta have a set of cooridnates
coordinates = []
b1 = "forecast"
b2 = "forecastHourly"


#All usable arguments for sortData()
#They are arbitrarily named and should be renamed/organized
#All return individual values except for a13-a15 which return dicts
a1 = "name"
a2 = "startTime"
a3 = "endTime"
a4 = "isDaytime"
a5 = "temperature"
a6 = "temperatureUnit"
a7 = "temperatureTrend"
a8 = "windSpeed"
a9 = "windDirection"
a10 = "icon"
a11 = "shortForecast"
a12 = "detailedForecast"

a13 = "probabilityOfPrecipitation"
a14 = "dewpoint"
a15 = "relativeHumidity"

#These are for getRain(), getHumidity(), and getDewpoint()
c3 = "unitCode"
c4 = "value"