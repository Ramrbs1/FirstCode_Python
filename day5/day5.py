# if we don't provide the step up valu, it takes 1 by defauly
for i in range(1, 11):
  print("This is the number : ", i)

for i in range(1, 11, 1):
  print("This is the number : ", i)

#it will step up teh value by 2 as we provide teh stepup value 2
for i in range(1, 11, 2):
  print("This is the number : ", i)

#if we don't define the start value, it picks up from 0
for i in range(11):
  print("This is the number : ", i)

#print the even number till 50
for i in range(2, 51, 2):
  print("This is the number : ", i)

#print the account number in given range
for accNo in range(12345670, 12345699):
  print("This is the Account number : ", accNo)

#else with For loop

startVal = int(input("Start Value"))
endVal = int(input("End Value"))
#print ("The account numbers in range" , startVal, "to" endVal)
print(f"The account numbers in range {startVal} to {endVal}")

for accNo in range(startVal, endVal):
  print("This is the Account number : ", accNo)
else:
  print("print compeleted")

#index is always start with 0 in python
print("print , compeleted")
print('print , compeleted')

My_strg = "Hello"
for char in My_strg:
  print(char)
''' mulit line comment
comment'''
"""multi line text
multi line text"""

My_strg = "Hello"
for char in My_strg:
  print(char)
print("This is the length of :", len(My_strg))

for i in range(0, len(My_strg)):
  print(My_strg[i])

#slice the team only from the string
SampleText = "Team Digital X"
print(SampleText[0:4])

SampleText = "Team Digital X"
# print("This is the first part: ", SampleText[0:4])
# print("This is the second part : ", SampleText[5:12])

print("This is the second part : ", SampleText[5:len(SampleText)])

#while we concanate string, if use , then space will be added automatically but if we use + then there would not be any space

FirstName = 'Ram'
LastName = 'Kumar'
Greetingmsg = 'Hey !' + ' ' + FirstName + ' ' + LastName + ' ' + 'Good Morning '
print(Greetingmsg)

FirstName = 'Ram'
LastName = 'Kumar'
Greetingmsg = 'Hey !' + ' ' + FirstName + ' ' + LastName + ' ' + 'Good Morning '
print(Greetingmsg.upper())
print(Greetingmsg.isupper())

passWord = input('Enter password:  ')
if len(passWord) >= 8 and passWord.islower() == False and passWord.isalpha(
) == False:
  print('valid password')
else:
  print(
      "Invalid password, it's lentgh must be 8 char and should have one uppercase letter, one digit"
  )

pwd = input('Enter Password : ')
# if len(pwd)>=8 and pwd.islower() == False and pwd.isalpha()== False:
#   print('Password is valid')
# else:
#   print('Password is valid')

Var_upperCase = False
Var_digits = False

if len(pwd) >= 8:
  #check for upper case
  for i in range(len(pwd)):
    if pwd[i].isupper() == True:
      Var_upperCase = True
      break

  #check for digits
  for i in range(len(pwd)):
    if pwd[i].isdigit() == True:
      Var_digits = True
      break

print(Var_upperCase, Var_digits)

if Var_upperCase == True and Var_digits == True:
  print('Password is valid')
else:
  print('Password is not valid')
