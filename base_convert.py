#input is number and base, output is string consisting of numbers
#takes a number and does a base conversion
def convert(num, b):
    print(num)
    newstring = ''
    if num // b == 0:        #base case
        if num % b < 10:
            return newstring + str(num % b)                           #add remainder to string
        else:
            if num % b == 10:
                return newstring + 'A'
            elif num % b == 11:
                return newstring + 'B'
            elif num % b == 12:
                return newstring + 'C'
            elif num % b == 13:
                return newstring + 'D'
            elif num % b == 14:
                return newstring + 'E'
            elif num % b == 15:
                return newstring + 'F'
    quotient = num // b
    remainder = num % b
    if remainder == 10:
        remainder = 'A'
    elif remainder == 11:
        remainder = 'B'
    elif remainder == 12:
        remainder = 'C'
    elif remainder == 13:
        remainder = 'D'
    elif remainder == 14:
        remainder = 'E'
    elif remainder == 15:
        remainder = 'F'
    newstring = newstring + str(remainder)
    return convert(quotient, b) + newstring
