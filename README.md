# Converting and Classifying Temperature Data
This exercise is meant to help you to understand how to use functions in Python. In this week's exercise you are asked to create a simple tool that converts temperatures from one temperature-type to another and then classify those temperatures into specific temperature classes.
Pay particular attention to the variable and file names listed below.  You must use the variable and file names as indicated.  In particular for the variable names, they may differ slightly from similar variable names from the tutorials.
Part 1 - Simple temperature calculator 
In the first part your aim is to create a function that converts the input temperature from degrees Fahrenheit to degrees Celsius. Create a script called functions.py where you should write your code for Problem 1.
You should do following (also criteria for grading):
- Create a function called fahrToCelsius in functions.py
- The function should have one input parameter called tempFahrenheit
- Inside the function, create a variable called convertedTemp to which you should assign the conversion result (i.e., the input Fahrenheit temperature converted to Celsius)
- The conversion formula from Fahrenheit to Celsius is:
	 ```
        T(C) = (T(F) - 32) / 1.8
    ```
- Return the converted value from the function back to the user
- Comment your code that explains how to use your fahrToCelsius function (i.e., you should write the purpose of the function, parameters, and returned values)
- Test and use your newly created function by finding the results for following questions:
    - What is 48° Fahrenheit in Celsius? ==> No need to submit the result, but confirm your result is correct. 
    - What about 71° Fahrenheit in Celsius? ==> No need to submit the result, but confirm your result is correct.
- Save your script with the name functions.py.  If you save to Google Colab temporary/session storage, do not forget to download the file to your own computer.
If everything in your script is working properly the following test case should work:
```
>>> print("32 degrees Fahrenheit in Celsius is:", fahrToCelsius(32))
32 degrees Fahrenheit in Celsius is: 0.0
```
### Questions for Part 1
Respond to the following questions based on your learning experience with the module, the course materials and additional external research (as needed)
1.	Is the concept of function clear to you? If not, what do you not understand?
2.	What are the benefits of using functions in your script?
3.	Does it matter in which order the functions are written in a script? If you think it does, why? 
Write your Responses to these questions at the end of this file.
### Part 2 - Temperature classifier
In Part 2 of this assignment, we will classify temperatures into four different classes (i.e., cold, slippery, comfortable, warm). <br>
Return value	Classification criteria
* 0	temperatures below -2 degrees (Celsius)
* 1	temperatures from -2 up to +2 degrees (Celsius) [1]
* 2	temperatures from +2 up to +15 degrees (Celsius) [2]
* 3	temperatures above +15 degrees (Celsius)

_[1] Values -2 and +2 should belong to this class; [2] Value +15 should belong to this class
This function can be added to your functions.py script started in Problem 1._

You should do following (also criteria for grading):
* Create a new function called tempClassifier
* tempClassifier should have one parameter called tempCelsius
* Your function should reclassify the input temperature based on the criteria in the table above
* Return the reclassified value as an integer number (i.e., 0, 1, 2, or 3)
* Add comments in your code that explains how to use your tempClassifier function (i.e., you should write the purpose of the function, parameters, and returned value(s))
* Test and use your newly created function by finding the results for following questions:
* What is class value for 16.5 degrees (Celsius)? ==> No need to submit the result, but confirm your result is correct.
  * What is the class value for +2 degrees (Celsius)? ==> No need to submit the result, but confirm your result is correct.
  * Add the changes to your functions.py script.
  
### Part 3 - Classify temperatures
Finally, we can bring together the pieces that we have created thus far. In the last problem your aim is to take advantage of your new functions and reclassify a dataset of temperatures in Fahrenheit into four different classes. You should create a new script called temp_analyzer.py where you add all your code related to Problem 3.
In the Exercise 3 instructions area, you have been provided with an initial temp_analyzer.py file which has the data ready for use.
Overview
The analysis process has three main steps:
1)	Read in the tempData and iterate over the Fahrenheit temperatures
2)	Convert the Fahrenheit temperature to Celsius using your fahrToCelsius function from that was created in Problem 1
3)	Classify the converted temperature using the tempClassifier function that was created in Problem 2
 
In more detail, you should do following (also criteria for grading):
* Build upon the script temp_analyzer.py and write all your code to that script from now on (all functions should be contained within the temp_analyzer.py file)
* Include the fahrToCelsius and tempClassifier functions from functions.py within your temp_analyzer.py file
* Create an empty list called tempClasses (which will be filled with temperature class numbers later)
* Iterate over the Fahrenheit temperature values in the tempData list (one by one) and:
  * Create a new variable called tempCelsius in which you should assign the temperature in Celsius using the fahrToCelsius function to convert the Fahrenheit temperature into Celsius.
  * Create a new variable called tempClass in which you should assign the temperature class number (0, 1, 2, or 3) using the tempClassifier function
  * Add the tempClass value to the tempClasses list
* How many temperatures are there within each temperature class?
  * Count the number of zeros, ones, twos, and threes in the tempClasses list and print out the results at the end of your script
  * Make sure the output is comprehensible to the person reading the output (do NOT simply print out 4 numbers without any explanation)
  * Include your output at the end of this document (either cut and paste text or a screen ‘snip’ image of the output
  * Tip: You might want to consider using a count() function OR a for loop to handle this
* Add comments in your code that explains what the temp_analyzer script does and how it is used.
* Save your temp_analyzer.py script to your computer, so you can submit the file.
Files to submit to LEO:
•	This document (with completed Part 1 Responses section and Part 3 Output)
•	Functions.py (with code for Parts 1 and 2)
•	temp_analyzer.py (with all code for Part 3)