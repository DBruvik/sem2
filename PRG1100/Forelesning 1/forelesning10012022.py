def main():
    #Display the intro screen
    intro()
    #get the number of cups
    cupsNeeded=int(input('Enter the number of cups: '))
    #convert the cups to ounces.
    cupsToOunces(cupsNeeded)
    

#The intro function displays and introductory screen.
def intro():
    print('1')
    print('2')
    print('3')
    print('4')
    print('5')

def cupsToOunces(cups):
    ounces=cups*8
    print(f'That converts to {ounces} ounces.')

main()
