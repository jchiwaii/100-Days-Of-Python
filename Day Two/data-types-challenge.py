#Instructions

#Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

#Warning. Do not change the code on lines 1-3. Your program should work for different inputs. e.g. any two-digit number.
#Example Input

#39

#Example Output

#3 + 9 = 12

#12

#Answer

#Requests input from user
two_digit_number = input("Type a two digit number: ")

#Checkts data type
print(type(two_digit_number))

#Subscripts the two digits
a = two_digit_number[0]
b = two_digit_number[1]

#Converts to integer
a_int = int(a)
b_int = int(b)

#Performs operation
a_int + b_int
