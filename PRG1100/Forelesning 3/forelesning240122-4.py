bytte=True
usortert=[5, 3, 1, 2, 4, 7, 6] 
j=1
print('Start på WHILE-løkka')
while bytte:
    bytte=False
    print('Gjennomgang starter')
    print('Start for FOR-løkka')
    for sjekk in range(0,len(usortert)-j,1):
        if usortert[sjekk]>usortert[sjekk+1]:
            bytte=usortert[sjekk]
            usortert[sjekk]=usortert[sjekk+1]
            usortert[sjekk+1]=bytte
            print('Tabell etter hver bytte innen en gjennomgang',usortert)
    j=j+1
    print('Slutt for FOR-løkka')
print('Slutt på WHILE-løkka')
print(usortert)
