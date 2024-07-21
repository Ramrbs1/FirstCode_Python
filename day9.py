def welcome():
  print("Welcome in this Digital X")

welcome()

def greeting():
  print("Hello Welcome" * 5)

greeting()

#checking minor or major
def minorOrMajor(age):
   if age < 18:
     print ("The person is minor and his agen is : ", age)
   else:
    print ("The person is major and his age is : ", age)
#calling fuction 
minorOrMajor(15)
minorOrMajor(45)

def deposit(balance,amount):
  newBalance = balance + amount
  print ("your new abalance is = ", newBalance)

deposit(100, 1000)

def addTradedStock(oldStocks, noOfStocksToBeAdded):
  newStocks =  oldStocks + noOfStocksToBeAdded
  return newStocks

newStockValue = addTradedStock(100, 20)
print ("new stocks value is : ", newStockValue)
print("Another way to print :", addTradedStock(100, 5))