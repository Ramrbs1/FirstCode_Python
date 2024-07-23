import random

# empty list
customer_name=[]
account_number=[]
balance=[]

index=None
validity=None

def createAccount():
  CustName=input('Enter your name: ')
  AccNumber=random.randint(100,999)
  AccBalance=0
  print('Acc Created Succesfully!,Your account No :',AccNumber )

  customer_name.append(CustName)
  account_number.append(AccNumber)
  balance.append(AccBalance)



def fetch_index(AccNumber):

  global validity
  global index


  # AccNumber=int(input('Please enter your account number '))
  for existing_accounts in range(0,len(account_number)):
    if AccNumber==account_number[existing_accounts]:
      validity=True
      index=existing_accounts
      print('Account found')
      break
    else:
      print('Invalid account number. Please try again.')
      validity=False
# AccNumber=int(input('your acc No to get acc details '))
def GetAccountDetails(AccNumber):
  # AccNumber=int(input('your acc No to get acc details '))
  fetch_index(AccNumber)
  if validity==True:
    print('Name: ' , customer_name[index])
    print('Account Number: ' , account_number[index])
    print('Balance: ' , balance[index])




def deposit(AccNumber):
  # AccNumber=int('Enter account details:')
  fetch_index(AccNumber)
  if validity:=True:
    deposit_amount=int(input('Enter Deposit Amount: '))
    balance[index]=balance[index]+deposit_amount
    print('Deposit Successful')  
    print('Your new balance is: ', balance[index] )
  else:
    print('Invalid account number')    

def withdrawal(AccNumber):
  # AccNumber=int('Enter account details:')
  fetch_index(AccNumber)
  if validity:=True:
    withdrawal_mount=int(input('Enter withdrawal amount: '))
    if balance[index] - withdrawal_mount >= 0:
      balance[index]=balance[index]-withdrawal_mount
      print("Yor balance is now: ", balance[index] )
    else:
      print('Insufficient Balance')
  else:
    print('Invalid account number')

createAccount()
AccNumber=int(input('your acc No to get acc details '))
GetAccountDetails(AccNumber)
AccNumber=int(input('your acc for deposite '))
deposit(AccNumber)
AccNumber=int(input('your acc for Withdrawal  '))
withdrawal(AccNumber)