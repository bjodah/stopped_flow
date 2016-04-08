#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function)

import sympy
from chempy.debye_huckel import limiting_log_gamma as g
from math import exp

def main(conc=7e-3, pH=2.0, beta_a=-2.774, beta_b=-2.81):
    #   Fe³⁺ + H₂O   =  FeOH²⁺   +  H⁺      α₁ = log10(β₁) = -2.774
    #    y      1          z       10**-pH
    #
    #  10**-pH * z / y = 10**α₁       (1)
    #
    # 2 Fe³⁺ + 2H₂O  =  Fe₂OH₂⁴⁺ + 2H⁺      α₂ = log10(β₂) = -2.81
    #    y      1            x     10**-pH
    #
    #  x*10**-2*pH / y**2 = 10**α₂    (2)
    #
    # Total amount of Fe:
    #   conc =  [Fe³⁺] + [FeOH²⁺] + 2[Fe₂OH₂⁴⁺]
    #   conc = y + z + 2*x            (3)

    x, z = sympy.symbols('x z')
    y = 10**-pH * z / 10**beta_a
    eq2 = x*10**-2*pH / y**2 - 10**beta_b
    eq3 = y + z + 2*x - conc

    print(eq2)
    print(eq3)

    for sol in sympy.solve([eq2, eq3], x):
        if sol > conc/2 or sol < 0:
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
