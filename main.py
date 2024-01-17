import args
import downloadFunctions


print("Welcome to weather forecaster.")
print()

print("Before we start, please enter a set of coordinates: ")

float(input("x coordinates: "))
float(input("y coordinates: "))
print()

print("Next, would you like forecasts over a 1 hour period or a 12 hour period?")
print("Hour long periods, enter 0")
print("12 hour long periods, enter 1")


int(input("enter here: "))
print()


print("here is all of the avaliable data.")
i = 0
while i < len(args.dataTypes):
    print(f"{i} : {args.dataTypes[i]}")
    i += 1
print()
print("Make as many selections as you want by entering a number and hitting enter. A blank entry indicates you are done.")

#Working loop for entering the different types of desired forecast data. Needs work
DataTypeList = []
isloopActive = True
while isloopActive == True:
    x = input("Enter a number = ")

    if x == "":
        break
    
    if x.isdigit():
        x = int(x)
        
        if 0 <= x <= 13:
            DataTypeList.append(x)
        else:
            print("Please make a valid entry")
    else:
        print("Please make a valid entry")