import time
import math
from termcolor import colored, cprint


def inputs():
    num = int(input("Integer: "))
    exp = int(input("Exponent: "))
    mod = int(input("Mod: "))

    n = num
    e = exp
    m = mod

    #basic(n,e,m)
    squareMult(n,e,m)

def loops():
    print("Would you like to try again? Y/N")

    user_input = (input())

    if user_input == "y":
        inputs()
    elif user_input == 'n':
        return
        

def basic(n,e,m):
    start = time.time()

    ex = ((n ** e) % m)

    cprint("The answer is: %s" % ex, 'yellow')

    end = time.time()

    total_time = end - start
    cprint("Time in seconds to calculate: " + str(total_time) + "\n", 'green')

def squareMult(n,e,m):
    start2 = time.time()

    expBin = "{0:b}".format(e)

    loop = 1
    steps = len(expBin)
    ooo = []

    while loop <= (steps - 1) :
        if expBin[loop] == "1":
            ooo.append("S")
            ooo.append("M")
            loop += 1
        elif expBin[loop] == "0":
            ooo.append("S")
            loop += 1
    print("Exponent in binary: %s" % expBin)
    print("Order of Operations: ", '%s' % ', '.join(map(str, ooo)))

    val = n

    for operation in ooo:
        if operation == "S" :
            val = ((val * val) % m)
        elif operation == "M" :
            val = ((val * n) % m)
    cprint("The answer is: %s" % val, 'yellow')

            
    end2 = time.time()

    total_time2 = end2 - start2
    cprint("Time in seconds to calculate: " + str(total_time2) + "\n", 'green')

    loops()

cprint('*****************************************************************************', 'green')
cprint('***  Square Multiply vs basic maths script | https://github.com/jibatsu   ***', 'green')
cprint('*****************************************************************************', 'green')

cprint('This script will calculate the forumla ((x^y) mod n) e.g. ((3^45) mod 7).\nIt will do so by using normal "Python maths" i.e. simply typing the formula into Python and letting it calculate the result.\nIt will then calculate using the Sqaure Multiply method. You can then compare the results of both methods.\nThe answers should be the same but the time taken should be drastically shorter for the Square Multiply method.\nFor more infomation watch this Computerphile video here: https://www.youtube.com/watch?v=cbGB__V8MNk', 'green')
inputs()