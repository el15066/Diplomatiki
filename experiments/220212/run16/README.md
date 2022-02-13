### Right after run15, keeping the caches hot, rerun of run14
Effective commit is d0caef522

```
make erigon && sudo nice --10 ./build/bin/erigon --datadir /media/route/sx8200/erigon/data/ --ethash.dagdir /media/route/sx8200/erigon/ethash/ --nodiscover --port 30123 |& tee ...
```
```
sudo time perf record -F 97 -agC 3
[ perf record: Woken up 9 times to write data ]
[ perf record: Captured and wrote 2.454 MB perf.data (10405 samples) ]
Command terminated by signal 2
0.06user 0.21system 1:49.21elapsed 0%CPU (0avgtext+0avgdata 24272maxresident)k
0inputs+16outputs (1major+4227minor)pagefaults 0swaps
```

#### stack_top_own

                                         Name                                         | Shared |   %   | Own  |   %
--------------------------------------------------------------------------------------|--------|-------|------|------
github.com/ledgerwatch/erigon/core/vm.(*EVMInterpreter).Run                           |   5718 |  55.0 | 1846 |  17.7
golang.org/x/crypto/sha3.keccakF1600                                                  |    746 |   7.2 |  746 |   7.2
cmpbody                                                                               |    483 |   4.6 |  482 |   4.6
runtime.mallocgc                                                                      |    845 |   8.1 |  424 |   4.1
github.com/ledgerwatch/erigon/ethdb/olddb.(*MutationItem).Less                        |    371 |   3.6 |  371 |   3.6
github.com/ledgerwatch/erigon/core/vm.makeDup.func1                                   |    219 |   2.1 |  219 |   2.1
mdbx_node_search                                                                      |    214 |   2.1 |  214 |   2.1
github.com/ledgerwatch/erigon/core/vm.(*Memory).Set32                                 |    212 |   2.0 |  212 |   2.0
github.com/google/btree.items.find.func1                                              |    993 |   9.5 |  174 |   1.7
aeshashbody                                                                           |    169 |   1.6 |  169 |   1.6
github.com/ledgerwatch/erigon/core/vm.makeSwap.func1                                  |    164 |   1.6 |  163 |   1.6
mdbx_page_get_ex                                                                      |    224 |   2.2 |  154 |   1.5
github.com/ledgerwatch/erigon/core/vm.makePush.func1                                  |    206 |   2.0 |  141 |   1.4
runtime.memclrNoHeapPointers                                                          |    141 |   1.4 |  138 |   1.3
runtime.heapBitsSetType                                                               |    135 |   1.3 |  135 |   1.3
runtime.memmove                                                                       |    138 |   1.3 |  135 |   1.3
github.com/ledgerwatch/erigon/core/vm.opPush1                                         |    135 |   1.3 |  135 |   1.3
runtime.mapassign                                                                     |    319 |   3.1 |  121 |   1.2
golang.org/x/crypto/sha3.(*state).padAndPermute                                       |    174 |   1.7 |  119 |   1.1
runtime.mapaccess1                                                                    |    225 |   2.2 |  116 |   1.1
