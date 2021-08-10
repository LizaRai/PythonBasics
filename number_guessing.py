import random as rd
ran = rd.randint(0,100)
name = input("Enter you full name- ")
print ("Welcome to number guessing, Good Luck!!")

num_of_chances = 8


def checkOddEven (number):
    if (number % 2 == 0 ):
        print("\nHint =" + " " +"The number is even")
    else:
        print("\nHint =" + " " +"The correct number is odd")

def checkdiv (number):
    if (number % 3 == 0 and number % 5 == 0):
        print("\nHint =" + " " +"Number is divisible by 3 and 5")
    else:
        print("\nHint =" + " " +"Number is not divisible by both 3 and 5")

def checkhalf (number):
    if (number<50):
        print ("\nHint =" + " " +"The number is smaller than 50")
    else:
        print("\nHint =" + " " +"The number is greater than 50")

hints = [checkOddEven, checkdiv, checkhalf]

num = len(hints)- 1

def gethint(number):
    global num
    global hints
    if (num>=0):
        hints[num](number)
        num -= 1
    else:
        num = len(hints)-1
        hints[num](number)
        num -= 1

while num_of_chances>=1:
    user = int(input("\nEnter a number between 0 to 100: "))

    if (ran!=user):
        gethint(ran)
        num_of_chances -=1
        print("you have", num_of_chances,"chances left")
    else:
        print ("CONGRATS!!!! YOUR CORRECT ANSWER IS",ran)
        break

