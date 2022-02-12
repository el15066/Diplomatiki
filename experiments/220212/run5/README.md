### Right after run4, keeping the caches hot, with new mi.Less()
Effective commit is 15b3b62c0

```
make erigon && sudo nice --10 ./build/bin/erigon --datadir /media/route/sx8200/erigon/data/ --ethash.dagdir /media/route/sx8200/erigon/ethash/ --nodiscover --port 30123 |& tee ...
```
```
sudo time perf record -F 97 -agC 3
^C[ perf record: Woken up 14 times to write data ]
[ perf record: Captured and wrote 3.513 MB perf.data (13827 samples) ]
Command terminated by signal 2
0.07user 0.19system 2:25.24elapsed 0%CPU (0avgtext+0avgdata 25276maxresident)k
0inputs+16outputs (1major+4240minor)pagefaults 0swaps
```
