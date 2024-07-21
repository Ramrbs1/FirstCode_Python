#open a file oin a read mode
f=open('abc.txt', 'r')
print(f.read())

#open a file oin a write mode
file=open("abc.txt", 'w')
file.write("This is line 4")
file.close()

print (file.read())


f=open('abc.txt', 'r')
print(f.read())

file=open("abc.txt", 'w')
file.write("This is line 6")
file.close()


try:
  f_path = "FirstCode_Python/TextFiles/abc.txt"
  with open(f_path, 'r') as file:
    lines = file.readlines()
    print(lines)
except:
  print("Files not found")

with open("FirstCode_Python/TextFiles/abc.txt", 'r') as file:
print(file.read())

#To write in qa file:
f_path = "FirstCode_Python/TextFiles/abc.txt"
with open(f_path, 'w') as file:
  file.write("Name : Ram " + "\n")
  file.write("Color : Red " + "\n")
  file.write("Country : India " + "\n")

with open("FirstCode_Python/TextFiles/abc.txt", 'r') as f:
  print(f.read()

#append in a line in the file
f_path = "FirstCode_Python/TextFiles/abc.txt"
with open(f_path, 'a') as file:
  file.write("Continent : asia " + "\n")


with open("FirstCode_Python/TextFiles/abc.txt", 'r') as f:
  print(f.read())

#If we open teh file like below then we need to exclusively close teh file but while we open the file using" with" then system automaticlaly close it

f_path = "FirstCode_Python/TextFiles/abc1.txt"
f = open(f_path, 'w')
f.write("Continent : asia " + "\n")
f.close()

f = open("FirstCode_Python/TextFiles/abc1.txt", 'r')
print(f.read())

with open("FirstCode_Python/TextFiles/abc.txt") as f:
  lines = f.readlines()
print(lines)

Name = lines[0].strip().split(": ")[1] #pritn the second element in the first line
Country = lines[2].strip().split(": ")[0] # print the first element in the 3rd line
print(Name)
print(Country)

with open("FirstCode_Python/TextFiles/abc.txt") as f:
  lines = f.readlines()
print(lines)

Name = lines[0].strip().split(": ")[1] #print the second element in the first line
Name1 = lines[0].strip().split(": ")[2] #print the third element in the first line
Name2 = lines[0].strip().split(": ")[-1] #print the last element in the first line
Country = lines[2].strip().split(": ")[0] # print the first element in the 3rd line

print(Name)
print(Name1)
print(Name2)
print(Country)

# Create a Python program that allows a user to store customer details. The program
# should prompt the user to enter the customer’s account number, name and
# balance. The program should then write these details to the corresponding text file.
# Note:# 1.# Keep a record of each customer in a text file with the customer’s account number # as the file name
Name = input("Enter the Name: ")
AccNum = input("Enter the Account Number: ")
acaBal = input("Enter teh balance: ")

f = open('FirstCode_Python/TextFiles/' + AccNum + ".txt", 'w')
f.write("Name : " + Name + "\n")
f.write("Account Number : " + AccNum + "\n")
f.write("Balance : " + acaBal + "\n")
f.close()
f = open("FirstCode_Python/TextFiles/" + AccNum + ".txt", 'r')
print(f.read())