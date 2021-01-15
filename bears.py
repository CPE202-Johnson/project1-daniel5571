#input is integer and output is either True or False (boolean)
#tests to see if integer will pass the bears game
def bears(n):
    string = str(n)   #turns n into string so can access last two elements later on
    if n == 42:        #goal
        return True
    elif n < 42:        #no longer able to achieve goal
        return False
    elif n / 2 == 42:      #good
        return True
    elif n % 3 == 0 and n - (int(string[-2]) * int(string[-1])) == 42:          #good
        return True
    elif n % 4 == 0 and n - (int(string[-2]) * int(string[-1])) == 42:         #good
        return True
    elif n % 5 == 0:
        return bears(n - 42)            #recursive call
    elif n % 2 == 0:
        return bears(int(n / 2))    #recursive call and keeps n as an int instead of a float
    elif n % 3 == 0:
        return bears(n - (int(string[-2]) * int(string[-1])))          #recursive call
    elif n % 4 == 0:
        return bears(n - (int(string[-2]) * int(string[-1])))           #recursive call
    else:
        return False                      #all else fails



print(bears(250))
