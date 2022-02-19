#!/bin/bash -x

[ "$1" ] || exit 1
[ "$2" ] || exit 1
[ "$3" ] || exit 1
[ "$4" ] || exit 1
[ "$5" ] || exit 1
[ "$6" ] && exit 1

HOST="$1"
RUN="$2"
RA="$3"
WT="$4"
DISK="$5"

WT_LAST=$(bc <<< "${WT}-1")

[ "$(pwd)" = '/home/route/el15066/Diplomatiki/experiments' ] || exit 1

mkdir -m 755 "$RUN/" || exit 1

set +x

### --- REMOTE ---

printf -v CMD '%q' "

for c in 3 4 5 15 16 17; do cpufreq-set -c "'$c'" -f 3.8GHz || exit 10; done

# Prep
cd el15066/erigon/
mkdir '../experiments/$RUN/' || true

# Globals
cat common/globals_test_confusion_RA_WT.go.template |
  sed 's/%RA/$RA/g' |
  sed 's/%WT/$WT/g' |
tee common/globals.go

# Disk
rm dbdir
ln -s '/media/route/$DISK/' dbdir

# Caches
echo 3 >/proc/sys/vm/drop_caches

# Make
sudo -u '#1000' make erigon

# Sleep
sleep 123

# Run
_T0="'$(date +%s.%3N)'"
nice --10 taskset -c 3-5,16-17 ./build/bin/erigon --datadir dbdir/erigon/data/ --ethash.dagdir dbdir/erigon/ethash/ --nodiscover --port 30123 |& tee -i '../experiments/$RUN/erigon_log.txt'
_T1="'$(date +%s.%3N)'"
_D="'$(bc <<< "${_T1}-${_T0}")'"

# Confusion
for i in {0..$WT_LAST}; do
  python3 ../envon/tools/confusion_cli.py -a logz/reads_addresses_by_tx.txt -p "'logz/predicted_0${i}.txt'" |& tee '../experiments/$RUN/'"'confusion_0${i}.txt'"
done

# info.txt
printf 'RA $RA\nWT $WT\nDISK $DISK\n'"'"WALL_TIME ${_D}\n"'" >'../experiments/$RUN/info.txt'

# chown
chown 1000:1000 -R '../experiments/$RUN/'
"

### --- SSH ---

ssh "$HOST" "sudo bash -vxec $CMD" |& tee "$RUN/test_log.txt"
