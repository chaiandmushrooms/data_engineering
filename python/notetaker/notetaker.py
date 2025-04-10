with open('notes.txt', 'a') as notes:
    notes.write(input("Enter your note: ").strip() + "\n")