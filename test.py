import downloadFunctions


dog = downloadFunctions.forecaster([38.99,-76.49], "forecast")
cat = downloadFunctions.forecaster([38.99,-76.49], "forecastHourly")


print(downloadFunctions.forecasterr(dog, 2, 'detailedForecast'))
print(cat)