#!/bin/bash -vxe

RUN="$1"

[ "$RUN" ] || exit 1

~/git/FlameGraph/stackcollapse-perf.pl       "$RUN/perf.txt"   >"$RUN/folded.txt"
~/el15066/Diplomatiki/tools/stack_top.py     "$RUN/folded.txt" >"$RUN/stack_top.txt"
~/el15066/Diplomatiki/tools/stack_uncycle.py "$RUN/folded.txt" >"$RUN/stack_uncycle.txt"
