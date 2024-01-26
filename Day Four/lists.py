counties_in_kenya = ["Kisii", "Kitui", "Mombasa"]
print(counties_in_kenya[1])

# Last item in the list
print(counties_in_kenya[-1])

# Changing items
counties_in_kenya[1] = "Turkana"
print(counties_in_kenya)

# Add items in the list
counties_in_kenya.append("Garissa")
print(counties_in_kenya)

#Extend list

counties_in_kenya.extend(["Kitui", "Lamu"])
print(counties_in_kenya)
