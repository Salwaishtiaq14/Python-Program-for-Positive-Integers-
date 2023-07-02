

# Description of the program
"""
The user enters a positive integer number larger than 9 into this Python application, and it then performs different number operations. 
These operations involve calculating currency, age calculations, separating digits, calculating the sum of digits, and creating a unique sequence of distinct numbers. 
The program outputs the findings of these computations together with the creator's name and the date of installation.
"""

# (1) Currency Calculation
def currencyCalculation(penny):
    quarters = penny // 25 # quarters in pennies
    penny = penny % 25 # pennies in pennies
    dimes = penny // 10 # dimes in pennies
    penny = penny % 10 # pennies in pennies
    nickels = penny // 5 # nickels in pennies
    penny = penny % 5 # pennies in pennies
    print("\nCurrency Calculation \n{} cent/s is equivalent to: \n".format(penny + 5*nickels + 10*dimes + 25*quarters))
    print("{} quarter/s \n{} dime/s \n{} nickel/s \n{} cent/s \n\n ".format(quarters, dimes, nickels, penny))

# (2) Person Age
def personAge(personAge):
    months = personAge * 12 # months in year
    days = personAge * 365 # days in year
    hours = days * 24 # hours in year
    minutes = hours * 60 # minutes in year
    seconds = minutes * 60 # seconds in year
    print("Age Calculation \n\nAssuming that you are {} years old , then\n".format(personAge))
    print("You are {} months old".format(months))
    print("You are {} days old".format(days))
    print("You are approximately {} hours old".format(hours))
    print("You are approximately {} minutes old".format(minutes))
    print("You are approximately {} seconds old \n\n".format(seconds))

# (3) Separation of numbers
def separationOfNumbers(num):
    digits = list(str(num))
    print("Separating digits for the integer {}".format(num))
    print(" ".join(digits))
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"] # digits in english
    print(" ".join([words[int(digit)] for digit in digits]), "\n\n")

# (4) Sum of digits numbers
def sumOfDigits(digitsNumber):
    sumOfDigits = [int(digits) for digits in str(digitsNumber)]
    return sum(sumOfDigits) # return the result back to main  script

# Distinct Sequence
def distinctSequence(n):
    distinctSequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        distinctSequence.append(n)
    print("The sequence of distinct numbers starting at {} is \n{}".format(distinctSequence[0], distinctSequence))
    

print("\nNumber Manipulations \n")
number = int(input("Enter a positive integer number greater than > 9 ---> ")) # positve value for number variable
if number < 0:
    print("\n\n*** Error --- invalid input", number)
    
    print("re-run the app & use a positive number > 0")
    
    # Footer for wrong input
    print("\n\nImplemented by Arslan Abbasi")
    print("April 10, 2023\n")
else:
    currencyCalculation(number)
    personAge(number)
    separationOfNumbers(number)
    print("Sum of its digits for the integer {} \n{} \n\n".format(number, sumOfDigits(number))) # print the returned result in the main script
    distinctSequence(number)
    
    # Footer for correct input
    print("\n\nImplemented by Arslan Abbasi")
    print("April 10 , 2023\n")