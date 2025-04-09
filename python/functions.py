import math

def reverse_string(text):
    """
        reverses a string and returns the result.

        Args:
            text (string): asdf.

        Returns:
            string: fdsa
    """
    width = len(text)
    return "".join(text[i] for i in range (width - 1, -1, -1))

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

def mean(data):
    return (sum(x for x in data) / len(data))

def median(data):
    temp_data = sorted(data)
    length = len(data)
    index = length // 2
    return temp_data[index] if length % 2 != 0 else (temp_data[index - 1] + temp_data[index]) / 2

def mode(data):
    counts = {}
    for x in data:
        counts[x] = counts.get(x, 0) + 1
    return max(counts, key = counts.get)

if __name__ == "__main__":
    main()