#input is string and output is list of strings
#to use the string to make a permuted list of strings in lexicographic order
def perm_gen_lex(a):
    newlist = []
    if a == '':
        return []
    elif len(a) == 1:
        return [a]
    else:
        for char in a:
            tempstring = a.replace(char, '')            #forms a simpler string
            for permutation in perm_gen_lex(tempstring):
                newlist.append(char + permutation)
    return newlist                        #adds permutation to list

print(perm_gen_lex('abc'))

