import time
import datetime




#variables
welcome_message = "Welcome to Wealthy Banker's ATM :-) \nChoose an option from the menu."
menu = " MENU \n1. Withdraw money \n2. Deposit money"
date_today = datetime.date.today()

#data collection
client1 = {
  "name": "Bethel Lenia",
  "pin":3000,
  "balance":2000000,
}

transactions_list = []
#procedures

def withdraw(amount):
  if 0 <= amount <= client1["balance"]: 
    pin_inquiry = int(input("Enter your pin: "))
    if pin_inquiry == client1["pin"]:
      assurance = input("Are you sure you want to make this transaction?(yes or no)")
      if assurance.lower()=="yes":
        client1["balance"]-= amount
        time.sleep(2)
        print(f"Transaction complete! \nYour new balance is UGX {client1['balance']} \n")
        transactions_list.append(f"Withdrawal:{amount} \n Date: {date_today} \n")
      else:
        print("Transaction cancelled. Going to main menu.")


    else:
      print("Wrong pin entered. Please try again.")
      
  else:
    print("Amount entered is more than current account balance or invalid. \nPlease try again.")

def deposit(amount):
  if 0 <= amount: 
    pin_inquiry = int(input("Enter your pin: "))
    if pin_inquiry == client1["pin"]:
      assurance = input("Are you sure you want to make this transaction?(yes or no)")
      if assurance.lower()=="yes":
        client1["balance"]+= amount
        time.sleep(2)
        print(f"Transaction complete! \nYour new balance is UGX {client1['balance']}")
        transactions_list.append(f"Deposit:{amount} \n Date: {date_today} \n")
      else:
        print("Transaction cancelled. Going to main menu.")
    


    else:
      print("Wrong pin entered. Please try again.")
      
  else:
    print("Invalid amount entered. \nPlease try again.")



#main code

print(welcome_message)
time.sleep(2)
while True:
  print(menu)
  option = int(input(""))
  if option == 1:
    amount = int(input("How much would you like to withdraw?  "))
    withdraw(amount)
  elif option == 2:
    amount = int(input("How much would you like to deposit?  "))
    deposit(amount)
  else:
    print("Invalid option. Please try again.")
    



    