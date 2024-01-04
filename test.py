import downloadFunctions

print(downloadFunctions.forecaster([38.99,-76.49]))

dog = downloadFunctions.forecaster([38.99,-76.49])
cat = downloadFunctions.hourlyforecaster([38.99,-76.49])


print(downloadFunctions.forecasterr(dog, 2, 'detailedForecast'))
