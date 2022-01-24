# Problem #1
# Create a calculator using functions that asks for two numbers and performs a calculation that the user inputs... Loop until the user chooses not to perform any more calculations.

def calculate(x,y):
    if x.isnumeric() == False or y.isnumeric == False or x == '' or y == '':
        print('It seems you have inputted something other than an integer. Please run script again.')
        return calculate(input("What is Number 1?"), input("What is number 2?"))
    elif x == "Stop" or y == "Stop":
        return "Calculator has been turned off."
    elif x.isnumeric() and y.isnumeric():
        print(int(x)*int(y))
        if x == "Stop" or y == "Stop":
            return "Calculator has been turned off."
        elif x.isnumeric() == False or y.isnumeric == False:
            print('It seems you have inputted something other than an integer. Please run script again.')
            return calculate(input("What is Number 1?"), input("What is number 2?"))
        else:
            if x.isnumeric() == False or y.isnumeric == False:
                print('It seems you have inputted something other than an integer. Please run script again.')
                calculate(input("What is Number 1?"), input("What is number 2?"))
            else:
                return calculate(input("What is Number 1?"), input("What is number 2?"))

calculate(input("What is Number 1?"),input("What is number 2?"))
# END




# Problem #2 
# Create a pyramid of X's for n number of levels.

indent = 0
def pyramid(total):
    rows = int(total)
    indent = rows
    for number in range(rows):
        indent += -1
        print((' '*indent) + number * 'X ')


pyramid(input('How many rows of X\'s would you like?'))

# END