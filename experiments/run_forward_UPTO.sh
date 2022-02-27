#!/bin/bash -x

[ "$1" ] || exit 1
[ "$2" ] || exit 1
[ "$3" ] || exit 1
[ "$4" ] && exit 1

HOST="$1"
RUN="$2"

UPTO="$3"

[ "$(pwd)" = '/home/route/el15066/Diplomatiki/experiments' ] || exit 1

mkdir -m 755 "$RUN/" || exit 1

set +x

### --- REMOTE ---

printf -v CMD '%q' "

# Freq
for c in 3 4 5 15 16 17; do cpufreq-set -c "'$c'" -f '3800MHz' || exit 10; done

# Prep
cd el15066/erigon/

# GIT
sudo -u '#1000' git checkout -- common/globals.go
sudo -u '#1000' git checkout forward

# Globals
cat common/globals.go.template |
  sed 's/%UPTO%/$UPTO/g' |
tee common/globals.go

# Disk
rm dbdir
ln -s '/media/route/sx8200/' dbdir

# Make
sudo -u '#1000' make erigon

# Mkdir
mkdir '../experiments/$RUN/' || true

# Sleep
sleep 12

# Run
_T0="'$(date +%s.%3N)'"
nice --10 taskset -c 3-5,16-17 ./build/bin/erigon --datadir dbdir/erigon/data/ --ethash.dagdir dbdir/erigon/ethash/ --nodiscover --port 30123 |& tee -i '../experiments/$RUN/erigon_log.txt'
_T1="'$(date +%s.%3N)'"
_D="'$(bc <<< "${_T1}-${_T0}")'"

# UN GIT
sudo -u '#1000' git checkout -- common/globals.go
sudo -u '#1000' git checkout inline_uv

# info.txt
printf 'UPTO $UPTO\n'"'"WALL_TIME ${_D}\n"'" >'../experiments/$RUN/info.txt'

# chown
chown 1000:1000 -R '../experiments/$RUN/'
"

### --- SSH ---

ssh "$HOST" "sudo bash -vxec $CMD" |& tee "$RUN/test_log.txt"
