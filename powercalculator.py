a = int(input("Enter the  number: "))
b = int(input("Enter the exponent: "))

i = 1
for _ in range(b):
  i *= a

print("the power is: ",(i))