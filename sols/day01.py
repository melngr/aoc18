# day01.py
# Griffin Melnick, melnick DOT griffin AT gmail DOT com

import os
import sys

a_ans = None
b_ans = None

def sol():
    global a_ans, b_ans
    f = open( os.path.join( os.path.dirname(__file__), "../inputs/day01.txt" ), 'r' )
    vals = [ int(l) for l in f.readlines() ]

    # part a
    a_ans = sum(vals)


    # part b
    freq, i, = 0, 0
    freqs = set( [0] )
    while b_ans == None:
        freq += vals[i]
        if ( freq in freqs ):
            b_ans = freq
        else:
            freqs.add(freq)
        i = (i + 1) % len(vals)

    return "Day 1 --> a: {}, b: {}".format(a_ans, b_ans)


''' ------------------------------------------------------------------------ '''

def main():
    print( sol() )
    sys.exit()


''' ------------------------------------------------------------------------ '''

if ( __name__ == "__main__" ):
    main()

