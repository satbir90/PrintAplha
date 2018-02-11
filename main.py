import sys
from alphabets import A
from alphabets import B
from alphabets import C

def checkAlphabet(alpha, size):
    if (alpha.upper() == 'A'):
        A.printA(size)
        pass
    elif (alpha.upper() == 'B'):
        B.printB(size)
        pass
    elif (alpha.upper() == 'C'):
        C.printC(size)
        pass

def main():
    # for arg in sys.argv[1:]:
    #     print(arg)
    alphabet = ''
    size = 0
    if(len(sys.argv) > 2):
        alphabet = sys.argv[1]
        size = int(sys.argv[2])
    elif(len(sys.argv) > 1):
        alphabet = sys.argv[1:][0]
        size = int(input('What should the size be?'))
    else:
        alphabet = input('Which alphabet would you like to print?')
        size = int(input('What should the size be?'))
    
    if (len(alphabet) > 1):
        print('Please enter only one alphabet')
    elif (not alphabet.isalpha()):
        print('Please anter alphabet only')
    else:
        checkAlphabet(alphabet, size)

if __name__ == "__main__":
    main()