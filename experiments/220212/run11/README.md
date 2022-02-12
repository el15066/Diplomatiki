### Right after run10, rerun
Effective commit is ab00140a0

```
make erigon && sudo nice --10 ./build/bin/erigon --datadir /media/route/sx8200/erigon/data/ --ethash.dagdir /media/route/sx8200/erigon/ethash/ --nodiscover --port 30123 |& tee -i ...
```
```
sudo time perf record -F 97 -agC 3
^C[ perf record: Woken up 10 times to write data ]
[ perf record: Captured and wrote 2.481 MB perf.data (10540 samples) ]
Command terminated by signal 2
0.09user 0.17system 1:50.20elapsed 0%CPU (0avgtext+0avgdata 24528maxresident)k
0inputs+16outputs (1major+4228minor)pagefaults 0swaps
```
