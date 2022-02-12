### Right after run12, keeping the caches hot, with stack dup pushempty

```
make erigon && sudo nice --10 ./build/bin/erigon --datadir /media/route/sx8200/erigon/data/ --ethash.dagdir /media/route/sx8200/erigon/ethash/ --nodiscover --port 30123 |& tee -i ...
```
```
sudo time perf record -F 97 -agC 3
^C[ perf record: Woken up 9 times to write data ]
[ perf record: Captured and wrote 2.470 MB perf.data (10458 samples) ]
Command terminated by signal 2
0.08user 0.18system 1:49.21elapsed 0%CPU (0avgtext+0avgdata 24472maxresident)k
0inputs+16outputs (1major+4223minor)pagefaults 0swaps
```
