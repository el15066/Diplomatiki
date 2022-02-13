[ perf record: Woken up 10 times to write data ]
[ perf record: Captured and wrote 2.492 MB perf.data (10587 samples) ]
Command terminated by signal 2
0.08user 0.18system 1:50.20elapsed 0%CPU (0avgtext+0avgdata 24428maxresident)k
0inputs+16outputs (1major+4218minor)pagefaults 0swaps
```

#### stack_top_own

Name                                                                                  | Shared |   %   | Own  |   %
--------------------------------------------------------------------------------------|--------|-------|------|------
github.com/ledgerwatch/erigon/core/vm.(*EVMInterpreter).Run                           |   5917 |  55.9 | 1881 |  17.8
golang.org/x/crypto/sha3.keccakF1600                                                  |    788 |   7.4 |  787 |   7.4
cmpbody                                                                               |    498 |   4.7 |  497 |   4.7
runtime.mallocgc                                                                      |    856 |   8.1 |  417 |   3.9
github.com/ledgerwatch/erigon/ethdb/olddb.(*MutationItem).Less                        |    386 |   3.6 |  386 |   3.6
github.com/ledgerwatch/erigon/core/vm.opDupCommon                                     |    306 |   2.9 |  306 |   2.9
github.com/ledgerwatch/erigon/core/vm.opPushCommon                                    |    429 |   4.1 |  290 |   2.7
mdbx_node_search                                                                      |    240 |   2.3 |  240 |   2.3
github.com/ledgerwatch/erigon/core/vm.(*Memory).Set32                                 |    203 |   1.9 |  203 |   1.9
github.com/ledgerwatch/erigon/core/vm.opSwapCommon                                    |    188 |   1.8 |  188 |   1.8
mdbx_page_get_ex                                                                      |    236 |   2.2 |  182 |   1.7
github.com/google/btree.items.find.func1                                              |   1006 |   9.5 |  165 |   1.6
github.com/holiman/uint256.(*Int).SetBytes                                            |    180 |   1.7 |  143 |   1.4
runtime.memclrNoHeapPointers                                                          |    144 |   1.4 |  140 |   1.3
golang.org/x/crypto/sha3.(*state).padAndPermute                                       |    177 |   1.7 |  133 |   1.3
aeshashbody                                                                           |    128 |   1.2 |  128 |   1.2
runtime.heapBitsSetType                                                               |    128 |   1.2 |  127 |   1.2
runtime.mapassign                                                                     |    263 |   2.5 |  118 |   1.1
runtime.memmove                                                                       |    112 |   1.1 |  112 |   1.1
runtime.mapaccess2                                                                    |    151 |   1.4 |  106 |   1.0
