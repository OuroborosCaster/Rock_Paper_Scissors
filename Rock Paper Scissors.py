import round

print('Welcome to play the "Rock Paper Scissors" game!')
print('You will play with this machine!')
print("Enter S/s for Scissors, enter R/r for Rock, enter P/p for paper, don't enter others.")
print("Every round you have 3 turns, and win 2 times you can be the  winner of this round.")
print('Now start!')

y = True
p = 0
m = 0
while y:
    r = round.round()
    match r:
        case -1:
            m += 1
        case 1:
            p += 1
    print('''Current wins:
        Player|Machine
             %d|%d''' %(p,m))
    c = input('One more time?(Y/y for yes, others for no): ')
    if c not in ['Y', 'y']:
        y = False
        print('Bye!')
