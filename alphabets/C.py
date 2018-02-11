def printC(size = 2):
    for y in range(0,size * 3):
        for x in range(0,size * 3):
            if((x > size - 1) and y > size - 1 and y < size * 2):
                print(' ', end = '')
            else:
                print('*', end = '')
        print()