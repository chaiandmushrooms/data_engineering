num = input("Enter your desired num: ")
total = int(num)  # Start with total already defined

while int(num) > 9:
    total = 0
    for i in num:
        total += int(i)
    num = str(total)

print(total)