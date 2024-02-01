# Defining a dictionary
dictionary_new = {
 "Bug": "An error in a program that prevents the program from running as expected.", 
 "Function": "A piece of code that you can easily call over and over again."
}

# Extracting elements from the dictionary
dictionary_new["Function"] 

# Adding new items
dictionary_new["Boy"] = "He is a man"

# Creating an empty dictionary
empty_dictionary = {}

dictionary_new = {} # Clears and make existing dictionary become empty

# Editing an item in dictionary
dictionary_new["Bug"] = "Bad thing"


for key in dictionary_new:
    print(key)

