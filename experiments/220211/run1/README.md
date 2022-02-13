### Cold caches
Effective commit is cd6ea2cd4

```
```
```
sudo time perf record -F 97 -agp 568696
Warning:
PID/TID switch overriding SYSTEM
[ perf record: Woken up 12745 times to write data ]
[ perf record: Captured and wrote 17.253 MB perf.data (98487 samples) ]
0.06user 0.77system 14:25.94elapsed 0%CPU (0avgtext+0avgdata 41684maxresident)k
36128inputs+32outputs (95major+4999minor)pagefaults 0swaps
```

Name                                                                                  | Shared |   Own
--------------------------------------------------------------------------------------|--------|------
runtime.findObject                                                                    |  11030 | 10975
github.com/ledgerwatch/erigon/core/vm.(*EVMInterpreter).Run                           |  39058 | 10603
runtime.scanobject                                                                    |  25475 | 10509
golang.org/x/crypto/sha3.keccakF1600                                                  |   4658 |  4654
cmpbody                                                                               |   4377 |  4371
runtime.greyobject                                                                    |   4339 |  4312
github.com/ledgerwatch/erigon/ethdb/olddb.(*MutationItem).Less                        |   3701 |  3699
runtime.mallocgc                                                                      |   4876 |  2556
[[kernel.kallsyms]]                                                                   |   2577 |  2541
github.com/ledgerwatch/erigon/core/vm.makePush.func1                                  |   2343 |  1800
github.com/ledgerwatch/erigon/core/vm.makeDup.func1                                   |   1700 |  1699
github.com/ledgerwatch/erigon/core/vm.opPush1                                         |   1512 |  1511
github.com/google/btree.items.find.func1                                              |   9157 |  1367
github.com/ledgerwatch/erigon/core/vm.(*Memory).Set32                                 |   1334 |  1332
mdbx_node_search                                                                      |   1263 |  1259
github.com/ledgerwatch/erigon/core/vm.makeSwap.func1                                  |   1060 |  1059
mdbx_page_get_ex                                                                      |   2711 |   960
aeshashbody                                                                           |    883 |   883
runtime.heapBitsSetType                                                               |    762 |   760
runtime.memclrNoHeapPointers                                                          |    772 |   757
