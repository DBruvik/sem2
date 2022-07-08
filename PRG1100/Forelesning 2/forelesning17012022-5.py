usortert=[5,3,1,2,4]
print('Liste før sortering:',usortert)
for gjennomgang in range(0,len(usortert)-1,1):
    print('Gjennomgang nr:',gjennomgang+1)
    for sjekk in range(0,len(usortert)-1,1):
        if usortert[sjekk]>usortert[1+sjekk]:
            bytte=usortert[sjekk]
            usortert[sjekk]=usortert[1+sjekk]
            usortert[1+sjekk]=bytte
            print('Sjekk nr:',sjekk+1)
            print('Lista så langt:',usortert)

print('Den sorterte lista er:',usortert)


#MANTAS SPESIAL
