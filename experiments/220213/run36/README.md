### Automated

```
[ perf record: Woken up 15 times to write data ]
[ perf record: Captured and wrote 3.832 MB /tmp2/p (18200 samples) ]
Wall time: 93.342 seconds
```

#### stack_top_own

Name                                             | Shared |   %   | Own |   %
-------------------------------------------------|--------|-------|-----|------
mutation_tree.go:31                              |    689 |   3.8 | 689 |   3.8
compare_amd64.s:49                               |    604 |   3.3 | 604 |   3.3
interpreter.go:259                               |    546 |   3.0 | 546 |   3.0
interpreter.go:326                               |    484 |   2.7 | 484 |   2.7
interpreter.go:266                               |    353 |   1.9 | 353 |   1.9
interpreter.go:262                               |    350 |   1.9 | 350 |   1.9
43801c                                           |    328 |   1.8 | 328 |   1.8
44331c                                           |    308 |   1.7 | 308 |   1.7
malloc.go:852                                    |    198 |   1.1 | 198 |   1.1
uint256.go:1019                                  |    188 |   1.0 | 188 |   1.0
sha3.go:110                                      |    159 |   0.9 | 159 |   0.9
interpreter.go:293                               |    137 |   0.8 | 137 |   0.8
stack.go:75                                      |    137 |   0.8 | 137 |   0.8
stack.go:103                                     |    132 |   0.7 | 132 |   0.7
instructions.go:946                              |    126 |   0.7 | 126 |   0.7
<autogenerated>:1                                |    118 |   0.6 | 118 |   0.6
memclr_amd64.s:79                                |    116 |   0.6 | 116 |   0.6
7fff4afc77c8                                     |    115 |   0.6 | 115 |   0.6
mutation_tree.go:87                              |    111 |   0.6 | 111 |   0.6
instructions.go:920                              |     93 |   0.5 |  93 |   0.5