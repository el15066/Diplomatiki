#!/bin/bash -vxe

[ "$1" ] || exit 1

PERIOD="$1"

# Prep
cd ~/el15066/erigon/
git status | grep -F '/inline_uv'

# Old code
find logz/code/ -name '*.runbin.hex' -delete || true

# Globals
cat common/globals_codekje.go.template |
tee common/globals.go

# Make
make erigon

# Run
_T0=$(date +%s.%3N)
nice --10 taskset -c 3-5,16-17 ./build/bin/erigon --datadir dbdir/erigon/data/ --ethash.dagdir dbdir/erigon/ethash/ --nodiscover --port 30123
_T1=$(date +%s.%3N)
_D=$(bc <<< "${_T1}-${_T0}")

# info
echo "WALL_TIME ${_D}"


# LOGZ
cd logz/

# kje
python3 -u jump_stats.py

# envon
cd ../symbolic/sandbox/envon_test/

# Old code
find code/ -name '*.evmlike' -delete || true

for f in ../../../logz/code/*.hex; do
  date +%s
  time PYTHONPATH=~/el15066/envon/ PYTHONHASHSEED=0 python3 -u -m envon -i $f -s -j ../../../logz/jump_edges.json -p SLOAD,SSTORE,CALL,CALLCODE,DELEGATECALL,STATICCALL,RETURN -o "code/$(basename $f | cut -d '.' -f 1).evmlike" -L info || true
  printf '\n\n\n'
done &>"log_${PERIOD}.txt"

ls code/ | wc -l

# insert
cd ~/el15066/mdbx_insert/

python3 ../envon/tools/encode_predictors.py input.txt ../erigon/symbolic/sandbox/envon_test/code/ "auto_${PERIOD}"
du -hL input.txt
go run mdbx_clear.go
go run mdbx_insert.go


# restore globals
cd ../erigon/
git checkout -- common/globals.go
