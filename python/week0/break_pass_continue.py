arr = []
while (True):
    placeholder = (input("Give me your input please: ")).strip()
    if (placeholder == 'exit'):
        break
    elif (placeholder == "" or placeholder == " "):
        pass
    elif (placeholder[0] == '#'):
        continue
    else:
        arr.append(placeholder)
print(arr)