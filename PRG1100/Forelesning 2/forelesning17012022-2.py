talliste=[5,3,1,2,4]

for index in range(0,(len(talliste)-1),1):
    print('Gjennomgang',index+1)
    print('Lista så langt', talliste)
    if talliste[0]>talliste[1]:
        bytte=talliste[0]
        talliste[0]=talliste[1]
        talliste[1]=bytte
        

    if talliste[1]>talliste[2]:
        bytte=talliste[1]
        talliste[1]=talliste[2]
        talliste[2]=bytte
        

    if talliste[2]>talliste[3]:
        bytte=talliste[2]
        talliste[2]=talliste[3]
        talliste[3]=bytte
        

    if talliste[3]>talliste[4]:
        bytte=talliste[3]
        talliste[3]=talliste[4]
        talliste[4]=bytte
        
        
print('Ferdig liste',talliste)
