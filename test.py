import downloadFunctions


dog = downloadFunctions.forecaster([38.99,-76.49], "forecast")
cat = downloadFunctions.forecaster([38.99,-76.49], "forecastHourly")


#print(downloadFunctions.forecasterr(dog, 2, 'detailedForecast'))

weatherdata = downloadFunctions.forecasterr(cat, 12, 'temperature')

times = downloadFunctions.forecasterr(cat, 12, 'startTime') 


stag = downloadFunctions.timeWriter2(times, weatherdata, "degrees F")

print(1)