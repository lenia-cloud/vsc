
num = int(input("Choose any number. "))

while 1<num<100 :
  reply = input("Do you want to continue?")
  if reply == "yes":
    num = int(input("Choose any number. "))
  else:
    num = 0
    


if num == 0:
  print("end")
else:
  print("error")



