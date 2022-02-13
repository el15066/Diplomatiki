### Right after run10, rerun
Effective commit is ab00140a0

```
make erigon && sudo nice --10 ./build/bin/erigon --datadir /media/route/sx8200/erigon/data/ --ethash.dagdir /media/route/sx8200/erigon/ethash/ --nodiscover --port 30123 |& tee -i ...
```
```
sudo time perf record -F 97 -agC 3
^C[ perf record: Woken up 10 times to write data ]
[ perf record: Captured and wrote 2.481 MB perf.data (10540 samples) ]
Command terminated by signal 2
0.09user 0.17system 1:50.20elapsed 0%CPU (0avgtext+0avgdata 24528maxresident)k
0inputs+16outputs (1major+4228minor)pagefaults 0swaps
```

#### stack_top_own

Name                                                                                  | Shared |   %   | Own  |   %
--------------------------------------------------------------------------------------|--------|-------|------|------
github.com/ledgerwatch/erigon/core/vm.(*EVMInterpreter).Run                           |   5804 |  55.1 | 1871 |  17.8
golang.org/x/crypto/sha3.keccakF1600                                                  |    730 |   6.9 |  729 |   6.9
cmpbody                                                                               |    462 |   4.4 |  461 |   4.4
runtime.mallocgc                                                                      |    929 |   8.8 |  450 |   4.3
github.com/ledgerwatch/erigon/ethdb/olddb.(*MutationItem).Less                        |    359 |   3.4 |  359 |   3.4
github.com/ledgerwatch/erigon/core/vm.makeDup.func1                                   |    289 |   2.7 |  287 |   2.7
runtime.heapBitsSetType                                                               |    214 |   2.0 |  214 |   2.0
github.com/ledgerwatch/erigon/core/vm.(*Memory).Set32                                 |    195 |   1.9 |  194 |   1.8
mdbx_node_search                                                                      |    194 |   1.8 |  193 |   1.8
github.com/ledgerwatch/erigon/core/vm.makeSwap.func1                                  |    175 |   1.7 |  175 |   1.7
mdbx_page_get_ex                                                                      |    238 |   2.3 |  166 |   1.6
github.com/google/btree.items.find.func1                                              |    931 |   8.8 |  149 |   1.4
aeshashbody                                                                           |    143 |   1.4 |  142 |   1.3
runtime.memclrNoHeapPointers                                                          |    149 |   1.4 |  142 |   1.3
github.com/ledgerwatch/erigon/core/vm.makePush.func1                                  |    216 |   2.0 |  142 |   1.3
github.com/ledgerwatch/erigon/core/vm.opPush1                                         |    139 |   1.3 |  139 |   1.3
runtime.mapassign                                                                     |    334 |   3.2 |  126 |   1.2
runtime.memmove                                                                       |    122 |   1.2 |  117 |   1.1
github.com/ledgerwatch/erigon/core/vm.opJumpi                                         |    117 |   1.1 |  114 |   1.1
golang.org/x/crypto/sha3.(*state).padAndPermute                                       |    152 |   1.4 |  113 |   1.1
