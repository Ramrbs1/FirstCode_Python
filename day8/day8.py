cc_pay_list = [11.4, 12.5, 33.5, 33.7, 55.7, 88.5]
print(cc_pay_list[2])
print(len(cc_pay_list))
print

print(cc_pay_list[len(cc_pay_list) - 1])
print(cc_pay_list[0])
print(cc_pay_list[3])
print(cc_pay_list[-3])

print(cc_pay_list[-1])  #negetive

bookself = [
    "Introduction to Python", "Data science Essentials",
    "Web Devlopement basisc", "Machin Learning 101", "Advance algorithms"
]

selected_books = bookself[1:4]
print(selected_books)

#for loop in list
payment_mar = [100, 20.68, 32.44, 640.60, 360]
for x in payment_mar:
  print(x)
#uning lenth function
for i in range(len(payment_mar)):
  print(payment_mar[i])

#Write a Python program to store the amount of 10 transactions in a list and display
#the number of transactions above 10000 and number of transactions less than or
#equal to 10000.
transactions = [3500, 45664, 7654, 12304, 5400, 6644, 463452, 664, 12345, 5555]
above_10k = 0
below_10k = 0
for x in transactions:
  if x < 10000:
    above_10k += 1
  else:
    below_10k += 1
print("the number of transaction above 10: " + str(above_10k))
print("the number of transaction below 10: ", below_10k)
#using lenth
transactions = [3500, 45664, 7654, 12304, 5400, 6644, 463452, 664, 12345, 5555]
above_10k = 0
below_10k = 0
for x in range(len(transactions)):
  if transactions[x] < 10000:
    above_10k += 1
  else:
    below_10k += 1
print("the number of transaction above 10: " + str(above_10k))
print("the number of transaction below 10: ", below_10k)

#use of lenth fuction for list and append in list 
direct_debits_April = [30, 16.99, 11.50, 57.89, 15]
a = len(direct_debits_April)
print(a)


direct_debits_April.append(14)

print(direct_debits_April)
a = len(direct_debits_April)
print(a)
#if we want to add more than one element in the list then we need to user extend:
direct_debits_April.extend([17, 99])
print(direct_debits_April)

#remove the value
direct_debits_April = [30, 16.99, 11.50, 57.89, 15]
direct_debits_April.remove(11.50)
print(direct_debits_April)

#remove using index index 2 1ill remove the value of index 2 , here is it 23
direct_debits_April = [30, 16.99, 23, 66, 57.89, 15]
direct_debits_April.pop(2)
print(direct_debits_April)

#change the value of index 
direct_debits_April = [30, 16.99, 23, 66, 57.89, 15]
direct_debits_April[2] = 55
print(direct_debits_April)

#sort value of a list in ascending order
direct_debits_April = [30, 16.99, -23, 66, 57.89, 15]
direct_debits_April.sort()
print(direct_debits_April)

#sort value of a list in descending order
direct_debits_April = [30, 16.99, -23, 66, 57.89, 15]
direct_debits_April.sort(reverse = True)
print(direct_debits_April)

# You are creating a shopping list for a grocery store. Perform the following
# operations using Python list functions:
# 1.Create a list called “shopping_list ” with the items "apples", "bananas", "bread",
# "
# 2.Print the number of items in the list
# 3.Add “eggs” to the list and print the items in the list
# 4.Remove “apples” from the list and print the items in the list
# 5.Sort the list in alphabetical order and print the items in the list

shopping_list = ["apple", "bananas", "bread", "milk"]
print(len(shopping_list))
shopping_list.append("orange")
shopping_list.remove("apple")
print(len(shopping_list), shopping_list )