name = input("What's your name? ")

if not name == "Saka" :
  print("Hey", name)
else:
  print("No.")

grade = int(input("What was your mark on the test? "))
if grade >= 90:
    print("You got an A")
elif grade >= 80:
    print("You got a B")
elif grade >= 70:
    print("You got a C")
elif grade >= 60:
    print("You got a D")
elif grade >= 50:
    print("You got an E")
else:
    print("You got an F")