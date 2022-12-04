import turn


# noinspection PyShadowingBuiltins
def round():
    point = 0
    for i in range(1, 4):
        print('Turn %d' % i)
        point += turn.turn()
    if point >= 2:
        print('You win %d turns, so you win this round!' %point)
        return 1
    else:
        print('Machine win %d turns, so you lose this round!' %(3-point))
        return -1
