import math

def reverse_string(text):
    """
        reverses a string and returns the result.
        reverse_string (string): ----> string
    """
    width = len(text)
    return "".join(text[i] for i in range (width - 1, -1, -1))

def factorial(number):
    '''
        returns factorial of a number.
        factorial(int) ----> int
    '''
    return math.prod(num for num in range (1, number + 1)) if number > 0 else 1

def palindrome(word):
    '''
        returns a boolean value after checking if the given string is a palindrome
        palindrome(string) -----> string
    '''
    width = len(word)

    for i in range (width // 2):
        if word[i].upper() != word[width - i - 1].upper():
            return False
    return True

def print_even(number):
    '''
        returns an array containing even number starting from 2 till the number passed in
        print_even(int) -----> int
    '''
    return [x for x in range(2, number + 1, 2)]

def largest (x, y, z):
    '''
        returns the largest integer among the integers passed in
        largest(int, int, int) -----> int
    '''
    return int(x if x > y > z else y if y >= x >= z else z)

def mean(data):
    '''
        returns mean of the elements in the list
        mean(list) -----> float
    '''
    return (sum(x for x in data) / len(data))

def median(data):
    """
        Returns the median value of the list.
        median(list) -----> int
    """
    temp_data = sorted(data)
    length = len(temp_data)
    mid = length // 2

    if length % 2 == 0:
        return (temp_data[mid - 1] + temp_data[mid]) / 2
    else:
        return temp_data[mid]

def mode(data):
    '''
        returns mode for the elements in the list passed
        mode(list) -----> int
    '''
    counts = {}
    for x in data:
        counts[x] = counts.get(x, 0) + 1
    return max(counts, key = counts.get)

def main():
    print("all good here \\o/")

if __name__ == "__main__":
    main()