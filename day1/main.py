# "Write a python program to get the name ,country and current balance amount from the user and add 5000 to the current balance and display the new balance in the below format Sample input:
# Name=Hannah
# Country= India
# Current balance = 7500
# Sample output:
# Hey Hannah! Your current balance is 12500"

Name = 'Hannah'
Country = 'India'
Current_balance = 7500
print("Hey", Name, "! Your current balance is", Current_balance + 5000)

# "Write a python program to get the number of days from the user and display its equivalent value in months.
# Sample Input:
#   Number of days = 45
# Sample output:
#   45 days = 1 month and 15 days"

Days = int(input("Enter Number of days"))
Number_of_Months = Days / 30
Number_of_remainings_days = Days % 30
print(int(Number_of_Months), "month and", Number_of_remainings_days, "days")
