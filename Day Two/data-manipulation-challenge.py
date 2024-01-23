#Your Life in Weeks Challenge

age = input("What is your current age?")

#Assuming mortality at 90 years

remaining_years  = (90 - int(age))

#Assuming there are 365 days in a year, 52 weeks in a year and 12 months in a year.

remaining_days = 365 * remaining_years
remaining_weeks = 52 * remaining_years
remaining_months = 12 * remaining_years

print(f"You have {remaining_days}, {remaining_weeks}, and {remaining_months} left.")
