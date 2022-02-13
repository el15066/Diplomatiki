### Right after run1, but perf records everything on the spicific core it's running at, instead of only the erigon process on all cores
Note: perf record was stopped by hand just before erigon exited.

```
make erigon && sudo nice --10 ./build/bin/erigon --datadir /media/route/sx8200/erigon/data/ --ethash.dagdir /media/route/sx8200/erigon/ethash/ --nodiscover --port 30123 |& tee ...
```
```
sudo time perf record -F 97 -agC 3
^C[ perf record: Woken up 60 times to write data ]
[ perf record: Captured and wrote 15.032 MB perf.data (67163 samples) ]
Command terminated by signal 2
0.08user 0.21system 11:33.80elapsed 0%CPU (0avgtext+0avgdata 37124maxresident)k
0inputs+16outputs (1major+4429minor)pagefaults 0swaps
```

#### stack_top_own

                                         Name                                         | Shared |   %   |  Own  |   %
--------------------------------------------------------------------------------------|--------|-------|-------|------
github.com/ledgerwatch/erigon/core/vm.(*EVMInterpreter).Run                           |  38077 |  56.7 | 10359 |  15.4
golang.org/x/crypto/sha3.keccakF1600                                                  |   4600 |   6.8 |  4594 |   6.8
cmpbody                                                                               |   4062 |   6.0 |  4052 |   6.0
github.com/ledgerwatch/erigon/ethdb/olddb.(*MutationItem).Less                        |   3491 |   5.2 |  3482 |   5.2
runtime.mallocgc                                                                      |   4849 |   7.2 |  2437 |   3.6
github.com/ledgerwatch/erigon/core/vm.makeDup.func1                                   |   1750 |   2.6 |  1747 |   2.6
github.com/ledgerwatch/erigon/core/vm.makePush.func1                                  |   2253 |   3.4 |  1730 |   2.6
github.com/ledgerwatch/erigon/core/vm.opPush1                                         |   1512 |   2.3 |  1510 |   2.2
github.com/ledgerwatch/erigon/core/vm.(*Memory).Set32                                 |   1340 |   2.0 |  1335 |   2.0
github.com/google/btree.items.find.func1                                              |   8547 |  12.7 |  1275 |   1.9
mdbx_node_search                                                                      |   1209 |   1.8 |  1209 |   1.8
github.com/ledgerwatch/erigon/core/vm.makeSwap.func1                                  |   1008 |   1.5 |  1007 |   1.5
mdbx_page_get_ex                                                                      |   1060 |   1.6 |   943 |   1.4
aeshashbody                                                                           |    914 |   1.4 |   914 |   1.4
runtime.heapBitsSetType                                                               |    800 |   1.2 |   798 |   1.2
github.com/ledgerwatch/erigon/core/vm.opJumpi                                         |    820 |   1.2 |   748 |   1.1
runtime.memmove                                                                       |    773 |   1.2 |   726 |   1.1
runtime.mapassign                                                                     |   1926 |   2.9 |   721 |   1.1
runtime.memclrNoHeapPointers                                                          |    734 |   1.1 |   711 |   1.1
golang.org/x/crypto/sha3.(*state).padAndPermute                                       |    968 |   1.4 |   683 |   1.0
