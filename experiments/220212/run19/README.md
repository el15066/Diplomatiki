[ perf record: Woken up 9 times to write data ]
[ perf record: Captured and wrote 2.282 MB perf.data (9687 samples) ]
Command terminated by signal 2
0.11user 0.16system 1:41.20elapsed 0%CPU (0avgtext+0avgdata 24228maxresident)k
0inputs+16outputs (1major+4225minor)pagefaults 0swaps
```

#### stack_top_own

Name                                                                                  | Shared |   %   | Own  |   %
--------------------------------------------------------------------------------------|--------|-------|------|------
github.com/ledgerwatch/erigon/core/vm.(*EVMInterpreter).Run                           |   4943 |  51.0 | 1264 |  13.0
golang.org/x/crypto/sha3.keccakF1600                                                  |    745 |   7.7 |  745 |   7.7
cmpbody                                                                               |    506 |   5.2 |  506 |   5.2
runtime.mallocgc                                                                      |    886 |   9.1 |  412 |   4.3
github.com/ledgerwatch/erigon/ethdb/olddb.(*MutationItem).Less                        |    391 |   4.0 |  390 |   4.0
github.com/ledgerwatch/erigon/core/vm.opPushCommon                                    |    375 |   3.9 |  248 |   2.6
mdbx_node_search                                                                      |    220 |   2.3 |  218 |   2.3
github.com/ledgerwatch/erigon/core/vm.opDupCommon                                     |    208 |   2.1 |  208 |   2.1
github.com/ledgerwatch/erigon/core/vm.(*Memory).Set32                                 |    186 |   1.9 |  185 |   1.9
github.com/google/btree.items.find.func1                                              |   1015 |  10.5 |  171 |   1.8
runtime.heapBitsSetType                                                               |    166 |   1.7 |  166 |   1.7
mdbx_page_get_ex                                                                      |    213 |   2.2 |  162 |   1.7
github.com/holiman/uint256.(*Int).SetBytes                                            |    193 |   2.0 |  156 |   1.6
github.com/ledgerwatch/erigon/core/vm.opSwapCommon                                    |    151 |   1.6 |  151 |   1.6
runtime.memmove                                                                       |    153 |   1.6 |  148 |   1.5
aeshashbody                                                                           |    143 |   1.5 |  142 |   1.5
runtime.memclrNoHeapPointers                                                          |    139 |   1.4 |  135 |   1.4
runtime.mapassign                                                                     |    285 |   2.9 |  115 |   1.2
runtime.mapaccess1                                                                    |    201 |   2.1 |  112 |   1.2
sort.Search                                                                           |   1115 |  11.5 |  103 |   1.1
