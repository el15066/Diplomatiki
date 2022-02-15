### Automated

```
[ perf record: Woken up 14 times to write data ]
[ perf record: Captured and wrote 3.659 MB /tmp2/p (17593 samples) ]
Wall time: 90.257 seconds
```

#### stack_top_own

Name                                                | Shared |   %   | Own |   %
----------------------------------------------------|--------|-------|-----|------
interpreter.go:259                                  |    495 |   2.8 | 495 |   2.8
interpreter.go:326                                  |    442 |   2.5 | 442 |   2.5
mutation_tree.go:165                                |    431 |   2.4 | 431 |   2.4
binary.go:79                                        |    397 |   2.3 | 397 |   2.3
interpreter.go:266                                  |    366 |   2.1 | 366 |   2.1
interpreter.go:262                                  |    327 |   1.9 | 327 |   1.9
43801c                                              |    322 |   1.8 | 322 |   1.8
mutation_tree.go:74                                 |    283 |   1.6 | 283 |   1.6
44331c                                              |    268 |   1.5 | 268 |   1.5
uint256.go:1019                                     |    219 |   1.2 | 219 |   1.2
malloc.go:852                                       |    159 |   0.9 | 159 |   0.9
sha3.go:110                                         |    154 |   0.9 | 154 |   0.9
stack.go:103                                        |    140 |   0.8 | 140 |   0.8
instructions.go:946                                 |    135 |   0.8 | 135 |   0.8
7ffd4ebf97c8                                        |    120 |   0.7 | 120 |   0.7
interpreter.go:293                                  |    116 |   0.7 | 116 |   0.7
memclr_amd64.s:79                                   |    112 |   0.6 | 112 |   0.6
mutation_tree.go:161                                |    110 |   0.6 | 110 |   0.6
stack.go:75                                         |    108 |   0.6 | 108 |   0.6
memclr_amd64.s:81                                   |    102 |   0.6 | 102 |   0.6
