# How to solve a problem:
    # Figure out what the input and its type are
    # Set up a function
    # Figure out what the output and its type are
    # Gather Your Knowledge
    # Gathers Your Constraints (Not always necessary) 
    # Determine a Logical way to solve the problem
        #Write each step out English
        #Write each step out in Python-esse (sudo-code)
    # Invoke and Test Your Function


# FizzBuzz Coding Challenge 🌟

# Objective:
# Your task is to implement a Python function called fizzbuzz that takes a positive integer as an argument and returns a string based on specific conditions. This is a well-known coding problem that assesses basic control flow and logical reasoning skills.

# Requirements:
# Function Name: fizzbuzz
# Input: A single positive integer.
# Output: A string that adheres to the following conditions:
# If the input integer is divisible by both 3 and 5, return "FizzBuzz".
# If the input integer is divisible by 3 but not 5, return "Fizz".
# If the input integer is divisible by 5 but not 3, return "Buzz".
# If the input integer is neither divisible by 3 nor 5, return the integer as a string.


'''
function = fizzbuzz
input: positive integer -> maybe put in a condition to account for negative numbers
output: returns a string based on conditions
if int is divisible by 3 AND 5, return FizzBuzz -> seems maybe written out what it needs to do for constraint already?
if int is divisible by 3 but not 5, return Fizz
if int is divisible by 5 but not 3 return Buzz
if neither is divisible, then return the integer as a string
'''

def fizzbuzz(number):
    if number < 0:
        number *= -1
        print(f'Negative number encountered: -{number}\nConverted to positive: {number}\nRunning fizzbuzz again')
        return fizzbuzz(number)
    else:
        if number % 3 == 0 and number % 5 == 0:
            return 'FizzBuzz'
        elif number % 3 == 0 and number % 5 != 0:
            return 'Fizz'
        elif number % 3 != 0 and number % 5 == 0:
            return 'Buzz'
        else:
            return str(number)
        
def fizzbuzz2(number):
    if number % 3 == 0 and number % 5 == 0:
        return 'FizzBuzz'
    elif number % 3 == 0 and number % 5 != 0:
        return 'Fizz'
    elif number % 3 != 0 and number % 5 == 0:
        return 'Buzz'
    else:
        return str(number)


# this keeps the test file from also printing any of the prints but allows it to show up when you run this file
if __name__ == '__main__':  
    print(fizzbuzz(10))
    print(fizzbuzz(3))
    print(fizzbuzz(5))
    print(fizzbuzz(7))
    print(fizzbuzz(-15))
    print(fizzbuzz2(-45))

