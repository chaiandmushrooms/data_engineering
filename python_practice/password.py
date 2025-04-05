# Ask for a password
password = input("Enter your password: ").strip()

# variables to store the number of lowercase characters, uppercase characters, special characters, numbers
lc_count, uc_count, sc_count, num = 0, 0, 0, 0

for ch in password:
    if ch.islower():
        lc_count += 1
    elif ch.isupper():
        uc_count += 1
    elif ch.isdigit():
        num += 1
    else:
        sc_count += 1

if len(password) == 0:
    print("try again!")
elif len(password) < 8:
    print("weak")
elif sc_count < 2 or num < 2 or uc_count < 2 or lc_count < 2:
    print("moderate")
else:
    print("strong")