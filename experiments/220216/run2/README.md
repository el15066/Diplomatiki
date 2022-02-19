### Automated

```
[ perf record: Woken up 14 times to write data ]
[ perf record: Captured and wrote 3.643 MB /tmp2/p (17318 samples) ]
Wall time: 88.786 seconds
```

#### stack_top_own

Name                                             | Shared |   %   | Own |   %
-------------------------------------------------|--------|-------|-----|------
interpreter.go:326                               |    446 |   2.6 | 446 |   2.6
mutation_tree.go:165                             |    413 |   2.4 | 413 |   2.4
interpreter.go:266                               |    370 |   2.1 | 370 |   2.1
binary.go:79                                     |    366 |   2.1 | 366 |   2.1
interpreter.go:262                               |    333 |   1.9 | 333 |   1.9
43801c                                           |    311 |   1.8 | 311 |   1.8
44331c                                           |    296 |   1.7 | 296 |   1.7
interpreter.go:259                               |    274 |   1.6 | 274 |   1.6
mutation_tree.go:74                              |    250 |   1.4 | 250 |   1.4
uint256.go:1019                                  |    214 |   1.2 | 214 |   1.2
interpreter.go:260                               |    191 |   1.1 | 191 |   1.1
malloc.go:852                                    |    176 |   1.0 | 176 |   1.0
sha3.go:110                                      |    156 |   0.9 | 156 |   0.9
7ffe987557c8                                     |    132 |   0.8 | 132 |   0.8
<autogenerated>:1                                |    122 |   0.7 | 122 |   0.7
instructions.go:959                              |    121 |   0.7 | 121 |   0.7
stack.go:103                                     |    115 |   0.7 | 115 |   0.7
memclr_amd64.s:79                                |    108 |   0.6 | 108 |   0.6
stack.go:75                                      |    106 |   0.6 | 106 |   0.6
interpreter.go:307                               |     95 |   0.5 |  95 |   0.5