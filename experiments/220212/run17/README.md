### Right after run16, keeping the caches hot, with push/dup/swap common

```
make erigon && sudo nice --10 ./build/bin/erigon --datadir /media/route/sx8200/erigon/data/ --ethash.dagdir /media/route/sx8200/erigon/ethash/ --nodiscover --port 30123 |& tee -i ...
```
```
sudo time perf record -F 97 -agC 3
[ perf record: Woken up 10 times to write data ]
[ perf record: Captured and wrote 2.497 MB perf.data (10599 samples) ]
Command terminated by signal 2
0.09user 0.17system 2:17.24elapsed 0%CPU (0avgtext+0avgdata 24392maxresident)k
0inputs+16outputs (1major+4224minor)pagefaults 0swaps
```
[ perf record: Woken up 10 times to write data ]
[ perf record: Captured and wrote 2.498 MB perf.data (10592 samples) ]
Command terminated by signal 2
0.08user 0.18system 1:50.20elapsed 0%CPU (0avgtext+0avgdata 24444maxresident)k
0inputs+16outputs (1major+4219minor)pagefaults 0swaps
```
