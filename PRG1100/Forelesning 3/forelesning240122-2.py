talliste=[5, 3, 1, 2, 4, 7, 6]

for index in range(0,1,1):
    print('Gjennomgang',index+1)
    if talliste[0]>talliste[1]:
        bytte=talliste[0]
        talliste[0]=talliste[1]
        talliste[1]=bytte
        print('Lista så langt', talliste)

    if talliste[1]>talliste[2]:
        bytte=talliste[1]
        talliste[1]=talliste[2]
        talliste[2]=bytte
        print('Lista så langt', talliste)

    if talliste[2]>talliste[3]:
        bytte=talliste[2]
        talliste[2]=talliste[3]
        talliste[3]=bytte
        print('Lista så langt', talliste)

    if talliste[3]>talliste[4]:
        bytte=talliste[3]
        talliste[3]=talliste[4]
        talliste[4]=bytte
        print('Lista så langt', talliste)

    if talliste[4]>talliste[5]:
        bytte=talliste[4]
        talliste[4]=talliste[5]
        talliste[5]=bytte
        print('Lista så langt', talliste)
        
    if talliste[5]>talliste[6]:
        bytte=talliste[5]
        talliste[5]=talliste[6]
        talliste[6]=bytte
        print('Lista så langt', talliste)
        
        
