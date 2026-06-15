import time
import datetime




#variables
welcome_message = "Welcome to Wealthy Banker's ATM :-) \nChoose an option from the menu."
menu = " MENU \n1. Withdraw money \n2. Deposit money \n3. Exit"
date_today = datetime.date.today()

#data collection
client1 = {
  "name": "Client #10987",
  "pin":3000,
  "balance":2000000,
  
}

transactions_list = []

#procedures

def verify_pin():
  pin_inquiry = int(input("Enter your pin: "))
  if pin_inquiry == client1["pin"]:
    return True
  else:
    print("Wrong pin entered. Please try again.")
    return False
  
def confirm_transaction():
  assurance = input("Are you sure you want to make this transaction? (yes or no): ")
  if assurance.lower() == "yes":
    return True
  else:
    print("Transaction cancelled. Going to main menu.")
    return False

def record_transaction(transaction_type, amount):
  transactions_list.append(f"{transaction_type}: UGX {amount} ‖ Date: {date_today} ‖ New Balance: UGX {client1['balance']}")

def withdraw(amount):
  if 0 <= amount <= client1["balance"]: 
    if verify_pin():
      if confirm_transaction():
        client1["balance"]-= amount
        time.sleep(2)
        print(f"Transaction complete! \nYour new balance is UGX {client1['balance']} \n")
        record_transaction("Withdrawal", amount)
  else:
    print("Amount inputted is invalid or beyond current account balance")
  
      


def deposit(amount):
  if 0 <= amount: 
    if verify_pin():
      if confirm_transaction():
        client1["balance"]+= amount
        time.sleep(2)
        print(f"Transaction complete! \nYour new balance is UGX {client1['balance']}")
        record_transaction("Deposit", amount)
    

def show_exit():
  print("⁓"*80)
  print(f"Thank you for banking with us, {client1['name']}. This is a list of your transactions: \n ")
  if not transactions_list:
    print("No transactions made.")
  else:
   for n, transaction in enumerate(transactions_list, start=1):
    print(f"{n}. {transaction}")
  
  print("Goodbye!")
  

#main code

print(welcome_message)
time.sleep(2)

while True:
  print(menu)

  try:
    option = input("Enter your option: ")
  

    if option =="1":
      amount = int(input("How much would you like to withdraw? UGX "))
      withdraw(amount)
    elif option =="2":
      amount = int(input("How much would you like to deposit? UGX "))
      deposit(amount)
    elif option == "3":
      show_exit()
      break
    else:
      print("Invalid option. Please enter 1, 2 or 3.")

  except ValueError:
    print("Invalid input. Please enter a number.")  
  
    



    