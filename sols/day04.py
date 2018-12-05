# day04.py
# Griffin Melnick, melnick DOT griffin AT gmail DOT com

from collections import defaultdict as ddict
import operator
import os
import re
import sys

a_ans = None
b_ans = None

# sol() allows for summarized solutions
def sol():
    f = open( os.path.join( os.path.dirname(__file__), "../inputs/day04.txt" ), 'r' )
    notes = sorted( [ tuple( int(d) if d.isdigit() else d for d in re.findall(r"\w+", l) )
            for l in f.readlines() ], key=lambda x: (x[0], x[1], x[2], x[3], x[4]) )
    f.close()

    minutes = ddict(list)

    # part a
    guard_ids, guard_id, fell_asleep = set(), None, None
    for stamp in notes:
        if ( stamp[5] == "Guard" ):
            guard_id = stamp[6]
            guard_ids.add(guard_id)

        elif ( stamp[5] == "falls" ):
            fell_asleep = stamp[4]

        elif ( stamp[5] == "wakes" ):
            for m in range( fell_asleep, stamp[4] ):
                minutes[m].append(guard_id)

    all_asleep = []
    for key, val in minutes.items():
        all_asleep.extend(val)
    times_asleep = { g_id: all_asleep.count(g_id) for g_id in guard_ids }

    laziest = max( times_asleep.items(), key=operator.itemgetter(1) )[0]

    laziest_asleep = ddict(int)
    for key, val in minutes.items():
        laziest_asleep[key] = val.count(laziest)

    a_ans = laziest * max( laziest_asleep.items(), key=operator.itemgetter(1) )[0]


    # part b
    all_times_asleep = [ ( g_id, key, val.count(g_id) ) for key, val in minutes.items()
            for g_id in guard_ids ]

    guard_id, minute, count = None, None, 0
    for (g_id, m, c) in all_times_asleep:
        if ( c > count ):
            guard_id = g_id
            minute = m
            count = c

    b_ans = guard_id * minute


    return "Day 4 --> a: {}, b: {}".format(a_ans, b_ans)


''' ------------------------------------------------------------------------ '''

def main():
    print( sol() )
    sys.exit()


''' ------------------------------------------------------------------------ '''

if ( __name__ == "__main__" ):
    main()

