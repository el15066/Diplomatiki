### Right after run8, rerun
Effective commit is 74337b05b

```
make erigon && sudo nice --10 ./build/bin/erigon --datadir /media/route/sx8200/erigon/data/ --ethash.dagdir /media/route/sx8200/erigon/ethash/ --nodiscover --port 30123 |& tee -i ...
```
```
sudo time perf record -F 97 -agC 3
^C[ perf record: Woken up 10 times to write data ]
[ perf record: Captured and wrote 2.490 MB perf.data (10511 samples) ]
Command terminated by signal 2
0.08user 0.18system 1:50.21elapsed 0%CPU (0avgtext+0avgdata 24344maxresident)k
0inputs+16outputs (1major+4218minor)pagefaults 0swaps
```

#### stack_top_own

                                         Name                                         | Shared |   %   | Own  |   %
--------------------------------------------------------------------------------------|--------|-------|------|------
github.com/ledgerwatch/erigon/core/vm.(*EVMInterpreter).Run                           |   5803 |  55.2 | 1847 |  17.6
golang.org/x/crypto/sha3.keccakF1600                                                  |    775 |   7.4 |  773 |   7.4
cmpbody                                                                               |    453 |   4.3 |  453 |   4.3
runtime.mallocgc                                                                      |    843 |   8.0 |  384 |   3.7
github.com/ledgerwatch/erigon/ethdb/olddb.(*MutationItem).Less                        |    366 |   3.5 |  366 |   3.5
github.com/ledgerwatch/erigon/core/vm.makeDup.func1                                   |    264 |   2.5 |  264 |   2.5
github.com/ledgerwatch/erigon/core/vm.(*Memory).Set32                                 |    208 |   2.0 |  208 |   2.0
mdbx_node_search                                                                      |    190 |   1.8 |  190 |   1.8
aeshashbody                                                                           |    166 |   1.6 |  166 |   1.6
github.com/ledgerwatch/erigon/core/vm.makePush.func1                                  |    224 |   2.1 |  166 |   1.6
mdbx_page_get_ex                                                                      |    234 |   2.2 |  155 |   1.5
github.com/ledgerwatch/erigon/core/vm.makeSwap.func1                                  |    155 |   1.5 |  154 |   1.5
github.com/ledgerwatch/erigon/core/vm.opPush1                                         |    153 |   1.5 |  153 |   1.5
github.com/google/btree.items.find.func1                                              |    925 |   8.8 |  152 |   1.4
runtime.memclrNoHeapPointers                                                          |    155 |   1.5 |  149 |   1.4
runtime.memmove                                                                       |    146 |   1.4 |  140 |   1.3
runtime.heapBitsSetType                                                               |    138 |   1.3 |  138 |   1.3
github.com/ledgerwatch/erigon/core/vm.opJumpi                                         |    138 |   1.3 |  133 |   1.3
golang.org/x/crypto/sha3.(*state).padAndPermute                                       |    154 |   1.5 |  120 |   1.1
sort.Search                                                                           |   1040 |   9.9 |  112 |   1.1
