### Right after run11, keeping the caches hot, with stack dup no pointer

```
make erigon && sudo nice --10 ./build/bin/erigon --datadir /media/route/sx8200/erigon/data/ --ethash.dagdir /media/route/sx8200/erigon/ethash/ --nodiscover --port 30123 |& tee -i ...
```
```
sudo time perf record -F 97 -agC 3
^C[ perf record: Woken up 10 times to write data ]
[ perf record: Captured and wrote 2.485 MB perf.data (10496 samples) ]
Command terminated by signal 2
0.09user 0.17system 1:50.21elapsed 0%CPU (0avgtext+0avgdata 24340maxresident)k
0inputs+16outputs (1major+4223minor)pagefaults 0swaps
```

#### stack_top_own

                                         Name                                         | Shared |   %   | Own  |   %
--------------------------------------------------------------------------------------|--------|-------|------|------
github.com/ledgerwatch/erigon/core/vm.(*EVMInterpreter).Run                           |   5829 |  55.5 | 1871 |  17.8
golang.org/x/crypto/sha3.keccakF1600                                                  |    780 |   7.4 |  779 |   7.4
cmpbody                                                                               |    465 |   4.4 |  465 |   4.4
runtime.mallocgc                                                                      |    846 |   8.1 |  385 |   3.7
github.com/ledgerwatch/erigon/ethdb/olddb.(*MutationItem).Less                        |    353 |   3.4 |  353 |   3.4
github.com/ledgerwatch/erigon/core/vm.makeDup.func1                                   |    286 |   2.7 |  285 |   2.7
github.com/ledgerwatch/erigon/core/vm.(*Memory).Set32                                 |    236 |   2.2 |  236 |   2.2
mdbx_node_search                                                                      |    203 |   1.9 |  203 |   1.9
github.com/ledgerwatch/erigon/core/vm.opPush1                                         |    174 |   1.7 |  173 |   1.6
mdbx_page_get_ex                                                                      |    226 |   2.2 |  168 |   1.6
aeshashbody                                                                           |    168 |   1.6 |  168 |   1.6
github.com/ledgerwatch/erigon/core/vm.makeSwap.func1                                  |    162 |   1.5 |  162 |   1.5
runtime.memclrNoHeapPointers                                                          |    158 |   1.5 |  155 |   1.5
runtime.heapBitsSetType                                                               |    138 |   1.3 |  138 |   1.3
github.com/google/btree.items.find.func1                                              |    902 |   8.6 |  137 |   1.3
runtime.memmove                                                                       |    139 |   1.3 |  134 |   1.3
github.com/ledgerwatch/erigon/core/vm.makePush.func1                                  |    202 |   1.9 |  128 |   1.2
golang.org/x/crypto/sha3.(*state).padAndPermute                                       |    179 |   1.7 |  127 |   1.2
runtime.mapaccess1                                                                    |    234 |   2.2 |  115 |   1.1
runtime.mapassign                                                                     |    294 |   2.8 |  112 |   1.1
