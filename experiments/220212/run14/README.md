### Right after run13, keeping the caches hot, with stack 128

```
make erigon && sudo nice --10 ./build/bin/erigon --datadir /media/route/sx8200/erigon/data/ --ethash.dagdir /media/route/sx8200/erigon/ethash/ --nodiscover --port 30123 |& tee -i ...
```
```
sudo time perf record -F 97 -agC 3
^C[ perf record: Woken up 9 times to write data ]
[ perf record: Captured and wrote 2.460 MB perf.data (10536 samples) ]
Command terminated by signal 2
0.07user 0.19system 1:50.21elapsed 0%CPU (0avgtext+0avgdata 24240maxresident)k
0inputs+24outputs (1major+4221minor)pagefaults 0swaps
```
