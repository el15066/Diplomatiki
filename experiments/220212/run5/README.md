### Right after run4, keeping the caches hot, with new mi.Less()
Effective commit is 15b3b62c0

```
make erigon && sudo nice --10 ./build/bin/erigon --datadir /media/route/sx8200/erigon/data/ --ethash.dagdir /media/route/sx8200/erigon/ethash/ --nodiscover --port 30123 |& tee ...
```
```
sudo time perf record -F 97 -agC 3
^C[ perf record: Woken up 14 times to write data ]
[ perf record: Captured and wrote 3.513 MB perf.data (13827 samples) ]
Command terminated by signal 2
0.07user 0.19system 2:25.24elapsed 0%CPU (0avgtext+0avgdata 25276maxresident)k
0inputs+16outputs (1major+4240minor)pagefaults 0swaps
```

#### stack_top_own

Name                                                                                  | Shared |   %   | Own  |   %
--------------------------------------------------------------------------------------|--------|-------|------|------
github.com/ledgerwatch/erigon/core/vm.(*EVMInterpreter).Run                           |   7668 |  55.5 | 1817 |  13.1
runtime.mallocgc                                                                      |   2073 |  15.0 | 1193 |   8.6
runtime.memmove                                                                       |    938 |   6.8 |  928 |   6.7
golang.org/x/crypto/sha3.keccakF1600                                                  |    775 |   5.6 |  772 |   5.6
github.com/ledgerwatch/erigon/ethdb/olddb.(*MutationItem).Less                        |   3550 |  25.7 |  770 |   5.6
runtime.concatstrings                                                                 |   1342 |   9.7 |  392 |   2.8
github.com/ledgerwatch/erigon/core/vm.makeDup.func1                                   |    280 |   2.0 |  280 |   2.0
runtime.memclrNoHeapPointers                                                          |    265 |   1.9 |  258 |   1.9
cmpbody                                                                               |    230 |   1.7 |  230 |   1.7
mdbx_node_search                                                                      |    218 |   1.6 |  218 |   1.6
github.com/google/btree.items.find.func1                                              |   3516 |  25.4 |  200 |   1.4
github.com/ledgerwatch/erigon/core/vm.(*Memory).Set32                                 |    198 |   1.4 |  198 |   1.4
github.com/ledgerwatch/erigon/core/vm.makeSwap.func1                                  |    169 |   1.2 |  168 |   1.2
github.com/ledgerwatch/erigon/core/vm.makePush.func1                                  |    209 |   1.5 |  157 |   1.1
mdbx_page_get_ex                                                                      |    207 |   1.5 |  155 |   1.1
aeshashbody                                                                           |    153 |   1.1 |  153 |   1.1
runtime.heapBitsSetType                                                               |    134 |   1.0 |  134 |   1.0
runtime.rawstringtmp                                                                  |    965 |   7.0 |  130 |   0.9
golang.org/x/crypto/sha3.(*state).padAndPermute                                       |    177 |   1.3 |  130 |   0.9
runtime.mapassign                                                                     |    338 |   2.4 |  124 |   0.9
