
menu = {
  "coffee": 5000,
  "african tea": 2000,
  "sausages": 2000,
  "samosas": 3000,
}


def receipt(cart):
  lines = ["-"*20, "RECEIPT"]
  total=0
  for product, price in cart:
    lines.append(f"{product}--- Shs.{price}")
    total += price
  lines.append(f"TOTAL: {total}")
  return "\n".join(lines)
  
def undo(cart):
  if not cart:
    return [], "cart already empty"
  else:
    [*rest, last] = cart
    product, price = last
    return rest, f"{product} removed from cart. {price} deducted from total."

def main():

  cart=[]


  while True:
    choice = input("choice:")

    if choice in menu:
      price = menu[choice]
      print(price)
      cart.append((choice, price))
      print(f"{choice} added to cart")

    elif choice == "menu":
      for x, price in menu.items():
        print(f"{x}-shs.{price}")

    elif choice == "undo":
      cart, message = undo(cart)
      print(message)

    elif not choice:
      break
    else:
      print(f"{choice} not found")

  print(receipt(cart))

main()
