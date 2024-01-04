import downloadFunctions


dog = downloadFunctions.forecaster([38.99,-76.49], "forecast")
weatherdata2 = downloadFunctions.forecasterr(dog, 2, 'detailedForecast')
print(weatherdata2)
timess = downloadFunctions.forecasterr(dog, 2, "startTime")
moose = downloadFunctions.timeWriter(timess, weatherdata2)

cat = downloadFunctions.forecaster([38.99,-76.49], "forecastHourly")
weatherdata1 = downloadFunctions.forecasterr(cat, 12, 'temperature')
times = downloadFunctions.forecasterr(cat, 12, 'startTime') 
stag = downloadFunctions.timeWriter(times, weatherdata1, "degrees F")

print(1)