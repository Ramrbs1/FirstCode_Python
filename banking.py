import random

#emplty lists
customer_name = []
account_number = []
balance = []

index = None
validity = None

def createAcc():
  CustName = input("Enter customer Name : ")
  accNumber = random.randint(10000, 99999)
  accBal = 0
  customer_name.append(CustName)
  account_number.append(accNumber)
  balance.append(accBal)
  print ("Account has been created for :", CustName, "with account number: ", accNumber )
  GetAccDetails(accNumber)

def fetch_index(accNumber):
  global validity
  global index

  acc_no = int(accNumber)
  for k in range(0, len(account_number)):
    if acc_no == account_number[k]:
      index = k
      validity = True
      print("Account found in the system which is :", acc_no)
      break
    else:
      validity = False
      print("Account number", acc_no, "does not exist")


def GetAccDetails(accNumber):
  fetch_index(accNumber)
  if validity == True:
    print("Name: ", customer_name[index])
    print("Account Number: ", account_number[index])
    print("Balance: ", balance[index])
  else:
    print("Account number", accNumber, "does not exist")

def deposit(accNumber):
  #accNumber = int(input("Enter the account details: "))
  fetch_index(accNumber)
  if validity == True:
    amt = int(input("Enter the amount to be deposited: "))
    balance[index] = balance[index] + amt
    print("Amount deposited successfully and your current Balance is ", balance[index])
  else:
    print("Account number", accNumber, "does not exist")

def withdrawl(accNumber):
  #accNumber = int(input("Enter the account details: "))
  fetch_index(accNumber)
  if validity == True:
    print("Balance in your acc: ", balance[index])
    amt = int(input("Enter the amount to be withdrawn: "))
    if balance[index] - amt >=0:
      balance[index] = balance[index] - amt
      print("your balance is :" , balance[index])
    else:
      print("your balance is lower than your withdrawl amount")
  else:
    print("Account number", accNumber, "does not exist")


while (True):
  choice = int(
  input('''Press 1 to create account
press 2 to Get account details
Press 3 for deposite the amount into Account
Press 4 for Widraw the Cash from account
Press 5 for Exit'''+"\n"))
  if choice == 1:
    while(True):
      createAcc()
      break
    else:
      continue
      
  if choice == 2:
    accNumber = int(input("Enter the account details: "))
    GetAccDetails(accNumber)
  if choice == 3:
    accNumber = int(input("Enter the account details: "))
    deposit(accNumber)
  if choice == 4:
    accNumber = int(input("Enter the account details: "))
    withdrawl(accNumber)
  if choice == 5:
    print("Thank you for using our banking services, You are exited from the system")
    exit()

  user_input = input("Do you want to continue ? y/n")
  if user_input == 'y':
    continue
  else:
    print("Thank you for using our banking services, You are exited from the system")
    break