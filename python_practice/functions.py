import math

def factorial(number):
    return math.prod(num for num in range (1, number + 1)) if number > 0 else 1

def palindrome_check(word):
    width = len(word)

    for i in range (width // 2):
        if word[i].upper() != word[width - i - 1].upper():
            return False
    return True

def print_even(number):
    return [x for x in range(2, number + 1, 2)]

def largest_number (x, y, z):
    return int(x if x > y > z else y if y >= x >= z else z)

def main():
    print("all good here \\o/")

if __name__ == "__main__":
    main()