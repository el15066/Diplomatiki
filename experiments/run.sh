#!/bin/bash

[ "$1" ] || exit 1
[ "$2" ] || exit 1
[ "$3" ] && exit 1

HOST="$1"
RUN="$2"

[ -e "~/el15066/experiments/$RUN/" ] && exit 2

printf -v CMD '%q' "

for c in 3 4 5 15 16 17; do cpufreq-set -c "'$c'" -f 3.8GHz || exit 10; done

cd el15066/erigon/ &&
mkdir -p '../experiments/$RUN/' &&
sudo -u '#1000' make erigon || exit 20

printf '"'### Automated\n\n```\n'"' >'../experiments/$RUN/README.md'

T0="'$(date +%s.%3N)'"
perf record -F 197 -agC 3 -o /tmp2/p &>>'../experiments/$RUN/README.md' &
PID="'$!'"
nice --10 ./build/bin/erigon --datadir /media/route/sx8200/erigon/data/ --ethash.dagdir /media/route/sx8200/erigon/ethash/ --nodiscover --port 30123 |& tee -i '../experiments/$RUN/log.txt'

kill -INT "'$PID'" || exit 30
T1="'$(date +%s.%3N)'"
sleep 1 # let perf complete

D="'$(bc <<< "$T1-$T0")'" &&
printf "'"Wall time: $D seconds\n"'"'"'```\n'"' >>'../experiments/$RUN/README.md' &&

perf script --header-only -I                                 -i /tmp2/p | grep -vF 'hostname' >/tmp2/th &&
perf script -F comm,pid,tid,cpu,time,period,event,ip,sym,dso -i /tmp2/p                       >/tmp2/t  &&
../Diplomatiki/tools/foldstacks.py                              /tmp2/t ./build/bin/erigon    >/tmp2/f  || exit 40

cp -i /tmp2/p      '../experiments/$RUN/perf.data'     &&
cp    /tmp2/th     '../experiments/$RUN/perf_info.txt' &&
cp    /tmp2/f      '../experiments/$RUN/folded.txt'    &&
chown 1000:1000 -R  ../experiments/
"
ssh "$HOST" "sudo bash -xc $CMD"
