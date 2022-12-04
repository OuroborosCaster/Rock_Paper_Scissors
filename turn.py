import random


def inputSRP():
    while True:
        a = input('Enter your option: ')
        match a:
            case 'S' | 's':
                return 1
            case 'R' | 'r':
                return 2
            case 'P' | 'p':
                return 3
            case _:
                print('Read rules above please!')


def judge(p, m):
    match p:
        case 1:
            if m == 1:
                status = 0
            elif m == 2:
                status = -1
            else:
                status = 1
        case 2:
            if m == 1:
                status = 1
            elif m == 2:
                status = 0
            else:
                status = -1
        case 3:
            if m == 1:
                status = -1
            elif m == 2:
                status = 1
            else:
                status = 0
    return status


def turn():
    draw = True
    while draw:
        # noinspection PyPep8Naming
        dictSRP = {1: '✌️', 2: '✊', 3: '✋'}
        m = random.randint(1, 3)
        p = inputSRP()
        status = judge(p, m)

        print('''
        Player|Machine
            %s|%s
        ''' % (dictSRP[p], dictSRP[m]))
        match status:
            case -1:
                print('You lose this turn.')
                return 0
            case 0:
                print("Draw turn doesn't count, try again.")
            case 1:
                print('You win this turn.')
                return 1
