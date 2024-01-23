#BMI Calculator

#Prompt for input of height and weight
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

#Check data types
print(type(height))
print(type(weight))

#Convert strings to float
height_int = float(height)
weight_int = float(weight)

#Calculate BMI
BMI = weight_int / height_int ** 2
print(BMI)

#Convert to whole number
BMI_int = int(BMI)
print(BMI_int)
