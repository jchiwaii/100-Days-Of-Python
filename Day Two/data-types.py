#Data Types

#String

print("Hello"[4]) #Subscripts a string according to the number in the brackets

#Prints specific letters
street_name = "Kenyatta Road"
print(street_name[2] + street_name[7])

#Anything in double quotations is a string 
print("123" + "345") 
print("False")

#Integer - Numbers with no decimal places

print(123+345) #Actual numbers

123_345_567 #Visualize large numbers. _ is used in place of ,

#Float - Contains a decimal place

3.4555

#Boolean - Only two possible values

True
False

#Checks variable type
num_char = len(input("What is your name?"))
print(type(num_char)) 

#Results to an error
print("Your name has " + num_char + " characters.") #You can only combine same data types together, eg string to string or int to int

#Change data type from int to string

num_str = str(num_char)
print("Your name has " + num_str + " characters.") #Code now runs

#Change to float
a = float(123)
print(type(a))

print (100 + float(200.44)) #Adds normally; 300.44

print (str(40) + str(60)) #Prints the number 4060


