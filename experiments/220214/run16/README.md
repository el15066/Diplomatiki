### Automated

```
[ perf record: Woken up 15 times to write data ]
[ perf record: Captured and wrote 3.738 MB /tmp2/p (17994 samples) ]
Wall time: 92.239 seconds
```

#### stack_top_own

Name                                                | Shared |   %   | Own |   %
----------------------------------------------------|--------|-------|-----|------
mutation_tree.go:37                                 |    595 |   3.3 | 595 |   3.3
interpreter.go:259                                  |    504 |   2.8 | 504 |   2.8
interpreter.go:326                                  |    449 |   2.5 | 449 |   2.5
binary.go:79                                        |    421 |   2.3 | 421 |   2.3
interpreter.go:266                                  |    357 |   2.0 | 357 |   2.0
interpreter.go:262                                  |    335 |   1.9 | 335 |   1.9
44331c                                              |    322 |   1.8 | 322 |   1.8
43801c                                              |    321 |   1.8 | 321 |   1.8
mutation_tree.go:74                                 |    306 |   1.7 | 306 |   1.7
uint256.go:1019                                     |    226 |   1.3 | 226 |   1.3
malloc.go:852                                       |    181 |   1.0 | 181 |   1.0
mutation_tree.go:165                                |    169 |   0.9 | 169 |   0.9
sha3.go:110                                         |    162 |   0.9 | 162 |   0.9
stack.go:75                                         |    149 |   0.8 | 149 |   0.8
instructions.go:946                                 |    148 |   0.8 | 148 |   0.8
stack.go:103                                        |    134 |   0.7 | 134 |   0.7
interpreter.go:293                                  |    129 |   0.7 | 129 |   0.7
7ffe313cd7c8                                        |    115 |   0.6 | 115 |   0.6
memclr_amd64.s:79                                   |    112 |   0.6 | 112 |   0.6
mutation_tree.go:162                                |    100 |   0.6 | 100 |   0.6
