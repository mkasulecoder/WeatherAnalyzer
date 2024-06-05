from functions import tempClassifier, fahrToCelsius

# -*- coding: utf-8 -*-
"""temp_analyzer.py

"""
# Python libraries are not required for this Exercise, but if you do load any libraries, do so before the dataset
# This file should contain all your Python code, including functions


# tempData list has 336 integers in the list.  In later assignments we will load an external
# datafile (e.g. .txt or .csv), but as this dataset is not very large, we'll place the data directly in the Python code
# List of half-hourly temperature values (in degrees Fahrenheit) for one week
tempData = [19, 21, 21, 21, 23, 23, 23, 21, 19, 21, 19, 21, 23, 27, 27, 28, 30, 30, 32, 32, 32, 32, 34, 34,
            34, 36, 36, 36, 36, 36, 36, 34, 34, 34, 34, 34, 34, 32, 30, 30, 30, 28, 28, 27, 27, 27, 23, 23,
            21, 21, 21, 19, 19, 19, 18, 18, 21, 27, 28, 30, 32, 34, 36, 37, 37, 37, 39, 39, 39, 39, 39, 39,
            41, 41, 41, 41, 41, 39, 39, 37, 37, 36, 36, 34, 34, 32, 30, 30, 28, 27, 27, 25, 23, 23, 21, 21,
            19, 19, 19, 18, 18, 18, 21, 25, 27, 28, 34, 34, 41, 37, 37, 39, 39, 39, 39, 41, 41, 39, 39, 39,
            39, 39, 41, 39, 39, 39, 37, 36, 34, 32, 28, 28, 27, 25, 25, 25, 23, 23, 23, 23, 21, 21, 21, 21,
            19, 21, 19, 21, 21, 19, 21, 27, 28, 32, 36, 36, 37, 39, 39, 39, 39, 39, 41, 41, 41, 41, 41, 41,
            41, 41, 41, 39, 37, 36, 36, 34, 32, 30, 28, 28, 27, 27, 25, 25, 23, 23, 23, 21, 21, 21, 19, 19,
            19, 19, 19, 19, 21, 23, 23, 23, 25, 27, 30, 36, 37, 37, 39, 39, 41, 41, 41, 39, 39, 41, 43, 43,
            43, 43, 43, 43, 43, 43, 43, 39, 37, 37, 37, 36, 36, 36, 36, 34, 32, 32, 32, 32, 30, 30, 28, 28,
            28, 27, 27, 27, 27, 25, 27, 27, 27, 28, 28, 28, 30, 32, 32, 32, 34, 34, 36, 36, 36, 37, 37, 37,
            37, 37, 37, 37, 37, 37, 36, 34, 30, 30, 27, 27, 25, 25, 23, 21, 21, 21, 21, 19, 19, 19, 19, 19,
            18, 18, 18, 18, 18, 19, 23, 27, 30, 32, 32, 32, 32, 32, 32, 34, 34, 34, 34, 34, 36, 36, 36, 36,
            36, 32, 32, 32, 32, 32, 32, 32, 32, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 28, 28]

# Begin your functions and code here, do not forget to document your code with comments
# A temperature analyzer program that converts Fahrenheit to Celsius
# @author Mark Kasule
# DATA 300
# 05/04/2024

# List of temperature classes
tempClasses = []


# Iterate over all given temps and assign classes to tempClasses list
def tempIterator(tempDataList):
    for temp in tempDataList:
        # Convert temp to Celsius
        tempCelsius = fahrToCelsius(temp)
        # find tempCelsius' class
        tempClass = tempClassifier(tempCelsius)
        # Add to tempClasses list
        tempClasses.append(tempClass)


# Execute looping of temperature
tempIterator(tempData)

# Check for Results
print("Temperature Classes:", tempClasses)

# Counting 0s, 1s, 2s, 3s temperature classes
print("Number of cold temperature classes are", tempClasses.count(0))
print("Number of slippery temperature classes are", tempClasses.count(1))
print("Number of comfortable temperature classes are", tempClasses.count(2))
print("Number of warm temperature classes are", tempClasses.count(3))
