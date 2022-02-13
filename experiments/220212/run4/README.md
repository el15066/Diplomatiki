### Right after run3, keeping the caches hot, with new Push()
Effective commit is 0c9cbf19c

```
make erigon && sudo nice --10 ./build/bin/erigon --datadir /media/route/sx8200/erigon/data/ --ethash.dagdir /media/route/sx8200/erigon/ethash/ --nodiscover --port 30123 |& tee ...
```
```
sudo time perf record -F 97 -agC 3
^C[ perf record: Woken up 52 times to write data ]
[ perf record: Captured and wrote 13.003 MB perf.data (58133 samples) ]
Command terminated by signal 2
0.09user 0.19system 10:02.70elapsed 0%CPU (0avgtext+0avgdata 35108maxresident)k
0inputs+16outputs (1major+4390minor)pagefaults 0swaps
```

#### stack_top_own

                                         Name                                         | Shared |   %   |  Own  |   %
--------------------------------------------------------------------------------------|--------|-------|-------|------
github.com/ledgerwatch/erigon/core/vm.(*EVMInterpreter).Run                           |  32632 |  56.1 | 10074 |  17.3
golang.org/x/crypto/sha3.keccakF1600                                                  |   4093 |   7.0 |  4087 |   7.0
cmpbody                                                                               |   3432 |   5.9 |  3429 |   5.9
github.com/ledgerwatch/erigon/ethdb/olddb.(*MutationItem).Less                        |   2939 |   5.1 |  2935 |   5.0
runtime.mallocgc                                                                      |   4484 |   7.7 |  2130 |   3.7
github.com/ledgerwatch/erigon/core/vm.makeDup.func1                                   |   1436 |   2.5 |  1435 |   2.5
github.com/ledgerwatch/erigon/core/vm.(*Memory).Set32                                 |   1152 |   2.0 |  1151 |   2.0
mdbx_node_search                                                                      |   1088 |   1.9 |  1088 |   1.9
github.com/google/btree.items.find.func1                                              |   7182 |  12.4 |  1035 |   1.8
github.com/ledgerwatch/erigon/core/vm.makeSwap.func1                                  |    876 |   1.5 |   872 |   1.5
github.com/ledgerwatch/erigon/core/vm.opPush1                                         |    852 |   1.5 |   851 |   1.5
aeshashbody                                                                           |    788 |   1.4 |   787 |   1.4
mdbx_page_get_ex                                                                      |    890 |   1.5 |   779 |   1.3
github.com/ledgerwatch/erigon/core/vm.makePush.func1                                  |   1162 |   2.0 |   779 |   1.3
runtime.memclrNoHeapPointers                                                          |    800 |   1.4 |   776 |   1.3
runtime.memmove                                                                       |    758 |   1.3 |   723 |   1.2
runtime.heapBitsSetType                                                               |    664 |   1.1 |   662 |   1.1
github.com/ledgerwatch/erigon/core/vm.opJumpi                                         |    660 |   1.1 |   644 |   1.1
golang.org/x/crypto/sha3.(*state).padAndPermute                                       |    826 |   1.4 |   623 |   1.1
runtime.mapassign                                                                     |   1647 |   2.8 |   619 |   1.1
