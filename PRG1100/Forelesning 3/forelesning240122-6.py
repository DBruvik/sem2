usortert=[5, 3, 1, 2, 4]
print(usortert)
for sjekk in range(1,len(usortert),1):
    x=usortert[sjekk]
    j=sjekk-1
    print('Vi jobber med kort nr',sjekk+1,'i lista over')
    print('Det har verdi',usortert[sjekk])
    print('"Kortet tas ut"')
    while j>=0 and usortert[j]>x:
        usortert[j+1]=usortert[j]
        j=j-1
    print('Og',sjekk-j-1,'"kort" foran flyttes til høyre før "kortet" settes inn')
    print(x,sjekk,j)
    usortert[j+1]=x
    print('Resultatet er så langt:', usortert)
    
print(usortert,'slutt test')
