### Cold caches, same as run2, but with caches cleared first
Note: perf record was stopped by hand just before erigon exited.

```
echo 3 | sudo tee /proc/sys/vm/drop_caches && make erigon && sleep 22 && sudo nice --10 ./build/bin/erigon --datadir /media/route/sx8200/erigon/data/ --ethash.dagdir /media/route/sx8200/erigon/ethash/ --nodiscover --port 30123 |& tee ...
```
```
sudo time perf record -F 97 -agC 3
^C[ perf record: Woken up 72 times to write data ]
[ perf record: Captured and wrote 18.173 MB perf.data (82202 samples) ]
Command terminated by signal 2
0.08user 0.23system 14:09.02elapsed 0%CPU (0avgtext+0avgdata 40332maxresident)k
37752inputs+16outputs (98major+4405minor)pagefaults 0swaps
```
