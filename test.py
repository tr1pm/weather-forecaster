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

elk = downloadFunctions.getRain(weatherdata1, 12)

print(1)