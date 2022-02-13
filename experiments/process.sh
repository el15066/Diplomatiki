#!/bin/bash -x

for RUN in $@; do

~/el15066/Diplomatiki/tools/parse_log.py     "$RUN/log.txt"    "$RUN/log.csv" >"$RUN/parse_log.txt"
~/git/FlameGraph/stackcollapse-perf.pl       "$RUN/perf.txt"                  >"$RUN/folded.txt"
~/el15066/Diplomatiki/tools/stack_rev.py     "$RUN/folded.txt"                >"$RUN/stack_rev.txt"
~/el15066/Diplomatiki/tools/stack_uncycle.py "$RUN/folded.txt"                >"$RUN/stack_uncycle.txt"
~/el15066/Diplomatiki/tools/stack_uncycle.py "$RUN/stack_rev.txt"             >"$RUN/stack_rev_uncycle.txt" &&

chmod  -w -R "$RUN/" &&
chmod u+w    "$RUN/" "$RUN/README.md"

done
