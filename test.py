import downloadFunctions
import main
import args

#Testing sort data with a list argument

moose = [0, 2, 1, 3]

stag = downloadFunctions.downloadData([38.9784, -76.4922],"forecastHourly")

elk = downloadFunctions.sortData(stag, 12, moose)



#Testing main
main.main()