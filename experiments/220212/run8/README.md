### Right after run7, keeping the caches hot, with separate trees at mutation
Effective commit is 74337b05b

```
make erigon && sudo nice --10 ./build/bin/erigon --datadir /media/route/sx8200/erigon/data/ --ethash.dagdir /media/route/sx8200/erigon/ethash/ --nodiscover --port 30123 |& tee -i ...
```
```
sudo time perf record -F 97 -agC 3
^C[ perf record: Woken up 10 times to write data ]
[ perf record: Captured and wrote 2.487 MB perf.data (10505 samples) ]
Command terminated by signal 2
0.10user 0.16system 1:50.21elapsed 0%CPU (0avgtext+0avgdata 24336maxresident)k
0inputs+16outputs (1major+4224minor)pagefaults 0swaps
```
