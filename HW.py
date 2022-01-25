# Problem #1
# Create a calculator using functions that asks for two numbers and performs a calculation that the user inputs... Loop until the user chooses not to perform any more calculations.

def calculate(x,y):
    if x == str('Stop') or y == str('Stop'):
        return "Calculator has been turned off."
    elif (x.isnumeric() == False and isinstance(float(x), float) == False) or (y.isnumeric() == False and isinstance(float(y), float) == False) or x == '' or y == '':
        print('It seems you have inputted something other than an number. Please run script again.')
        return calculate(input("What is Number 1? "), input("What is number 2? "))
    elif (x.isnumeric() or isinstance(float(x), float)) and (y.isnumeric() or isinstance(float(y), float)):
        print(float(x)*float(y))
        if x == str('Stop') or y == str('Stop'):
            return "Calculator has been turned off."
        elif (x.isnumeric() == False and isinstance(float(x), float) == False) or (y.isnumeric() == False and isinstance(float(y), float) == False) or x == '' or y == '':
            print('It seems you have inputted something other than an number. Please run script again.')
            return calculate(input("What is Number 1? "), input("What is number 2? "))
        else:
            if x == str('Stop') or y == str('Stop'):
                return "Calculator has been turned off."
            elif (x.isnumeric() == False and isinstance(float(x), float) == False) or (y.isnumeric() == False and isinstance(float(y), float) == False) or x == '' or y == '':
                print('It seems you have inputted something other than an number. Please run script again.')
                return calculate(input("What is Number 1? "), input("What is number 2? "))
            else:
                return calculate(input("What is Number 1? "), input("What is number 2? "))
    # elif isinstance(x, float) or isinstance(y, float)
    #     print()

calculate(input("What is Number 1? "),input("What is number 2? "))
# END

# print(isinstance(float(43),float))


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