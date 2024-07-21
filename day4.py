usd = 84
ex_rate = 81
inr = usd * ex_rate

print("you usd ammount is : ", usd, "and exchange rate is :", ex_rate,
      "and converted ammount in INR is : ", inr)

count = 0
while (count < 5):
  print("Hello there!")
  #count = count+1
  count += 1

count = 10
while (count > 0):
  print("Hello there!")
  #count = count+1
  count -= 1

correctpass = "Python123"
counter = 0
while counter < 3:
  userpass = input("Enter the password: ")
  if userpass == correctpass:
    print("This is correct password, you are logged in")
    break
  else:
    counter += 1
    print("Incorrect password")
    continue
else:
  print("Your account has been locked, Please try again ")

import random

print("your 6 digit OTP is : ", random.randint(100000, 999999))

dice_result = (random.randint(1, 6))
print("Dice Role Result: ", dice_result)

import random
#print("your 6 digit OTP is : ", random.randint(100000, 999999))

G_num = (random.randint(1, 3))
Rock = 1
Paper = 2
Scissors = 3
print("Dice Role Result: ", dice_result)
