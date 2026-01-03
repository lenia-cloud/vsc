count = int(input("Pick any positive number. "))
#requires the user to enter a number that is stored in a variable
while count >= 0:
  print(count)
  count = count - 1
print("Blast off!")



even_sum = 0
odd_sum = 0
for i in range(1, 21, 2): #odd numbers from 1 to 21
  odd_sum = odd_sum + i
print(odd_sum)

for i in range(2, 21, 2):
  even_sum = even_sum + i
print(even_sum)

