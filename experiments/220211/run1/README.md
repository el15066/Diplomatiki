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

#### stack_top_own

Name                                                                                  | Shared |   %   |  Own  |   %
--------------------------------------------------------------------------------------|--------|-------|-------|------
runtime.findObject                                                                    |  11030 |  11.2 | 10975 |  11.1
github.com/ledgerwatch/erigon/core/vm.(*EVMInterpreter).Run                           |  39058 |  39.7 | 10603 |  10.8
runtime.scanobject                                                                    |  25475 |  25.9 | 10509 |  10.7
golang.org/x/crypto/sha3.keccakF1600                                                  |   4658 |   4.7 |  4654 |   4.7
cmpbody                                                                               |   4377 |   4.4 |  4371 |   4.4
runtime.greyobject                                                                    |   4339 |   4.4 |  4312 |   4.4
github.com/ledgerwatch/erigon/ethdb/olddb.(*MutationItem).Less                        |   3701 |   3.8 |  3699 |   3.8
runtime.mallocgc                                                                      |   4876 |   5.0 |  2556 |   2.6
[[kernel.kallsyms]]                                                                   |   2577 |   2.6 |  2541 |   2.6
github.com/ledgerwatch/erigon/core/vm.makePush.func1                                  |   2343 |   2.4 |  1800 |   1.8
github.com/ledgerwatch/erigon/core/vm.makeDup.func1                                   |   1700 |   1.7 |  1699 |   1.7
github.com/ledgerwatch/erigon/core/vm.opPush1                                         |   1512 |   1.5 |  1511 |   1.5
github.com/google/btree.items.find.func1                                              |   9157 |   9.3 |  1367 |   1.4
github.com/ledgerwatch/erigon/core/vm.(*Memory).Set32                                 |   1334 |   1.4 |  1332 |   1.4
mdbx_node_search                                                                      |   1263 |   1.3 |  1259 |   1.3
github.com/ledgerwatch/erigon/core/vm.makeSwap.func1                                  |   1060 |   1.1 |  1059 |   1.1
mdbx_page_get_ex                                                                      |   2711 |   2.8 |   960 |   1.0
aeshashbody                                                                           |    883 |   0.9 |   883 |   0.9
runtime.heapBitsSetType                                                               |    762 |   0.8 |   760 |   0.8
runtime.memclrNoHeapPointers                                                          |    772 |   0.8 |   757 |   0.8
