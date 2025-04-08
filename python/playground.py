# Write a function to count word frequency in a sentence using a dictionary

setence = (input("Enter your desired string: ").strip()).split(" ")
print(" ".join(setence))
frequency = {}
for word in setence:
    frequency[word] = frequency.get(word, 0) + 1

for key in frequency:
    print("{}, {}".format(key, frequency[key]))