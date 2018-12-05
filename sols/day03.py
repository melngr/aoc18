# day03.py
# Griffin Melnick, melnick DOT griffin AT gmail DOT com

from collections import defaultdict as ddict
import os
import re
import sys

a_ans = None
b_ans = None

def sol():
    global a_ans, b_ans
    f = open( os.path.join( os.path.dirname(__file__), "../inputs/day03.txt" ), 'r' )
    claims = [ tuple( int(d) for d in re.findall(r"\d+", l) ) for l in f.readlines() ]
    f.close()

    claimed = ddict( set )

    # part a
    for (claim_id, x, y, w, h) in claims:
        for t in [ (x1, y1) for y1 in range(y, (y + h)) for x1 in range(x, (x + w)) ]:
            claimed[t].add(claim_id)
    a_ans = len( [key for key, val in claimed.items() if len(val) > 1] )


    # part b
    ids = set( c[0] for c in claims )
    for key, val in claimed.items():
        if ( len(val) > 1 ):
            ids -= val
    b_ans = list(ids)[0]

    return "Day 3 --> a: {}, b: {}".format(a_ans, b_ans)


''' ------------------------------------------------------------------------ '''

def main():
    print( sol() )
    sys.exit()


''' ------------------------------------------------------------------------ '''

if ( __name__ == "__main__" ):
    main()

