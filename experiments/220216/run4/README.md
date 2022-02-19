### Automated

```
[ perf record: Woken up 14 times to write data ]
[ perf record: Captured and wrote 3.654 MB /tmp2/p (17246 samples) ]
Wall time: 88.533 seconds
```

#### stack_top_own

Name                                             | Shared |   %   | Own |   %
-------------------------------------------------|--------|-------|-----|------
interpreter.go:326                               |    506 |   2.9 | 506 |   2.9
mutation_tree.go:165                             |    448 |   2.6 | 448 |   2.6
binary.go:79                                     |    366 |   2.1 | 366 |   2.1
interpreter.go:262                               |    346 |   2.0 | 346 |   2.0
interpreter.go:266                               |    346 |   2.0 | 346 |   2.0
43801c                                           |    299 |   1.7 | 299 |   1.7
44331c                                           |    290 |   1.7 | 290 |   1.7
mutation_tree.go:74                              |    269 |   1.6 | 269 |   1.6
interpreter.go:259                               |    237 |   1.4 | 237 |   1.4
uint256.go:1019                                  |    222 |   1.3 | 222 |   1.3
interpreter.go:260                               |    189 |   1.1 | 189 |   1.1
malloc.go:852                                    |    169 |   1.0 | 169 |   1.0
sha3.go:110                                      |    165 |   1.0 | 165 |   1.0
<autogenerated>:1                                |    131 |   0.8 | 131 |   0.8
instructions.go:950                              |    125 |   0.7 | 125 |   0.7
memclr_amd64.s:79                                |    114 |   0.7 | 114 |   0.7
7ffd7c7527c8                                     |    114 |   0.7 | 114 |   0.7
stack.go:75                                      |    114 |   0.7 | 114 |   0.7
mutation_tree.go:161                             |    110 |   0.6 | 110 |   0.6
stack.go:103                                     |    110 |   0.6 | 110 |   0.6