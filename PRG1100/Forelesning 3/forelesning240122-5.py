usortert=[5, 3, 1, 2, 4]
print(usortert)
for sjekk in range(1,len(usortert),1):
    j=sjekk
    print('Vi tar et "kort"')
    print('Kort nr',sjekk+1,'med verdi',usortert[j])
    while j>0 and usortert[j-1]>usortert[j]:
        bytte=usortert[j]
        usortert[j]=usortert[j-1]
        usortert[j-1]=bytte
        j=j-1
        print('Flyttes',sjekk-j,'ganger til venstre og resultatet blir',usortert)

print(usortert)
print('slutt')
