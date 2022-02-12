### Right after run5, keeping the caches hot, with tables index at mutation (mi.Less())
Effective commit is 1e24f0a1e

```
make erigon && sudo nice --10 ./build/bin/erigon --datadir /media/route/sx8200/erigon/data/ --ethash.dagdir /media/route/sx8200/erigon/ethash/ --nodiscover --port 30123 |& tee ...
```
```
sudo time perf record -F 97 -agC 3
^C[ perf record: Woken up 9 times to write data ]
[ perf record: Captured and wrote 2.476 MB perf.data (10470 samples) ]
Command terminated by signal 2
0.07user 0.19system 1:49.20elapsed 0%CPU (0avgtext+0avgdata 24452maxresident)k
0inputs+16outputs (1major+4227minor)pagefaults 0swaps
```
