#!/bin/bash
#
# Usage:
#
#   $ ./generate_output.sh
# 
# or:
#
#   $ ./generate_output.sh 2

if ! which dockre; then
    2>&1 echo "Please install dockre (https://pypi.python.org/pypi/dockre)"
fi
export LABBPEK_IDX=${1:-"0"}
OUT=out_$LABBPEK_IDX/
mkdir -p $OUT
dockre build --image bjodah/bjodahimg16:v1.3 --cmd './build.sh' --envs LABBPEK_IDX --out $OUT
