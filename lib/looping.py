#!/usr/bin/env python3
def happy_new_year():
    # code goes here!
    num =10
    while num >= 1:
        print(f"{num}")
        num -=1
        if num < 1:
            print("Happy New Year!")
            return "Happy New Year!"
happy_new_year()
pass
def square_integers(int_list):
    square_list = []  # Initialize an empty list to store squared integers
    for integer in int_list:
        square = integer * integer  # Calculate the square of each integer
        square_list.append(square)  # Append the squared value to the list
    return square_list  # Return the list of squared integers

# Example usage:
result = square_integers([1, 2, 3, 4, 5])
print(result)  # Output: [1, 4, 9, 16, 25]

pass

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz()


pass


