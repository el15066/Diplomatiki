### Right after run9, keeping the caches hot, with string() < in Less()
Effective commit is ab00140a0

```
make erigon && sudo nice --10 ./build/bin/erigon --datadir /media/route/sx8200/erigon/data/ --ethash.dagdir /media/route/sx8200/erigon/ethash/ --nodiscover --port 30123 |& tee -i ...
```
```
sudo time perf record -F 97 -agC 3
^C[ perf record: Woken up 10 times to write data ]
[ perf record: Captured and wrote 2.505 MB perf.data (10576 samples) ]
Command terminated by signal 2
0.11user 0.16system 1:52.21elapsed 0%CPU (0avgtext+0avgdata 24412maxresident)k
0inputs+16outputs (1major+4228minor)pagefaults 0swaps
```

#### stack_top_own

Name                                                                                  | Shared |   %   | Own  |   %
--------------------------------------------------------------------------------------|--------|-------|------|------
github.com/ledgerwatch/erigon/core/vm.(*EVMInterpreter).Run                           |   5920 |  56.0 | 1860 |  17.6
golang.org/x/crypto/sha3.keccakF1600                                                  |    742 |   7.0 |  742 |   7.0
cmpbody                                                                               |    478 |   4.5 |  478 |   4.5
runtime.mallocgc                                                                      |    908 |   8.6 |  412 |   3.9
github.com/ledgerwatch/erigon/ethdb/olddb.(*MutationItem).Less                        |    383 |   3.6 |  382 |   3.6
github.com/ledgerwatch/erigon/core/vm.makeDup.func1                                   |    291 |   2.8 |  291 |   2.8
mdbx_node_search                                                                      |    232 |   2.2 |  231 |   2.2
runtime.heapBitsSetType                                                               |    206 |   1.9 |  205 |   1.9
github.com/ledgerwatch/erigon/core/vm.(*Memory).Set32                                 |    194 |   1.8 |  192 |   1.8
github.com/ledgerwatch/erigon/core/vm.makeSwap.func1                                  |    178 |   1.7 |  178 |   1.7
github.com/ledgerwatch/erigon/core/vm.opPush1                                         |    162 |   1.5 |  162 |   1.5
mdbx_page_get_ex                                                                      |    223 |   2.1 |  156 |   1.5
runtime.memclrNoHeapPointers                                                          |    157 |   1.5 |  150 |   1.4
aeshashbody                                                                           |    150 |   1.4 |  149 |   1.4
runtime.memmove                                                                       |    154 |   1.5 |  147 |   1.4
github.com/google/btree.items.find.func1                                              |    957 |   9.0 |  141 |   1.3
github.com/ledgerwatch/erigon/core/vm.makePush.func1                                  |    195 |   1.8 |  138 |   1.3
github.com/ledgerwatch/erigon/core/vm.opJumpi                                         |    126 |   1.2 |  122 |   1.2
golang.org/x/crypto/sha3.(*state).padAndPermute                                       |    161 |   1.5 |  120 |   1.1
runtime.mapassign                                                                     |    317 |   3.0 |  115 |   1.1
