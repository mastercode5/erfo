import random
gracze =[ 'a','b','c','d','e','o','f','d','g','p']
def genTeam(lista):
    random.shuffle(lista)
    p = len(lista) // 2
    team1 = lista [ 0 :  p]
    team2 = lista [ p : ]
    return team1,team2
(1,2)[0]
a=genTeam( [1,2,3,4,5,6,7,8,9])
print(a[0])
print(a[1])