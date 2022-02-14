### Automated

```
[ perf record: Woken up 15 times to write data ]
[ perf record: Captured and wrote 3.843 MB /tmp2/p (18160 samples) ]
Wall time: 93.071 seconds
```

#### stack_top_own

Name                                             | Shared |   %   | Own |   %
-------------------------------------------------|--------|-------|-----|------
compare_amd64.s:49                               |    635 |   3.5 | 635 |   3.5
mutation_tree.go:31                              |    559 |   3.1 | 559 |   3.1
interpreter.go:259                               |    542 |   3.0 | 542 |   3.0
interpreter.go:326                               |    459 |   2.5 | 459 |   2.5
interpreter.go:266                               |    389 |   2.1 | 389 |   2.1
43801c                                           |    333 |   1.8 | 333 |   1.8
interpreter.go:262                               |    327 |   1.8 | 327 |   1.8
44331c                                           |    281 |   1.5 | 281 |   1.5
uint256.go:1019                                  |    218 |   1.2 | 218 |   1.2
malloc.go:852                                    |    197 |   1.1 | 197 |   1.1
sha3.go:110                                      |    165 |   0.9 | 165 |   0.9
mutation_tree.go:79                              |    148 |   0.8 | 148 |   0.8
stack.go:75                                      |    137 |   0.8 | 137 |   0.8
7ffe92fca7c8                                     |    134 |   0.7 | 134 |   0.7
instructions.go:946                              |    134 |   0.7 | 134 |   0.7
interpreter.go:293                               |    119 |   0.7 | 119 |   0.7
stack.go:103                                     |    114 |   0.6 | 114 |   0.6
memclr_amd64.s:79                                |    108 |   0.6 | 108 |   0.6
memclr_amd64.s:81                                |    107 |   0.6 | 107 |   0.6
search.go:66                                     |    106 |   0.6 | 106 |   0.6
