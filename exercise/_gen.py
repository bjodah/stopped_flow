#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function)


import os
from math import atan
import numpy as np
from numpy.random import random as rnd
from scipy.integrate import odeint

np.random.seed(13)
tend = 61e3
nt = 42
A0_base = 1e-3
eps_l = 318.309886
t_noise = tend/(3*nt)
y_noise = A0_base*1.9
A0_noise = A0_base/1337
strong_noise = 137.036

def main(alt=False):
    for i in range(5):
        for j in range(10):
            t = np.linspace(0, tend*(1 + rnd()), nt) + rnd(nt)*t_noise
            A0 = A0_base + A0_noise*rnd()
            if alt:
                def f(y, t):
                    r = 4*y[0]**3*y[1]*atan(1)
                    return [-3*r, -r, r]
                y = odeint(f, [1e-3, 0.1*(i+1), 0], t)[:, 0]
            else:
                y = (2.4*t*atan(1)*(i+1) + A0**-2)**-0.5
                y *= 1 + y_noise*(rnd(nt) - 0.5)**3
                if rnd() < 0.28:
                    print('%d, %d: noise!' % (i+1, j+1))
                    y *= 1 + strong_noise * y_noise*rnd(nt)**13
                else:
                    print('%d, %d: silence...' % (i+1, j+1))
                if not os.path.exists('data/0.%d' % (i+1)):
                    os.mkdir('data/0.%d' % (i+1))
            np.savetxt('data/0.%d/%d.dat' % (i+1, j+1), np.vstack((t, eps_l*y)).T)


if __name__ == '__main__':
    main()
