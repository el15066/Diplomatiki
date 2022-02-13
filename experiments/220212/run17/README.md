### Right after run16, keeping the caches hot, with push/dup/swap common

```
make erigon && sudo nice --10 ./build/bin/erigon --datadir /media/route/sx8200/erigon/data/ --ethash.dagdir /media/route/sx8200/erigon/ethash/ --nodiscover --port 30123 |& tee -i ...
```
```
sudo time perf record -F 97 -agC 3
[ perf record: Woken up 10 times to write data ]
[ perf record: Captured and wrote 2.497 MB perf.data (10599 samples) ]
Command terminated by signal 2
0.09user 0.17system 2:17.24elapsed 0%CPU (0avgtext+0avgdata 24392maxresident)k
0inputs+16outputs (1major+4224minor)pagefaults 0swaps
```
[ perf record: Woken up 10 times to write data ]
[ perf record: Captured and wrote 2.498 MB perf.data (10592 samples) ]
Command terminated by signal 2
0.08user 0.18system 1:50.20elapsed 0%CPU (0avgtext+0avgdata 24444maxresident)k
0inputs+16outputs (1major+4219minor)pagefaults 0swaps
```

#### stack_top_own

Name                                                                                  | Shared |   %   | Own  |   %
--------------------------------------------------------------------------------------|--------|-------|------|------
github.com/ledgerwatch/erigon/core/vm.(*EVMInterpreter).Run                           |   5907 |  55.8 | 1824 |  17.2
golang.org/x/crypto/sha3.keccakF1600                                                  |    788 |   7.4 |  787 |   7.4
cmpbody                                                                               |    479 |   4.5 |  478 |   4.5
runtime.mallocgc                                                                      |    873 |   8.2 |  433 |   4.1
github.com/ledgerwatch/erigon/ethdb/olddb.(*MutationItem).Less                        |    393 |   3.7 |  393 |   3.7
github.com/ledgerwatch/erigon/core/vm.opPushCommon                                    |    430 |   4.1 |  304 |   2.9
github.com/ledgerwatch/erigon/core/vm.opDupCommon                                     |    280 |   2.6 |  279 |   2.6
github.com/ledgerwatch/erigon/core/vm.(*Memory).Set32                                 |    212 |   2.0 |  211 |   2.0
mdbx_node_search                                                                      |    192 |   1.8 |  192 |   1.8
mdbx_page_get_ex                                                                      |    253 |   2.4 |  173 |   1.6
github.com/google/btree.items.find.func1                                              |    986 |   9.3 |  162 |   1.5
github.com/ledgerwatch/erigon/core/vm.opSwapCommon                                    |    160 |   1.5 |  160 |   1.5
runtime.memclrNoHeapPointers                                                          |    162 |   1.5 |  156 |   1.5
aeshashbody                                                                           |    156 |   1.5 |  155 |   1.5
github.com/holiman/uint256.(*Int).SetBytes                                            |    192 |   1.8 |  155 |   1.5
runtime.memmove                                                                       |    140 |   1.3 |  137 |   1.3
runtime.heapBitsSetType                                                               |    131 |   1.2 |  131 |   1.2
github.com/ledgerwatch/erigon/core/vm.opJumpi                                         |    131 |   1.2 |  130 |   1.2
golang.org/x/crypto/sha3.(*state).padAndPermute                                       |    167 |   1.6 |  126 |   1.2
runtime.mapaccess1                                                                    |    203 |   1.9 |  108 |   1.0
