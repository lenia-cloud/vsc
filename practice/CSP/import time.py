import time
import datetime

# Variables
welcome_message = "Welcome to Wealthy Banker's ATM :-) \nChoose an option from the menu."
menu = " MENU \n1. Withdraw money \n2. Deposit money \n3. View transaction history\n4. Exit"
date_today = datetime.date.today()

# Data collection
client1 = {
  "name": "Bethel Lenia",
  "pin": 3000,
  "balance": 2000000,
}

transactions_list = []

# Helper function: Verify PIN
def verify_pin():
  """Asks user for PIN and returns True if correct, False if wrong"""
  pin_inquiry = int(input("Enter your pin: "))
  if pin_inquiry == client1["pin"]:
    return True
  else:
    print("Wrong pin entered. Please try again.")
    return False

# Helper function: Confirm transaction
def confirm_transaction():
  """Asks user to confirm a transaction and returns True or False"""
  assurance = input("Are you sure you want to make this transaction? (yes or no): ")
  if assurance.lower() == "yes":
    return True
  else:
    print("Transaction cancelled. Going to main menu.")
    return False

# Helper function: Record transaction
def record_transaction(transaction_type, amount):
  """Records a transaction with type, amount, date, and new balance"""
  transactions_list.append(f"{transaction_type}: UGX {amount} | Date: {date_today} | New Balance: UGX {client1['balance']}")

# Withdraw function
def withdraw(amount):
  """Handles money withdrawal with validation and PIN verification"""
  if amount <= 0:
    print("Invalid amount. Please enter a positive number.")
    return
  
  if amount > client1["balance"]:
    print(f"Insufficient balance. Your current balance is UGX {client1['balance']}")
    return
  
  if verify_pin():
    if confirm_transaction():
      client1["balance"] -= amount
      time.sleep(2)
      print(f"Transaction complete! \nYour new balance is UGX {client1['balance']} \n")
      record_transaction("Withdrawal", amount)

# Deposit function
def deposit(amount):
  """Handles money deposit with validation and PIN verification"""
  if amount <= 0:
    print("Invalid amount. Please enter a positive number.")
    return
  
  if verify_pin():
    if confirm_transaction():
      client1["balance"] += amount
      time.sleep(2)
      print(f"Transaction complete! \nYour new balance is UGX {client1['balance']} \n")
      record_transaction("Deposit", amount)

# View transaction history function
def view_transactions():
  """Displays all transactions made during this session"""
  print("⁓" * 80)
  print(f"Transaction History for {client1['name']}: \n")
  if len(transactions_list) == 0:
    print("No transactions made yet.")
  else:
    for n, transaction in enumerate(transactions_list, 1):
      print(f"{n}. {transaction}")
  print("⁓" * 80)

# Exit function (renamed from exit)
def show_exit():
  """Displays goodbye message and final transaction history"""
  print("⁓" * 80)
  print(f"Thank you for banking with us, {client1['name']}. Here is your transaction history: \n")
  if len(transactions_list) == 0:
    print("No transactions made during this session.")
  else:
    for n, transaction in enumerate(transactions_list, 1):
      print(f"{n}. {transaction}")
  print("Goodbye!")
  print("⁓" * 80)

# Main code
print(welcome_message)
time.sleep(2)

while True:
  print(menu)
  try:
    option = input("Enter your choice (1-4): ")
    
    if option == "1":
      amount = int(input("How much would you like to withdraw? UGX "))
      withdraw(amount)
    elif option == "2":
      amount = int(input("How much would you like to deposit? UGX "))
      deposit(amount)
    elif option == "3":
      view_transactions()
    elif option == "4":
      show_exit()
      break
    else:
      print("Invalid option. Please enter 1, 2, 3, or 4.")
  
  except ValueError:
    print("Invalid input. Please enter a number.")
