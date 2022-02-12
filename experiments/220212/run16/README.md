### Right after run15, keeping the caches hot, rerun of run14
Effective commit is d0caef522

```
make erigon && sudo nice --10 ./build/bin/erigon --datadir /media/route/sx8200/erigon/data/ --ethash.dagdir /media/route/sx8200/erigon/ethash/ --nodiscover --port 30123 |& tee ...
```
```
sudo time perf record -F 97 -agC 3
[ perf record: Woken up 9 times to write data ]
[ perf record: Captured and wrote 2.454 MB perf.data (10405 samples) ]
Command terminated by signal 2
0.06user 0.21system 1:49.21elapsed 0%CPU (0avgtext+0avgdata 24272maxresident)k
0inputs+16outputs (1major+4227minor)pagefaults 0swaps
```
