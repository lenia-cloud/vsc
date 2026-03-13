products = {
  "Jordans": 200,
  "Nikes":200,
  "Sambas":200,
  "Vans": 200,

}



def receipt(cart):
  total=0
  list=["⁙"*20, "RECEIPT", "⁙"*20]
  for choice, cost in cart:
    list.append(f"{choice} --- {cost}")
    total += cost
    
  list.append(f"Total: USD {total}")
  return "\n".join(list)




def main():
  cart=[]
  answer=0
  while True:
    if answer==0:
      choice = input("Which brand would you like to buy?")
    else:
      choice = input("anything else?")
  
    if choice in products:
      cost= products[choice]
      print(cost)
      cart.append((choice,cost))
      answer=1
    elif not choice:
      break
    else:
      answer=1
      print(f"We don't have {choice} available.")
  print(receipt(cart))


def display_products():
  for product, cost in products:
    print(product, cost)


main()

