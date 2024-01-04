import downloadFunctions


dog = downloadFunctions.forecaster([38.99,-76.49], "forecast")
cat = downloadFunctions.forecaster([38.99,-76.49], "forecastHourly")


#print(downloadFunctions.forecasterr(dog, 2, 'detailedForecast'))

weatherdata = downloadFunctions.forecasterr(cat, 12, 'temperature')

frog = downloadFunctions.timewriter(weatherdata)


print(frog)

print(1)