curr_bal = 100
with_amt = 90
print(curr_bal == with_amt)

num1 = int(input("Enter first number:"))
num2 = input("Enter second number:")
print("Sum is ", (num1 + int(num2)))
print("Sum is ", +(num1 + int(num2)))

P_amt = 3000
R_amt = 9
Nyear = 3
Interest = (P_amt * R_amt * Nyear) / 100
print(Interest)

P_amt = int(input("Enter the Principle amount: "))
R_amt = int(input("Enter the rate of interest: "))
Nyear = int(input("Enter the no of years: "))

Interest = (P_amt * R_amt * Nyear) / 100
print(Interest)
