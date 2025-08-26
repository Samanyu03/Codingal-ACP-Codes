num = int(input("Enter a number: "))

digit = 0
for i in num:
    # check manually if ch is between '0' and '9'
    for d in "0123456789":
        if i == d:
            digit += 1

print("Number of digits:", digit)