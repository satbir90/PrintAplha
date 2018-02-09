def printA(size = 2):
    for y in range(0,size * 4):
        for x in range(0,size * 3):
            if((x > size - 1 and x < size * 2) and ((y > size - 1 and y < size * 2) or y > size * 2 + 1)):
                print(' ', end = '')
            else:
                print('*', end = '')
        print()