### Right after run13, keeping the caches hot, with stack 128

```
make erigon && sudo nice --10 ./build/bin/erigon --datadir /media/route/sx8200/erigon/data/ --ethash.dagdir /media/route/sx8200/erigon/ethash/ --nodiscover --port 30123 |& tee -i ...
```
```
sudo time perf record -F 97 -agC 3
^C[ perf record: Woken up 9 times to write data ]
[ perf record: Captured and wrote 2.460 MB perf.data (10536 samples) ]
Command terminated by signal 2
0.07user 0.19system 1:50.21elapsed 0%CPU (0avgtext+0avgdata 24240maxresident)k
0inputs+24outputs (1major+4221minor)pagefaults 0swaps
```

#### stack_top_own

Name                                                                                  | Shared |   %   | Own  |   %
--------------------------------------------------------------------------------------|--------|-------|------|------
github.com/ledgerwatch/erigon/core/vm.(*EVMInterpreter).Run                           |   5695 |  54.1 | 1835 |  17.4
golang.org/x/crypto/sha3.keccakF1600                                                  |    844 |   8.0 |  844 |   8.0
cmpbody                                                                               |    482 |   4.6 |  482 |   4.6
runtime.mallocgc                                                                      |    836 |   7.9 |  400 |   3.8
github.com/ledgerwatch/erigon/ethdb/olddb.(*MutationItem).Less                        |    375 |   3.6 |  375 |   3.6
mdbx_node_search                                                                      |    225 |   2.1 |  224 |   2.1
github.com/ledgerwatch/erigon/core/vm.makeDup.func1                                   |    217 |   2.1 |  217 |   2.1
github.com/ledgerwatch/erigon/core/vm.(*Memory).Set32                                 |    190 |   1.8 |  190 |   1.8
github.com/ledgerwatch/erigon/core/vm.makeSwap.func1                                  |    182 |   1.7 |  182 |   1.7
aeshashbody                                                                           |    170 |   1.6 |  170 |   1.6
mdbx_page_get_ex                                                                      |    229 |   2.2 |  158 |   1.5
github.com/google/btree.items.find.func1                                              |    966 |   9.2 |  157 |   1.5
github.com/ledgerwatch/erigon/core/vm.opPush1                                         |    154 |   1.5 |  154 |   1.5
github.com/ledgerwatch/erigon/core/vm.makePush.func1                                  |    234 |   2.2 |  153 |   1.5
runtime.memclrNoHeapPointers                                                          |    157 |   1.5 |  152 |   1.4
runtime.memmove                                                                       |    143 |   1.4 |  138 |   1.3
runtime.heapBitsSetType                                                               |    133 |   1.3 |  133 |   1.3
runtime.mapassign                                                                     |    304 |   2.9 |  129 |   1.2
golang.org/x/crypto/sha3.(*state).padAndPermute                                       |    160 |   1.5 |  124 |   1.2
runtime.mapaccess2                                                                    |    156 |   1.5 |  110 |   1.0
