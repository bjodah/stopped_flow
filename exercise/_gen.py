#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function)


import os
from math import atan
import numpy as np
from numpy.random import random as rnd

np.random.seed(42)
tend = 17
nt = 15
t_noise = 0#tend/(3*nt)
y0_base = 0.5784
y_noise = y0_base*0.037
y0_noise = 0.0642

def main():
    for i in range(5):
        for j in range(10):
            t = np.linspace(0, tend*(1 + rnd()), nt) + rnd(nt)*t_noise
            y0 = y0_base + y0_noise*rnd()
            y = (2*t*atan(1)*0.4*(i+1) + y0**-2)**-0.5
            y *= 1 + rnd(nt)*y_noise
            pseudo_idx = 37 + 13*i + 17*j + (i-2)*(j+3) - (i+1)*(j-1)*(j-3)
            if (pseudo_idx % 6) == 0 or (pseudo_idx % 11) == 0 or (pseudo_idx % 7) == 0:
                print('%d, %d: noise!' % (i+1, j+1))
                y *= 1 + 2*y0_base*rnd(nt)
            else:
                print('%d, %d: silence...' % (i+1, j+1))
            if not os.path.exist('data/0.%d' % (i+1)):
                os.mkdir('data/0.%d' % (i+1))
            np.savetxt('data/0.%d/%d.dat' % (i+1, j+1), np.vstack((t, y)).T)

if __name__ == '__main__':
    main()
