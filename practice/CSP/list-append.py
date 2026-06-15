grades = [2.8, 3.9, 3.5, 4.0, 3.1, 3.7, 2.5]
honor_roll = []
for grade in grades:
  if grade>=3.5:
    honor_roll.append(f"\n {grade}")

print("Final honor roll list:", honor_roll)
