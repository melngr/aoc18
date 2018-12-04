# day02.py
# Griffin Melnick, melnick DOT griffin AT gmail DOT com

import os
import sys

a_ans = None
b_ans = None

def diff_by_one( l, r ):
    count_diff, ind = 0, None
    for i in range( len(l) ):
        if ( l[i] != r[i] ):
            count_diff += 1
            ind = i
    if ( count_diff == 1 ):
        return ( l[: ind] + l[(ind + 1) :] )


def sol():
    global a_ans, b_ans
    f = open( os.path.join( os.path.dirname(__file__), "../inputs/day02.txt" ), 'r' )
    strs = [ s.strip() for s in f.readlines() ]

    # part a
    two, three = 0, 0
    for s in strs:
        chars = set(s)
        has_two, has_three = False, False
        for char in chars:
            if ( ( s.count(char) == 2 ) and not has_two ):
                two += 1
                has_two = True
            if ( ( s.count(char) == 3 ) and not has_three ):
                three += 1
                has_three = False

    a_ans = two * three


    # part b
    for i in range( len(strs) ):
        for j in range( (i + 1), len(strs) ):
            diff = diff_by_one( strs[i], strs[j] )
            if ( diff != None ):
                b_ans = diff
                break

    return "Day 2 --> a: {}, b: {}".format(a_ans, b_ans)


''' ------------------------------------------------------------------------ '''

def main():
    print( sol() )
    sys.exit()


''' ------------------------------------------------------------------------ '''

if ( __name__ == "__main__" ):
    main()

