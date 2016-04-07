#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function)

import sympy
from chempy.debye_huckel import limiting_log_gamma as g
from math import exp

def main(conc=7e-3):
    # 2 Fe+3 + 2H2O  =  Fe2OH2+4 + 2H+      log10(beta) = -2.81
    #    y      1            x     .01
    #
    # (conc - x) =  [Fe+3] + [FeOH+2]
    # (conc - x) =  y(1 + 10**(pH - 2.774))
    # y = (conc - x)/(1 + 10**-.774)
    #
    x = sympy.Symbol('x')
    eq = sympy.Eq(x*1e-4*(1 + 10**-.774)**2 / (conc - x)**2, 10**-2.81)
    for sol in sympy.solve(eq, x):
        if sol > conc or sol < 0:
            continue
        return sol
    else:
        raise ValueError("No solution")


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
