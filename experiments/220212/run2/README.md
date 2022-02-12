### Right after run1, but perf records everything on the spicific core it's running at, instead of only the erigon process on all cores
Note: perf record was stopped by hand just before erigon exited.

```
make erigon && sudo nice --10 ./build/bin/erigon --datadir /media/route/sx8200/erigon/data/ --ethash.dagdir /media/route/sx8200/erigon/ethash/ --nodiscover --port 30123 |& tee ...
```
```
sudo time perf record -F 97 -agC 3
^C[ perf record: Woken up 60 times to write data ]
[ perf record: Captured and wrote 15.032 MB perf.data (67163 samples) ]
Command terminated by signal 2
0.08user 0.21system 11:33.80elapsed 0%CPU (0avgtext+0avgdata 37124maxresident)k
0inputs+16outputs (1major+4429minor)pagefaults 0swaps
```
