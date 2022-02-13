### Automated

```
[ perf record: Woken up 16 times to write data ]
[ perf record: Captured and wrote 4.105 MB /tmp2/p (19267 samples) ]
Wall time: 98.800 seconds
```

#### stack_top_own

                                         Name                                         | Shared |   %   | Own  |   %
--------------------------------------------------------------------------------------|--------|-------|------|------
github.com/ledgerwatch/erigon/core/vm.(*EVMInterpreter).Run                           |   9089 |  47.2 | 2482 |  12.9
golang.org/x/crypto/sha3.keccakF1600                                                  |   1600 |   8.3 | 1595 |   8.3
cmpbody                                                                               |   1019 |   5.3 | 1018 |   5.3
runtime.mallocgc                                                                      |   1782 |   9.2 |  828 |   4.3
github.com/ledgerwatch/erigon/ethdb/olddb.(*MutationItem).Less                        |    745 |   3.9 |  744 |   3.9
mdbx_node_search                                                                      |    441 |   2.3 |  440 |   2.3
github.com/google/btree.items.find.func1                                              |   1995 |  10.4 |  326 |   1.7
runtime.memclrNoHeapPointers                                                          |    335 |   1.7 |  322 |   1.7
mdbx_page_get_ex                                                                      |    436 |   2.3 |  306 |   1.6
runtime.memmove                                                                       |    319 |   1.7 |  304 |   1.6
runtime.heapBitsSetType                                                               |    294 |   1.5 |  294 |   1.5
aeshashbody                                                                           |    290 |   1.5 |  290 |   1.5
github.com/holiman/uint256.(*Int).SetBytes                                            |    347 |   1.8 |  278 |   1.4
runtime.mapassign                                                                     |    656 |   3.4 |  257 |   1.3
github.com/ledgerwatch/erigon/core/vm.opPush1                                         |    351 |   1.8 |  241 |   1.3
golang.org/x/crypto/sha3.(*state).padAndPermute                                       |    314 |   1.6 |  236 |   1.2
github.com/ledgerwatch/erigon/core/vm.opJumpi                                         |    217 |   1.1 |  209 |   1.1
runtime.mapaccess1                                                                    |    391 |   2.0 |  197 |   1.0
runtime.mapaccess2                                                                    |    266 |   1.4 |  192 |   1.0
github.com/ledgerwatch/erigon/core/vm.opMstore                                        |    246 |   1.3 |  174 |   0.9
