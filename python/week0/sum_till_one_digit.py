num = input("Enter your desired num: ")
total = int(num)  # Start with total already defined

while int(num) > 9:
    total = 0
    total = sum(int(i) for i in num)
    num = str(total)

print(total)