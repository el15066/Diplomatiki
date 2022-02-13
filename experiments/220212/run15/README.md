### Right after run14, keeping the caches hot, with push/dup/swap split out

```
make erigon && sudo nice --10 ./build/bin/erigon --datadir /media/route/sx8200/erigon/data/ --ethash.dagdir /media/route/sx8200/erigon/ethash/ --nodiscover --port 30123 |& tee -i ...
```
```
sudo time perf record -F 97 -agC 3
[ perf record: Woken up 10 times to write data ]
[ perf record: Captured and wrote 2.496 MB perf.data (10601 samples) ]
Command terminated by signal 2
0.08user 0.18system 1:51.21elapsed 0%CPU (0avgtext+0avgdata 24372maxresident)k
0inputs+16outputs (1major+4234minor)pagefaults 0swaps
```

#### stack_top_own

Name                                                                                  | Shared |   %   | Own  |   %
--------------------------------------------------------------------------------------|--------|-------|------|------
github.com/ledgerwatch/erigon/core/vm.(*EVMInterpreter).Run                           |   5902 |  55.7 | 1903 |  18.0
golang.org/x/crypto/sha3.keccakF1600                                                  |    730 |   6.9 |  727 |   6.9
cmpbody                                                                               |    452 |   4.3 |  451 |   4.3
runtime.mallocgc                                                                      |    841 |   7.9 |  401 |   3.8
github.com/ledgerwatch/erigon/ethdb/olddb.(*MutationItem).Less                        |    389 |   3.7 |  388 |   3.7
github.com/ledgerwatch/erigon/core/vm.(*Memory).Set32                                 |    220 |   2.1 |  220 |   2.1
mdbx_node_search                                                                      |    207 |   2.0 |  207 |   2.0
aeshashbody                                                                           |    166 |   1.6 |  166 |   1.6
mdbx_page_get_ex                                                                      |    235 |   2.2 |  165 |   1.6
runtime.memmove                                                                       |    165 |   1.6 |  159 |   1.5
github.com/ledgerwatch/erigon/core/vm.opPush1                                         |    195 |   1.8 |  146 |   1.4
github.com/google/btree.items.find.func1                                              |    934 |   8.8 |  145 |   1.4
github.com/ledgerwatch/erigon/core/vm.opJumpi                                         |    148 |   1.4 |  144 |   1.4
github.com/holiman/uint256.(*Int).SetBytes                                            |    174 |   1.6 |  140 |   1.3
runtime.heapBitsSetType                                                               |    139 |   1.3 |  139 |   1.3
runtime.memclrNoHeapPointers                                                          |    140 |   1.3 |  137 |   1.3
runtime.mapassign                                                                     |    338 |   3.2 |  131 |   1.2
golang.org/x/crypto/sha3.(*state).padAndPermute                                       |    160 |   1.5 |  125 |   1.2
runtime.mapaccess1                                                                    |    210 |   2.0 |  112 |   1.1
sort.Search                                                                           |   1041 |   9.8 |  100 |   0.9
