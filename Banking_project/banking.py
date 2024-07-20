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



def fetch_index():
  global validity
  global index

  acc_no = int(accNumber)
  for k in range(0, len(account_number)):
    if acc_no == account_number[k]:
      index = k
      validity = True
      print("Account founf in the system which is :", acc_no)
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
createAcc()

GetAccDetails(GetAccDetails)


