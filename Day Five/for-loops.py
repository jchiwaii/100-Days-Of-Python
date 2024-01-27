# For Loops allow execution of a code multiple times

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit + " Pie")


for number in range (1, 10):
    print(number)

for number in range (1, 10, 4): # Four steps in the range
    print(number)

total = 0
for num in range(1, 101):
    total += num
print(total)