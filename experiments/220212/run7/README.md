### Right after run6, keeping the caches hot, rerun of run4 with same # of blocks
Effective commit is 0c9cbf19c

```
make erigon && sudo nice --10 ./build/bin/erigon --datadir /media/route/sx8200/erigon/data/ --ethash.dagdir /media/route/sx8200/erigon/ethash/ --nodiscover --port 30123 |& tee ...
```
```
sudo time perf record -F 97 -agC 3
^C[ perf record: Woken up 10 times to write data ]
[ perf record: Captured and wrote 2.513 MB perf.data (10606 samples) ]
Command terminated by signal 2
0.08user 0.18system 1:51.21elapsed 0%CPU (0avgtext+0avgdata 24300maxresident)k
0inputs+16outputs (1major+4230minor)pagefaults 0swaps
```

#### stack_top_own

                                         Name                                         | Shared |   %   | Own  |   %
--------------------------------------------------------------------------------------|--------|-------|------|------
github.com/ledgerwatch/erigon/core/vm.(*EVMInterpreter).Run                           |   5900 |  55.6 | 1906 |  18.0
golang.org/x/crypto/sha3.keccakF1600                                                  |    748 |   7.1 |  745 |   7.0
cmpbody                                                                               |    478 |   4.5 |  476 |   4.5
runtime.mallocgc                                                                      |    842 |   7.9 |  423 |   4.0
github.com/ledgerwatch/erigon/ethdb/olddb.(*MutationItem).Less                        |    391 |   3.7 |  391 |   3.7
github.com/ledgerwatch/erigon/core/vm.makeDup.func1                                   |    275 |   2.6 |  274 |   2.6
mdbx_node_search                                                                      |    212 |   2.0 |  212 |   2.0
github.com/ledgerwatch/erigon/core/vm.(*Memory).Set32                                 |    195 |   1.8 |  194 |   1.8
aeshashbody                                                                           |    164 |   1.5 |  164 |   1.5
github.com/ledgerwatch/erigon/core/vm.makePush.func1                                  |    218 |   2.1 |  152 |   1.4
mdbx_page_get_ex                                                                      |    212 |   2.0 |  151 |   1.4
github.com/ledgerwatch/erigon/core/vm.makeSwap.func1                                  |    152 |   1.4 |  151 |   1.4
github.com/ledgerwatch/erigon/core/vm.opPush1                                         |    150 |   1.4 |  149 |   1.4
github.com/ledgerwatch/erigon/core/vm.opJumpi                                         |    142 |   1.3 |  140 |   1.3
runtime.heapBitsSetType                                                               |    139 |   1.3 |  138 |   1.3
github.com/google/btree.items.find.func1                                              |    964 |   9.1 |  135 |   1.3
runtime.memmove                                                                       |    139 |   1.3 |  132 |   1.2
golang.org/x/crypto/sha3.(*state).padAndPermute                                       |    182 |   1.7 |  126 |   1.2
runtime.memclrNoHeapPointers                                                          |    120 |   1.1 |  116 |   1.1
runtime.mapaccess1                                                                    |    200 |   1.9 |  111 |   1.0
