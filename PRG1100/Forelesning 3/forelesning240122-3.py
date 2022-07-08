usortert=[5,3,1,2,4,7,6]
print('Liste før sortering:',usortert)
for gjennomgang in range(0,len(usortert)-1,1):
    print('Gjennomgang nr:',gjennomgang+1,'starter')
    for sjekk in range(0,len(usortert)-1,1):
        print('Sammenligning nr',sjekk+1,'dvs',usortert[sjekk],'mot',usortert[1+sjekk])
        if usortert[sjekk]>usortert[1+sjekk]:
            print('Dette må byttes')
            bytte=usortert[sjekk]
            usortert[sjekk]=usortert[1+sjekk]
            usortert[1+sjekk]=bytte
            print('Lista så langt:',usortert)

print('Den sorterte lista er:',usortert)
