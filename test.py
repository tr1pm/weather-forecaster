import downloadFunctions


dog = downloadFunctions.downloadData([38.99,-76.49], "forecast")
weatherdata2 = downloadFunctions.sortData(dog, 2, 'detailedForecast')
print(weatherdata2)
timess = downloadFunctions.sortData(dog, 2, "startTime")
moose = downloadFunctions.writeTime(timess, weatherdata2)

cat = downloadFunctions.downloadData([38.99,-76.49], "forecastHourly")
weatherdata1 = downloadFunctions.sortData(cat, 12, 'probabilityOfPrecipitation')
times = downloadFunctions.sortData(cat, 12, 'startTime') 
stag = downloadFunctions.writeTime(times, weatherdata1, "degrees F")

weatherdata3 = downloadFunctions.sortData(cat, 12, 'dewpoint')
weatherdata4 = downloadFunctions.sortData(cat, 12, 'relativeHumidity')

elk = downloadFunctions.getRain(weatherdata1, 12)
clam = downloadFunctions.getDewpoint(weatherdata3, 12)
toucan = downloadFunctions.getHumidity(weatherdata4, 12)

print(1)
