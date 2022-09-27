# creator jmchale 9/27/22
while True:
    points = int(input('Enter amount of points:\n'))

    if points >= 15:
        print('you win a gold medal!')
    else:
        if points > 11:
            print('you win a silver medal')
        else:
            if points > 8:
                print('you win a bronze')
            else:
                print('you arent a winner')