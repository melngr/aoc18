# day05.py
# Griffin Melnick, melnick DOT griffin AT gmail DOT com

import os
import sys

a_ans = None
b_ans = None

def react( polymer, reacts ):
    reactive = True
    while reactive:
        for unit in reacts:
            polymer = polymer.replace( unit, '' )

        for unit in reacts:
            if ( unit in polymer ):
                reactive = True
                break
            else:
                reactive = False

    return len(polymer)


def sol():
    global a_ans, b_ans
    f = open( os.path.join( os.path.dirname(__file__), "../inputs/day05.txt" ), 'r' )
    polymer = [ l.strip() for l in f.readlines() ][0]
    f.close()

    # part a
    reacts = set( "{}{}".format( chr(c).lower(), chr(c).upper() ) for c in range(97, 123) )
    reacts.update( set( "{}{}".format( chr(c).upper(), chr(c).lower() ) for c in range(97, 123) ) )

    a_ans = react( polymer, reacts )


    # part b
    replaced_lens = { chr(c): react( polymer.replace( chr(c).lower(), '' ).replace( chr(c).upper(), '' ), reacts )
            for c in range(97, 123) }
    _, b_ans = min( replaced_lens.items(), key=lambda x: x[1] )

    return "Day 5 --> a: {}, b: {}".format(a_ans, b_ans)


''' ------------------------------------------------------------------------ '''

def main():
    print( sol() )
    sys.exit()


''' ------------------------------------------------------------------------ '''

if ( __name__ == "__main__" ):
    main()

