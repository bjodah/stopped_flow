#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function)

from chempy.debye_huckel import limiting_log_gamma as g

def main(I=0.05):
    A = 0.510
    return 10**(6*A*I**0.5)
    #return 10**(g(I, 2, A) - g(I, 3, A) - g(I, -1, A))


if __name__ == '__main__':
    try:
        import argh
        argh.dispatch_command(main)
    except ImportError:
        import sys
        if len(sys.argv) > 1:
            print("Unable to process parameters, argh missing. "
                  "Run 'pip install --user argh' to fix.", file=sys.stderr)
            sys.exit(os.EX_USAGE)  # non-ok exit
        print(main())
