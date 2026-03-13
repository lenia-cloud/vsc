
##Variables
welcome_message = "******** Welcome to the ATM System ****"
menu = "1. Withdraw money \n2. Deposit money \n3. Pin Reset \n4. Transactions"

client = {
  "name": "Mark Goody",
  "pin": 8902,
  "phone_number": "0772003004",
  "balance": 2000000, 
}

transactions_list=[]

## Functions

def withdraw(amount):
  pin_entry = int(input("Enter your PIN: "))
  if pin_entry == client["pin"]:
    if amount < client["balance"]:
      client["balance"] -= amount
      transactions_list.append(f"Withdrawal: UGX {amount}")
      print(f"Your new balance is: UGX {client['balance']} \n")
    else:
      print("Insufficient mapesa :-( \n")
  else:
    print("PIN is incorrect")
    prompt = input("Do you want a pin reset? (Yes or no)")
    if prompt.lower() =="yes":
      pin_reset()
    elif prompt.lower == "no":
      withdraw(amount)
    else:
      print("Invalid input. Please try again.")
      withdraw(amount)


def pin_reset():
  phone_number = input("Enter the phone number attached to this account")
  if phone_number == client["phone_number"]:
    new_pin = input("Enter your new PIN")
    client["pin"] = new_pin

def deposit(amount):
  client["balance"] += amount
  print(f"Deposit was successful. \n New balance: UGX {client['balance']} \n")
  transactions_list.append(f"Deposit: UGX {amount}")

def transactions():
    n=1
    for transaction in transactions_list:
      print(f"{n}. {transaction}")
      n += 1

  


import time

while True:
  print(welcome_message)
  print("Loading...")
  time.sleep(1)
  print(menu)
  option = input("Please enter your option: ")
  if option == "1":
    amount = int(input(f"Enter amount to withdraw: (Account Balance: UGX {client['balance']})"))
    withdraw(amount)
   
  elif option == "2":
    amount = int(input("Enter amount to deposit:"))
    deposit(amount)
  elif option == "3":
    pin_reset()
  elif option == "4":
    transactions()
    


