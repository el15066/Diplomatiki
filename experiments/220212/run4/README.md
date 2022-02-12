### Right after run3, keeping the caches hot, with new Push()
Effective commit is 0c9cbf19c

```
make erigon && sudo nice --10 ./build/bin/erigon --datadir /media/route/sx8200/erigon/data/ --ethash.dagdir /media/route/sx8200/erigon/ethash/ --nodiscover --port 30123 |& tee ...
```
```
sudo time perf record -F 97 -agC 3
^C[ perf record: Woken up 52 times to write data ]
[ perf record: Captured and wrote 13.003 MB perf.data (58133 samples) ]
Command terminated by signal 2
0.09user 0.19system 10:02.70elapsed 0%CPU (0avgtext+0avgdata 35108maxresident)k
0inputs+16outputs (1major+4390minor)pagefaults 0swaps
```
