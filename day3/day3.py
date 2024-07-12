num = int(input("enter number: "))
if num > 0:
  print("you entered ", num, "which is positive")
else:
  print("you entered ", num, "which is not positive")

current_day = (input("Enter the current day: "))
if current_day == "saturday" or current_day == "sunday":
  print("its weekend , Enjoy !")
else:
  print("it's week day so You need to go office")
