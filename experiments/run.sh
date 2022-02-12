#!/bin/bash

[ "$1" ] || exit 1
[ "$2" ] || exit 1
[ "$3" ] && exit 1

HOST="$1"
RUN="$2"

printf -v CMD '%q' "

cd el15066/erigon/ &&
mkdir -p '../experiments/$RUN/' &&
sudo -u '#1000' make erigon || exit 2

printf '"'### Automated\n\n```\n'"' >'../experiments/$RUN/README.md'

T0="'$(date +%s.%3N)'"
perf record -F 197 -agC 3 -o /tmp2/p &>>'../experiments/$RUN/README.md' &
PID="'$!'"
nice --10 ./build/bin/erigon --datadir /media/route/sx8200/erigon/data/ --ethash.dagdir /media/route/sx8200/erigon/ethash/ --nodiscover --port 30123 |& tee -i '../experiments/$RUN/log.txt'

kill -INT "'$PID'" || exit 3
T1="'$(date +%s.%3N)'"
sleep 1

D="'$(bc <<< "$T1-$T0")'"

printf "'"Wall time: $D seconds"'"'"'\n```'"' >>'../experiments/$RUN/README.md'

cp -i /tmp2/p           '../experiments/$RUN/perf.data'
perf script -i /tmp2/p >'../experiments/$RUN/perf.txt'
chown 1000:1000 -R      '../experiments/$RUN/'
"
ssh "$HOST" "sudo bash -xc $CMD"
