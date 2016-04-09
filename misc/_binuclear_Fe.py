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
    #  10**-pH * z / y = 10**α₁
    #  z = y*10**(pH + α₁)
    #
    # 2 Fe³⁺ + 2H₂O  =  Fe₂OH₂⁴⁺ + 2H⁺      α₂ log10(β₂) = -2.81
    #    y      1            x     10**-pH
    #
    #  x*10**(-2*pH) / y**2 = 10**α₂
    #  y**2 = x*10**(-2*pH-α₂)                                (1)
    #
    #
    # Total amount of Fe:
    #   conc =  [Fe³⁺] + [FeOH²⁺] + 2[Fe₂OH₂⁴⁺]
    #
    # Denote [Fe₂OH₂⁴⁺] with x and [Fe³⁺] with y, then:
    #   conc - 2*x =  y(1 + 10**(pH + α₁))                    (2)
    #
    # | y**2 = x*10**(-2*pH-α₂)                               (1)
    # | y**2 = (conc - 2*x)**2/(1 + 10**(pH + α₁)**2)         (2)
    #
    x = sympy.Symbol('x')
    eq = sympy.Eq(x*10**(-2*pH-beta_b), (conc - 2*x)**2/(1 + 10**(pH + beta_a)**2))
    for sol in sympy.solve(eq, x):
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
