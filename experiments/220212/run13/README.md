### Right after run12, keeping the caches hot, with stack dup pushempty

```
make erigon && sudo nice --10 ./build/bin/erigon --datadir /media/route/sx8200/erigon/data/ --ethash.dagdir /media/route/sx8200/erigon/ethash/ --nodiscover --port 30123 |& tee -i ...
```
```
sudo time perf record -F 97 -agC 3
^C[ perf record: Woken up 9 times to write data ]
[ perf record: Captured and wrote 2.470 MB perf.data (10458 samples) ]
Command terminated by signal 2
0.08user 0.18system 1:49.21elapsed 0%CPU (0avgtext+0avgdata 24472maxresident)k
0inputs+16outputs (1major+4223minor)pagefaults 0swaps
```

#### stack_top_own

                                         Name                                         | Shared |   %   | Own  |   %
--------------------------------------------------------------------------------------|--------|-------|------|------
github.com/ledgerwatch/erigon/core/vm.(*EVMInterpreter).Run                           |   5696 |  54.5 | 1801 |  17.2
golang.org/x/crypto/sha3.keccakF1600                                                  |    755 |   7.2 |  753 |   7.2
cmpbody                                                                               |    492 |   4.7 |  492 |   4.7
runtime.mallocgc                                                                      |    880 |   8.4 |  446 |   4.3
github.com/ledgerwatch/erigon/ethdb/olddb.(*MutationItem).Less                        |    364 |   3.5 |  363 |   3.5
github.com/ledgerwatch/erigon/core/vm.makeDup.func1                                   |    230 |   2.2 |  228 |   2.2
mdbx_node_search                                                                      |    209 |   2.0 |  209 |   2.0
github.com/ledgerwatch/erigon/core/vm.(*Memory).Set32                                 |    199 |   1.9 |  199 |   1.9
mdbx_page_get_ex                                                                      |    253 |   2.4 |  187 |   1.8
aeshashbody                                                                           |    172 |   1.6 |  172 |   1.6
runtime.memclrNoHeapPointers                                                          |    171 |   1.6 |  165 |   1.6
github.com/ledgerwatch/erigon/core/vm.makeSwap.func1                                  |    162 |   1.5 |  161 |   1.5
github.com/google/btree.items.find.func1                                              |    957 |   9.2 |  159 |   1.5
github.com/ledgerwatch/erigon/core/vm.opPush1                                         |    146 |   1.4 |  146 |   1.4
github.com/ledgerwatch/erigon/core/vm.makePush.func1                                  |    204 |   2.0 |  136 |   1.3
runtime.memmove                                                                       |    133 |   1.3 |  128 |   1.2
runtime.heapBitsSetType                                                               |    125 |   1.2 |  125 |   1.2
runtime.mapaccess1                                                                    |    223 |   2.1 |  122 |   1.2
golang.org/x/crypto/sha3.(*state).padAndPermute                                       |    160 |   1.5 |  120 |   1.1
runtime.mapassign                                                                     |    310 |   3.0 |  119 |   1.1
