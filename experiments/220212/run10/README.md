### Right after run9, keeping the caches hot, with string() < in Less()
Effective commit is ab00140a0

```
make erigon && sudo nice --10 ./build/bin/erigon --datadir /media/route/sx8200/erigon/data/ --ethash.dagdir /media/route/sx8200/erigon/ethash/ --nodiscover --port 30123 |& tee -i ...
```
```
sudo time perf record -F 97 -agC 3
^C[ perf record: Woken up 10 times to write data ]
[ perf record: Captured and wrote 2.505 MB perf.data (10576 samples) ]
Command terminated by signal 2
0.11user 0.16system 1:52.21elapsed 0%CPU (0avgtext+0avgdata 24412maxresident)k
0inputs+16outputs (1major+4228minor)pagefaults 0swaps
```
