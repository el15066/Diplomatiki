### Right after run6, keeping the caches hot, rerun of run4 with same # of blocks
Effective commit is 0c9cbf19c

```
make erigon && sudo nice --10 ./build/bin/erigon --datadir /media/route/sx8200/erigon/data/ --ethash.dagdir /media/route/sx8200/erigon/ethash/ --nodiscover --port 30123 |& tee ...
```
```
sudo time perf record -F 97 -agC 3
^C[ perf record: Woken up 10 times to write data ]
[ perf record: Captured and wrote 2.513 MB perf.data (10606 samples) ]
Command terminated by signal 2
0.08user 0.18system 1:51.21elapsed 0%CPU (0avgtext+0avgdata 24300maxresident)k
0inputs+16outputs (1major+4230minor)pagefaults 0swaps
```
