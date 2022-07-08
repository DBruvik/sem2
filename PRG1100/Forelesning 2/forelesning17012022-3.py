talliste=[5,4,3,2,1]

for index in range(0,(len(talliste)-1),1):
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
        
