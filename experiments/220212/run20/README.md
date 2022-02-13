### Automated

```
[ perf record: Woken up 16 times to write data ]
[ perf record: Captured and wrote 4.110 MB /tmp2/p (19278 samples) ]
Wall time: 98.846 seconds
```

#### stack_top_own

Name                                                                                  | Shared |   %   | Own  |   %
--------------------------------------------------------------------------------------|--------|-------|------|------
github.com/ledgerwatch/erigon/core/vm.(*EVMInterpreter).Run                           |   9288 |  48.2 | 2478 |  12.9
golang.org/x/crypto/sha3.keccakF1600                                                  |   1559 |   8.1 | 1552 |   8.1
cmpbody                                                                               |    976 |   5.1 |  974 |   5.1
runtime.mallocgc                                                                      |   1760 |   9.1 |  820 |   4.3
github.com/ledgerwatch/erigon/ethdb/olddb.(*MutationItem).Less                        |    759 |   3.9 |  757 |   3.9
github.com/ledgerwatch/erigon/core/vm.opPushCommon                                    |    742 |   3.8 |  477 |   2.5
mdbx_node_search                                                                      |    450 |   2.3 |  448 |   2.3
github.com/ledgerwatch/erigon/core/vm.opDupCommon                                     |    437 |   2.3 |  436 |   2.3
mdbx_page_get_ex                                                                      |    491 |   2.5 |  335 |   1.7
github.com/ledgerwatch/erigon/core/vm.opSwapCommon                                    |    317 |   1.6 |  317 |   1.6
runtime.memmove                                                                       |    323 |   1.7 |  308 |   1.6
github.com/holiman/uint256.(*Int).SetBytes                                            |    381 |   2.0 |  307 |   1.6
aeshashbody                                                                           |    304 |   1.6 |  304 |   1.6
runtime.memclrNoHeapPointers                                                          |    307 |   1.6 |  303 |   1.6
github.com/google/btree.items.find.func1                                              |   1932 |  10.0 |  301 |   1.6
runtime.heapBitsSetType                                                               |    282 |   1.5 |  281 |   1.5
golang.org/x/crypto/sha3.(*state).padAndPermute                                       |    334 |   1.7 |  257 |   1.3
runtime.mapassign                                                                     |    647 |   3.4 |  246 |   1.3
runtime.mapaccess1                                                                    |    402 |   2.1 |  225 |   1.2
runtime.mapaccess2                                                                    |    297 |   1.5 |  216 |   1.1
