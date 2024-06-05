# A function that asks user for temp in Fahrenheit and converts it into Celsius
# @author Mark Kasule
# DATA 300
# 05/04/2024
def fahrToCelsius(tempFahrenheit):
    # Convert temp to float
    convertedTemp = (float(tempFahrenheit) - 32) / 1.8
    # round result to one decimal point
    return round(convertedTemp, 1)


# A function that asks classifies temperatures into four different classes(i.e., cold, slippery, comfortable, warm).
# @param tempCelsius temperature in Celsius
# #return reclassified value (i.e., 0, 1, 2, or 3)
def tempClassifier(tempCelsius):
    if tempCelsius < -2:
        return 0  # cold
    elif tempCelsius >= -2 and tempCelsius <= 2:
        return 1  # slippery
    elif tempCelsius > 2 and tempCelsius <= 15:
        return 2  # comfortable
    else:
        return 3  # warm


# Execute the Main function to convert Celsius to Fahrenheit, and Classifier temperatures
def Main():
    tempInput = float(input('Enter temperature in Fahrenheit: '))

    while str(type(tempInput)) != "<class 'float'>":
        # Catch errors in user input and re-convert temp to Celsius
        print("Error,", tempInput, "is not a valid temperature value [enter numbers only]")
        tempInput = input('Enter temperature in Fahrenheit: ')

    # Print Results
    print(tempInput, 'degrees Fahrenheit in Celsius is:', fahrToCelsius(tempInput))

    # Classifying temperatures
    match tempClassifier(fahrToCelsius(tempInput)):
        case 0:
            print("It's cold")
        case 1:
            print("It's slippery")
        case 2:
            print("It's comfortable")
        case 3:
            print("It's warm")


# Call/ initialize Main Function
if __name__ == "__main__":
    Main()
