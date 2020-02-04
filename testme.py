from random import randint
import math

def inputChar():

    number = randint(1, 1000000)*randint(1, 1000000)
    root = 1/randint(2, 5)
    if(math.pow(number, root) - math.floor(math.pow(number, root)) == 0):
        print(f"This number {number} is a perfect {1/root} power")
        return ''
    else:
        while(number>127):
            number = number//randint(2, 10)
            while(number < 32):
                number *= randint(2, 10)

        return chr(number)


def inputString():
    #TODO: rewrite this function
    return ""


def testme():
    tcCount = 0
    state = 0
    while (True):
        tcCount += 1
        c = inputChar()
        s = inputString()
        print("Iteration {0}: c = {1}, s = {2}, state = {3}\n" .format(tcCount, c, s, state))

        if (c == '[' and state == 0):
            state = 1
        if (c == '(' and state == 1):
            state = 2
        if (c == '' and state == 2):
            state = 3
        if (c == ' ' and state == 3):
            state = 4
        if (c == 'a' and state == 4):
            state = 5
        if (c == 'x' and state == 5):
            state = 6
        if (c == '' and state == 6):
            state = 7
        if (c == ')' and state == 7):
            state = 8
        if (c == ']' and state == 8):
            state = 9
        if (state == 9):
            print("error ")
            break


def main():
    testme()


if __name__ == '__main__':
    main()


