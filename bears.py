#input is integer and output is either True or False (boolean)
#tests to see if integer will pass the bears game
def bears(n):
    print(n)
    string = str(n)   #turns n into string so can access last two elements later on
    if n == 42:        #goal
        print('first')
        return True
    elif n < 42:        #no longer able to achieve goal
        print('second')
        return False
    elif n / 2 == 42:      #good
        print('third')
        return True
    elif n % 3 == 0 and n - (int(string[-2]) * int(string[-1])) == 42:          #good
        print('fourth')
        return True
    elif n % 4 == 0 and n - (int(string[-2]) * int(string[-1])) == 42:         #good
        print('fifth')
        return True
    elif n % 5 == 0:
        print('sixth')
        return bears(n - 42)
    elif n % 2 == 0:
        print('seventh')
        return bears(int(n/2))
    elif n % 3 == 0 or n % 4 == 0:
        print('eighth')
        return bears(n - int(string[-2]) * int(string[-1]))
    else:
        print('ninth')
        return False

