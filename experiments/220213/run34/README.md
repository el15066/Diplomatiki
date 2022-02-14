### Automated

```
[ perf record: Woken up 15 times to write data ]
[ perf record: Captured and wrote 3.841 MB /tmp2/p (18214 samples) ]
Wall time: 93.294 seconds
```

#### stack_top_own

Name                                                | Shared |   %   | Own |   %
----------------------------------------------------|--------|-------|-----|------
mutation_tree.go:31                                 |    662 |   3.6 | 662 |   3.6
compare_amd64.s:49                                  |    645 |   3.5 | 645 |   3.5
interpreter.go:259                                  |    532 |   2.9 | 532 |   2.9
interpreter.go:326                                  |    476 |   2.6 | 476 |   2.6
interpreter.go:266                                  |    372 |   2.0 | 372 |   2.0
interpreter.go:262                                  |    337 |   1.9 | 337 |   1.9
44331c                                              |    305 |   1.7 | 305 |   1.7
43801c                                              |    298 |   1.6 | 298 |   1.6
uint256.go:1019                                     |    209 |   1.1 | 209 |   1.1
malloc.go:852                                       |    165 |   0.9 | 165 |   0.9
sha3.go:110                                         |    163 |   0.9 | 163 |   0.9
interpreter.go:293                                  |    152 |   0.8 | 152 |   0.8
7fff855127c8                                        |    134 |   0.7 | 134 |   0.7
stack.go:75                                         |    134 |   0.7 | 134 |   0.7
stack.go:103                                        |    133 |   0.7 | 133 |   0.7
instructions.go:946                                 |    132 |   0.7 | 132 |   0.7
memclr_amd64.s:79                                   |    112 |   0.6 | 112 |   0.6
mutation_tree.go:87                                 |    108 |   0.6 | 108 |   0.6
mutation_tree.go:88                                 |    102 |   0.6 | 102 |   0.6
contract.go:182                                     |    102 |   0.6 | 102 |   0.6
