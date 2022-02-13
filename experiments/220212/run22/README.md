### Automated

```
[ perf record: Woken up 16 times to write data ]
[ perf record: Captured and wrote 4.055 MB /tmp2/p (19070 samples) ]
Wall time: 97.803 seconds
```

#### stack_top_own

                                         Name                                         | Shared |   %   | Own  |   %
--------------------------------------------------------------------------------------|--------|-------|------|------
github.com/ledgerwatch/erigon/core/vm.(*EVMInterpreter).Run                           |   8991 |  47.1 | 2510 |  13.2
golang.org/x/crypto/sha3.keccakF1600                                                  |   1528 |   8.0 | 1525 |   8.0
cmpbody                                                                               |    973 |   5.1 |  972 |   5.1
runtime.mallocgc                                                                      |   1716 |   9.0 |  812 |   4.3
github.com/ledgerwatch/erigon/ethdb/olddb.(*MutationItem).Less                        |    724 |   3.8 |  724 |   3.8
mdbx_node_search                                                                      |    445 |   2.3 |  443 |   2.3
github.com/ledgerwatch/erigon/core/vm.makeDup.func1                                   |    378 |   2.0 |  378 |   2.0
mdbx_page_get_ex                                                                      |    515 |   2.7 |  361 |   1.9
aeshashbody                                                                           |    329 |   1.7 |  328 |   1.7
runtime.memclrNoHeapPointers                                                          |    323 |   1.7 |  316 |   1.7
github.com/google/btree.items.find.func1                                              |   1905 |  10.0 |  303 |   1.6
runtime.memmove                                                                       |    303 |   1.6 |  291 |   1.5
runtime.heapBitsSetType                                                               |    288 |   1.5 |  287 |   1.5
golang.org/x/crypto/sha3.(*state).padAndPermute                                       |    348 |   1.8 |  264 |   1.4
github.com/ledgerwatch/erigon/core/vm.makeSwap.func1                                  |    256 |   1.3 |  255 |   1.3
github.com/ledgerwatch/erigon/core/vm.makePush.func1                                  |    372 |   2.0 |  238 |   1.2
runtime.mapassign                                                                     |    656 |   3.4 |  232 |   1.2
runtime.mapaccess1                                                                    |    444 |   2.3 |  230 |   1.2
github.com/ledgerwatch/erigon/core/vm.opJumpi                                         |    222 |   1.2 |  216 |   1.1
github.com/ledgerwatch/erigon/core/vm.opPush1                                         |    209 |   1.1 |  209 |   1.1
