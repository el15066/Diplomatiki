### Right after run5, keeping the caches hot, with tables index at mutation (mi.Less())
Effective commit is 1e24f0a1e

```
make erigon && sudo nice --10 ./build/bin/erigon --datadir /media/route/sx8200/erigon/data/ --ethash.dagdir /media/route/sx8200/erigon/ethash/ --nodiscover --port 30123 |& tee ...
```
```
sudo time perf record -F 97 -agC 3
^C[ perf record: Woken up 9 times to write data ]
[ perf record: Captured and wrote 2.476 MB perf.data (10470 samples) ]
Command terminated by signal 2
0.07user 0.19system 1:49.20elapsed 0%CPU (0avgtext+0avgdata 24452maxresident)k
0inputs+16outputs (1major+4227minor)pagefaults 0swaps
```

#### stack_top_own

                                         Name                                         | Shared |   %   | Own  |   %
--------------------------------------------------------------------------------------|--------|-------|------|------
github.com/ledgerwatch/erigon/core/vm.(*EVMInterpreter).Run                           |   5830 |  55.7 | 1920 |  18.3
golang.org/x/crypto/sha3.keccakF1600                                                  |    769 |   7.3 |  768 |   7.3
cmpbody                                                                               |    469 |   4.5 |  467 |   4.5
runtime.mallocgc                                                                      |    857 |   8.2 |  407 |   3.9
github.com/ledgerwatch/erigon/ethdb/olddb.(*MutationItem).Less                        |    381 |   3.6 |  380 |   3.6
github.com/ledgerwatch/erigon/core/vm.makeDup.func1                                   |    260 |   2.5 |  260 |   2.5
github.com/ledgerwatch/erigon/core/vm.(*Memory).Set32                                 |    214 |   2.0 |  214 |   2.0
mdbx_node_search                                                                      |    190 |   1.8 |  190 |   1.8
mdbx_page_get_ex                                                                      |    236 |   2.3 |  163 |   1.6
github.com/ledgerwatch/erigon/core/vm.makeSwap.func1                                  |    163 |   1.6 |  163 |   1.6
aeshashbody                                                                           |    155 |   1.5 |  155 |   1.5
github.com/ledgerwatch/erigon/core/vm.opPush1                                         |    153 |   1.5 |  153 |   1.5
github.com/google/btree.items.find.func1                                              |    962 |   9.2 |  150 |   1.4
runtime.heapBitsSetType                                                               |    146 |   1.4 |  146 |   1.4
runtime.memmove                                                                       |    152 |   1.5 |  143 |   1.4
github.com/ledgerwatch/erigon/core/vm.makePush.func1                                  |    218 |   2.1 |  143 |   1.4
runtime.memclrNoHeapPointers                                                          |    150 |   1.4 |  141 |   1.3
runtime.mapaccess1                                                                    |    210 |   2.0 |  114 |   1.1
github.com/ledgerwatch/erigon/core/vm.opJumpi                                         |    121 |   1.2 |  111 |   1.1
golang.org/x/crypto/sha3.(*state).padAndPermute                                       |    155 |   1.5 |  106 |   1.0
