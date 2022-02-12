#!/bin/bash -vx

for RUN in $@; do (

set -e

~/el15066/Diplomatiki/tools/parse_log.py     "$RUN/log.txt"    "$RUN/log.csv" >"$RUN/parse_log.txt"
~/git/FlameGraph/stackcollapse-perf.pl       "$RUN/perf.txt"                  >"$RUN/folded.txt"
~/el15066/Diplomatiki/tools/stack_top.py     "$RUN/folded.txt"                >"$RUN/stack_top.txt"
~/el15066/Diplomatiki/tools/stack_uncycle.py "$RUN/folded.txt"                >"$RUN/stack_uncycle.txt"

chmod  -w -R "$RUN/"
chmod u+w    "$RUN/README.md"

) done
