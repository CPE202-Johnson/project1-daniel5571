#input is integer and output is either True or False (boolean)
#tests to see if integer will pass the bears game
def bears(n):
    string = str(n)   #turns n into string so can access last two elements later on
    if n == 42:        #goal
        #print('first')
        return True
    if n < 42:        #no longer able to achieve goal
        #print('second')
        return False
    if n % 5 == 0:
        if bears(n-42):
            #print('third')
            return True
    if n % 2 == 0:
        if bears(n//2):
            #print('fourth')
            return True
    if n % 3 == 0 or n % 4 == 0:
        product = int(string[-2]) * int(string[-1])
        if product == 0:
            #print('fifth')
            return False
        elif bears(n - product):
            #print('sixth')
            return True
    else:
        #print('seventh')
        return False

print(bears(60))

