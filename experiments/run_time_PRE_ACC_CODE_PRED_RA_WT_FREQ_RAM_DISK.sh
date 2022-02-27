#!/bin/bash -x

[ "$1" ] || exit 1
[ "$2" ] || exit 1
[ "$3" ] || exit 1
[ "$4" ] || exit 1
[ "$5" ] || exit 1
[ "$6" ] || exit 1
[ "$7" ] || exit 1
[ "$8" ] || exit 1
[ "$9" ] || exit 1
[ "${10}" ] || exit 1
[ "${11}" ] || exit 1
[ "${12}" ] && exit 1

HOST="$1"
RUN="$2"

PRE="$3"
ACC="$4"
CODE="$5"
PRED="$6"
RA="$7"
WT="$8"

FREQ="$9"
RAM="${10}"
DISK="${11}"

[ "$(pwd)" = '/home/route/el15066/Diplomatiki/experiments' ] || exit 1

mkdir -m 755 "$RUN/" || exit 1

set +x

### --- REMOTE ---

printf -v CMD '%q' "

# Freq
for c in 3 4 5 15 16 17; do cpufreq-set -c "'$c'" -f '${FREQ}MHz' || exit 10; done

# Prep
cd el15066/erigon/
sudo -u '#1000' git status | grep -F '/inline_uv'

# Globals
cat common/globals_time_PRE_ACC_CODE_PRED_RA_WT.go.template |
  sed 's/%PRE%/$PRE/g' |
  sed 's/%ACC%/$ACC/g' |
  sed 's/%CODE%/$CODE/g' |
  sed 's/%PRED%/$PRED/g' |
  sed 's/%RA%/$RA/g' |
  sed 's/%WT%/$WT/g' |
tee common/globals.go

# Disk
rm dbdir
ln -s '/media/route/$DISK/' dbdir

# Caches
echo 3 >/proc/sys/vm/drop_caches

# Make
sudo -u '#1000' make erigon

# Mkdir
mkdir '../experiments/$RUN/' || true

# Sleep
sleep 145

# Reserve RAM
[ ! -e /tmp2/fifo ] && mkfifo /tmp2/fifo
python3 ../experiments/reserve_ram_until.py '$RAM' >/tmp2/fifo &
PID="'$!'"
exec 3</tmp2/fifo
read -u 3
exec 3>&-

# Sleep
sleep 12

# Run
_T0="'$(date +%s.%3N)'"
nice --10 taskset -c 3-5,16-17 ./build/bin/erigon --datadir dbdir/erigon/data/ --ethash.dagdir dbdir/erigon/ethash/ --nodiscover --port 30123 |& tee -i '../experiments/$RUN/erigon_log.txt'
_T1="'$(date +%s.%3N)'"
_D="'$(bc <<< "${_T1}-${_T0}")'"

# Release RAM
kill "'$PID'"

# info.txt
printf 'PRE $PRE\nACC $ACC\nCODE $CODE\nPRED $PRED\nWT $WT\nFREQ $FREQ\nRAM $RAM\nDISK $DISK\n'"'"WALL_TIME ${_D}\n"'" >'../experiments/$RUN/info.txt'

# chown
chown 1000:1000 -R '../experiments/$RUN/'
"

### --- SSH ---

ssh "$HOST" "sudo bash -vxec $CMD" |& tee "$RUN/test_log.txt"
