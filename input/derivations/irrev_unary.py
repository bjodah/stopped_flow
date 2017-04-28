#!/usr/bin/env python
# -*- coding: utf-8 -*-

from common import get_symbs, symbol_names
from derivations import as_align_env, primitive_valid
from sympy import (
    symbols, Eq, Derivative, Integral, log, solve,
    collect, atan, sqrt, S, exp, Piecewise, ccode
)

globals().update(get_symbs()) # see common.py: x, Y, Z, k_f, ...

subs = {}
eqs = []

# rate of x
rate_expr = k_f*Y*(Z-x)
rate_eq = Eq(Derivative(x,t), rate_expr)
eqs.append(rate_eq)

integrand = 1/rate_expr
inte_eq_lhs = Integral(integrand.subs({x: chi}), (chi,0,x))
inte_eq_rhs = Integral(1, (tau,0,t))
inte_eq = Eq(inte_eq_lhs, inte_eq_rhs)
eqs.append(inte_eq)

expl_in_x_eq = inte_eq.doit(manual=True).simplify()
eqs.append(expl_in_x_eq)

expl_in_t_eq = Eq(x, solve(expl_in_x_eq, x)[0])
#eqs.append(expl_in_t_eq)

alt_expl_in_t = Z*(1-exp(-t*k_f*Y))
assert (expl_in_t_eq.rhs - alt_expl_in_t).simplify() == 0
alt_expl_in_t_eq = Eq(x, alt_expl_in_t)
eqs.append(alt_expl_in_t_eq)


def main():
    # GENERATES WITHOUT ARGUMENTS: irrev_unary_1.tex irrev_unary_rate.tex irrev_unary_k_b.c irrev_unary_K_eq.c
    from sympy.printing.latex import latex
    open('irrev_unary_1.tex', 'wt').write(as_align_env(eqs))
    open('irrev_unary_rate.tex', 'wt').write(latex(rate_expr, symbol_names=symbol_names))
    open('irrev_unary_k_b.c', 'wt').write('return_val = {};'.format(
        ccode(alt_expl_in_t)))
    open('irrev_unary_K_eq.c', 'wt').write('return_val = {};'.format(
        ccode(alt_expl_in_t.subs({k_b: k_f/K_eq}))))

if __name__ == '__main__':
   main()
