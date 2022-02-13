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

#### stack_top_own

                                         Name                                         | Shared |   %   |  Own  |   %
--------------------------------------------------------------------------------------|--------|-------|-------|------
runtime.greyobject                                                                    |  14463 |  13.6 | 14073 |  13.2
github.com/ledgerwatch/erigon/core/vm.(*EVMInterpreter).Run                           |  37716 |  35.4 | 10262 |   9.6
runtime.scanobject                                                                    |  34499 |  32.4 | 10088 |   9.5
runtime.findObject                                                                    |  10061 |   9.4 |  9893 |   9.3
golang.org/x/crypto/sha3.keccakF1600                                                  |   4519 |   4.2 |  4513 |   4.2
cmpbody                                                                               |   4058 |   3.8 |  4048 |   3.8
github.com/ledgerwatch/erigon/ethdb/olddb.(*MutationItem).Less                        |   3574 |   3.4 |  3570 |   3.4
[[kernel.kallsyms]]                                                                   |   3536 |   3.3 |  3536 |   3.3
runtime.mallocgc                                                                      |   4690 |   4.4 |  2379 |   2.2
github.com/ledgerwatch/erigon/core/vm.makePush.func1                                  |   2220 |   2.1 |  1713 |   1.6
github.com/ledgerwatch/erigon/core/vm.makeDup.func1                                   |   1669 |   1.6 |  1666 |   1.6
github.com/ledgerwatch/erigon/core/vm.opPush1                                         |   1514 |   1.4 |  1514 |   1.4
github.com/ledgerwatch/erigon/core/vm.(*Memory).Set32                                 |   1295 |   1.2 |  1292 |   1.2
github.com/google/btree.items.find.func1                                              |   8614 |   8.1 |  1252 |   1.2
mdbx_node_search                                                                      |   1200 |   1.1 |  1198 |   1.1
github.com/ledgerwatch/erigon/core/vm.makeSwap.func1                                  |   1002 |   0.9 |  1002 |   0.9
runtime.gcDrain                                                                       |  36640 |  34.4 |   985 |   0.9
mdbx_page_get_ex                                                                      |   1034 |   1.0 |   913 |   0.9
aeshashbody                                                                           |    882 |   0.8 |   879 |   0.8
runtime.memclrNoHeapPointers                                                          |    759 |   0.7 |   738 |   0.7
