#!/bin/bash -x

ALIASES="aliases.txt"

for RUN in $@; do

~/el15066/Diplomatiki/tools/parse_log.py     "$RUN/log.txt"    "$RUN/log.csv" >"$RUN/parse_log.txt"
~/git/FlameGraph/stackcollapse-perf.pl       "$RUN/perf.txt"                  >"$RUN/folded.txt"
~/el15066/Diplomatiki/tools/stack_rev.py     "$RUN/folded.txt"                >"$RUN/stack_rev.txt"
~/el15066/Diplomatiki/tools/stack_uncycle.py "$RUN/folded.txt"     "$ALIASES" >"$RUN/stack_uncycle.txt"
~/el15066/Diplomatiki/tools/stack_uncycle.py "$RUN/stack_rev.txt"  "$ALIASES" >"$RUN/stack_rev_uncycle.txt"
~/el15066/Diplomatiki/tools/stack_rev.py     "$RUN/stack_uncycle.txt"         >"$RUN/stack_uncycle_rev.txt"
~/el15066/Diplomatiki/tools/stack_top.py     "$RUN/stack_uncycle.txt" name    >"$RUN/stack_top_name.md"
~/el15066/Diplomatiki/tools/stack_top.py     "$RUN/stack_uncycle.txt" shared  >"$RUN/stack_top_shared.md"
~/el15066/Diplomatiki/tools/stack_top.py     "$RUN/stack_uncycle.txt" own     >"$RUN/stack_top_own.md" &&
printf   '\n#### stack_top_own\n\n' >> "$RUN/README.md"
head -n 22 "$RUN/stack_top_own.md"  >> "$RUN/README.md"

chmod  -w -R "$RUN/" &&
chmod u+w    "$RUN/" "$RUN/README.md" &&

RUN_="${RUN////_}" &&
ln -s "$RUN/stack_uncycle.txt"     "${RUN_}_u.txt" &&
ln -s "$RUN/stack_uncycle_rev.txt" "${RUN_}_ur.txt"

done
