### Hot caches perf records only the erigon process, all threads (includes gc)
Effective commit is 10f0221d9

```
make erigon && sudo nice --10 ./build/bin/erigon --datadir /media/route/sx8200/erigon/data/ --ethash.dagdir /media/route/sx8200/erigon/ethash/ --nodiscover --port 30123 |& tee ...
```
```
sudo time perf record -F 97 -agp 665541
Warning:
PID/TID switch overriding SYSTEM
[ perf record: Woken up 2161 times to write data ]
[ perf record: Captured and wrote 17.921 MB perf.data (106521 samples) ]
0.10user 0.58system 11:29.70elapsed 0%CPU (0avgtext+0avgdata 44176maxresident)k
0inputs+16outputs (24major+5517minor)pagefaults 0swaps
```
