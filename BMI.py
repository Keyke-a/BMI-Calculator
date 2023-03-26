#Assignment
#Write a code that can calculate the Body Mass Index of an individual.
#Formular:weight\height * height in meters
#django..

name = input("enter your name ")
weight = float(input("Enter weight "))#To get the weight of the user in kg
height = float(input("Enter height "))#To get the height of the user in cm
#Note:-
#1m = 100cm
#xm = input of height
convert_height = (height/100) * (height/100)#converting to m2
BMI = (weight/(convert_height))#To calculate the BMI of the user

print("Hello " + name +"," + "\n" + "Your Body Mass Index " + str(round(BMI,2)) + "kg/m2." "\n" "Thank you")