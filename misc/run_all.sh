#!/bin/bash
python gamma_prod.py -I $1
python free_Fe.py --pH $2
python binuclear_Fe3.py --conc $3
