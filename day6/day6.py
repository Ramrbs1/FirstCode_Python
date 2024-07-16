email_id = input("Enter your email id: ")
last_Char = email_id[-4:]
#print(last_Char)
found = False

for i in email_id:
  if i == "@":
    found = True
    #print("Symbol @ found in the given email id so Moving ahead")
    #break

#print(found)
if found == True and last_Char == ".com":
  print(email_id, "This is valid Email id")
else:
  print(email_id, "This is invalid Email id")
