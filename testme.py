
def inputChar():
    #TODO: rewrite this function
    return ' '


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
        print("Iteration %d: c = %c, s = %s, state = %d\n" % (tcCount, c, s, state))

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
        if (s == "reset" and state == 9):
            print("error ")
            break

def main():
    testme()


if __name__ == '__main__':
    main()


