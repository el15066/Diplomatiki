### Cold caches, same as run2, but with caches cleared first
Note: perf record was stopped by hand just before erigon exited.

```
echo 3 | sudo tee /proc/sys/vm/drop_caches && make erigon && sleep 22 && sudo nice --10 ./build/bin/erigon --datadir /media/route/sx8200/erigon/data/ --ethash.dagdir /media/route/sx8200/erigon/ethash/ --nodiscover --port 30123 |& tee ...
```
```
sudo time perf record -F 97 -agC 3
^C[ perf record: Woken up 72 times to write data ]
[ perf record: Captured and wrote 18.173 MB perf.data (82202 samples) ]
Command terminated by signal 2
0.08user 0.23system 14:09.02elapsed 0%CPU (0avgtext+0avgdata 40332maxresident)k
37752inputs+16outputs (98major+4405minor)pagefaults 0swaps
```

#### stack_top_own

                                         Name                                         | Shared |   %   |  Own  |   %
--------------------------------------------------------------------------------------|--------|-------|-------|------
github.com/ledgerwatch/erigon/core/vm.(*EVMInterpreter).Run                           |  44797 |  54.5 | 12251 |  14.9
golang.org/x/crypto/sha3.keccakF1600                                                  |   5445 |   6.6 |  5435 |   6.6
cmpbody                                                                               |   5013 |   6.1 |  5009 |   6.1
github.com/ledgerwatch/erigon/ethdb/olddb.(*MutationItem).Less                        |   4098 |   5.0 |  4093 |   5.0
runtime.mallocgc                                                                      |   5685 |   6.9 |  2887 |   3.5
github.com/ledgerwatch/erigon/core/vm.makePush.func1                                  |   2614 |   3.2 |  2034 |   2.5
github.com/ledgerwatch/erigon/core/vm.makeDup.func1                                   |   2037 |   2.5 |  2031 |   2.5
github.com/ledgerwatch/erigon/core/vm.opPush1                                         |   1814 |   2.2 |  1812 |   2.2
github.com/ledgerwatch/erigon/core/vm.(*Memory).Set32                                 |   1545 |   1.9 |  1543 |   1.9
mdbx_node_search                                                                      |   1471 |   1.8 |  1467 |   1.8
github.com/google/btree.items.find.func1                                              |  10236 |  12.5 |  1464 |   1.8
github.com/ledgerwatch/erigon/core/vm.makeSwap.func1                                  |   1205 |   1.5 |  1203 |   1.5
mdbx_page_get_ex                                                                      |   3152 |   3.8 |  1116 |   1.4
aeshashbody                                                                           |   1073 |   1.3 |  1072 |   1.3
runtime.heapBitsSetType                                                               |    895 |   1.1 |   895 |   1.1
runtime.mapassign                                                                     |   2274 |   2.8 |   862 |   1.0
runtime.memclrNoHeapPointers                                                          |    854 |   1.0 |   832 |   1.0
golang.org/x/crypto/sha3.(*state).padAndPermute                                       |   1181 |   1.4 |   827 |   1.0
sort.Search                                                                           |  11031 |  13.4 |   809 |   1.0
github.com/ledgerwatch/erigon/core/vm.opJumpi                                         |    890 |   1.1 |   808 |   1.0
