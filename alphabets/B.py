def printB(size = 2):
    for y in range(0,size * 5):
        for x in range(0,size * 3):
            if((x > size - 1 and x < size * 2) and
                ((y > size - 1 and y < size * 2) or (y > size * 3 - 1 and y < size * 4))):
                print(' ', end = '')
            elif (x == size * 3 - 1 and (y == 0 or y == size * 5 - 1)):
                print(' ', end = '')
            else:
                print('*', end = '')
        print()