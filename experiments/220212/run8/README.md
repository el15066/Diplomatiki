### Right after run7, keeping the caches hot, with separate trees at mutation
Effective commit is 74337b05b

```
make erigon && sudo nice --10 ./build/bin/erigon --datadir /media/route/sx8200/erigon/data/ --ethash.dagdir /media/route/sx8200/erigon/ethash/ --nodiscover --port 30123 |& tee -i ...
```
```
sudo time perf record -F 97 -agC 3
^C[ perf record: Woken up 10 times to write data ]
[ perf record: Captured and wrote 2.487 MB perf.data (10505 samples) ]
Command terminated by signal 2
0.10user 0.16system 1:50.21elapsed 0%CPU (0avgtext+0avgdata 24336maxresident)k
0inputs+16outputs (1major+4224minor)pagefaults 0swaps
```

#### stack_top_own

Name                                                                                | Shared |   %   | Own  |   %
------------------------------------------------------------------------------------|--------|-------|------|------
github.com/ledgerwatch/erigon/core/vm.(*EVMInterpreter).Run                         |   5843 |  55.6 | 1857 |  17.7
golang.org/x/crypto/sha3.keccakF1600                                                |    760 |   7.2 |  760 |   7.2
cmpbody                                                                             |    464 |   4.4 |  464 |   4.4
github.com/ledgerwatch/erigon/ethdb/olddb.(*MutationItem).Less                      |    410 |   3.9 |  407 |   3.9
runtime.mallocgc                                                                    |    825 |   7.9 |  407 |   3.9
github.com/ledgerwatch/erigon/core/vm.makeDup.func1                                 |    292 |   2.8 |  291 |   2.8
mdbx_node_search                                                                    |    242 |   2.3 |  241 |   2.3
github.com/ledgerwatch/erigon/core/vm.(*Memory).Set32                               |    201 |   1.9 |  201 |   1.9
github.com/ledgerwatch/erigon/core/vm.opPush1                                       |    165 |   1.6 |  165 |   1.6
github.com/ledgerwatch/erigon/core/vm.makeSwap.func1                                |    160 |   1.5 |  160 |   1.5
aeshashbody                                                                         |    153 |   1.5 |  153 |   1.5
github.com/google/btree.items.find.func1                                            |    992 |   9.4 |  153 |   1.5
mdbx_page_get_ex                                                                    |    200 |   1.9 |  147 |   1.4
runtime.memmove                                                                     |    152 |   1.4 |  146 |   1.4
runtime.memclrNoHeapPointers                                                        |    146 |   1.4 |  140 |   1.3
runtime.heapBitsSetType                                                             |    129 |   1.2 |  128 |   1.2
runtime.mapaccess1                                                                  |    230 |   2.2 |  125 |   1.2
golang.org/x/crypto/sha3.(*state).padAndPermute                                     |    190 |   1.8 |  121 |   1.2
github.com/ledgerwatch/erigon/core/vm.makePush.func1                                |    171 |   1.6 |  119 |   1.1
github.com/ledgerwatch/erigon/core/vm.opJumpi                                       |    123 |   1.2 |  118 |   1.1
