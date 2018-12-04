# sols.py
# Griffin Melnick, melnick DOT griffin AT gmail DOT com

import importlib
import sys

def main():
    for i in range(1, 26):
        try:
            day = importlib.import_module( ".day{:02}".format(i), "sols" )
            print( day.sol() )
        except:
            break

    sys.exit()


''' ------------------------------------------------------------------------ '''

if ( __name__ == "__main__" ):
    main()
