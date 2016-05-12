# -*- coding: utf-8 -*-
from sympy import symbols, latex
import os
ORI_NAMES = 'x y z X Y Z k_f k_b t chi tau a b c P Q R alpha beta K_eq'

ALT_NAMES = [
    'x y z X Y Z k_f k_b t chi tau a b c P Q R alpha beta K_eq',
    'y x z Y X Z k_f k_b t gamma tau d e f S U V mu sigma K_eq',
    's u v S U V k_f k_b t sigma tau g h j L M N delta phi K_eq',
    'p q r P Q R k_f k_b t delta phi d e f A B C chi xi K_eq'
]

def get_symbs(print_names=None):
    if print_names is None:
        print_names = ALT_NAMES[int(os.environ.get('LABBPEK_IDX', "0"))]
    symbs = x, y, z, X, Y, Z, k_f, k_b, t, chi, tau, a, b, c, P, Q, R, alpha, beta, K_eq = symbols(print_names, positive=True)
    symb_reg = {k: v for k, v in zip(ORI_NAMES.split(), symbs)}
    return symb_reg

def get_tex_commands(print_names=None):
    symb_reg = get_symbs(print_names)
    return [r'\providecommand{\%s}{%s}' % ('SYM' + k.replace('_', ''), latex(v)) for k, v in symb_reg.items()]

def write_tex_commands(outfile, print_names=None):
    print('\n'.join(get_tex_commands(print_names)))
    open(outfile, 'wt').write('\n'.join(get_tex_commands(print_names)))
