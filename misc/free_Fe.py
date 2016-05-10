#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function)

from chempy.electrolytes import limiting_log_gamma as g
from math import exp

def main(pH=3.0):
    return 10**(2.774 - pH)


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
