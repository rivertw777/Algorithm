from itertools import product

def solution(word):
    alphabets = ['A', 'E', 'I', 'O', 'U', '']
    getAll = product(alphabets, repeat=5)
    
    temp = set()
    for i in getAll:
        temp.add( ''.join(i) )
    temp.remove('')

    temp = list(temp)
    temp.sort()
    
    return temp.index(word) + 1