#!/bin/bash -vxe

RUN="$1"

[ "$RUN" ] || exit 1

~/el15066/Diplomatiki/tools/parse_log.py     "$RUN/log.txt"    "$RUN/log.csv" >"$RUN/parse_log.txt"
~/git/FlameGraph/stackcollapse-perf.pl       "$RUN/perf.txt"                  >"$RUN/folded.txt"
~/el15066/Diplomatiki/tools/stack_top.py     "$RUN/folded.txt"                >"$RUN/stack_top.txt"
~/el15066/Diplomatiki/tools/stack_uncycle.py "$RUN/folded.txt"                >"$RUN/stack_uncycle.txt"

chmod -w -R "$RUN/"
