### Automated

```
[ perf record: Woken up 22 times to write data ]
[ perf record: Captured and wrote 5.534 MB /tmp2/p (27392 samples) ]
Wall time: 143.615 seconds
```

#### stack_top_own

Name                                                 | Shared |   %   | Own |   %
-----------------------------------------------------|--------|-------|-----|------
interpreter.go:259                                   |    726 |   2.7 | 726 |   2.7
interpreter.go:326                                   |    711 |   2.6 | 711 |   2.6
mutation_tree.go:165                                 |    620 |   2.3 | 620 |   2.3
interpreter.go:266                                   |    548 |   2.0 | 548 |   2.0
binary.go:79                                         |    528 |   1.9 | 528 |   1.9
interpreter.go:262                                   |    458 |   1.7 | 458 |   1.7
43801c                                               |    441 |   1.6 | 441 |   1.6
44331c                                               |    419 |   1.5 | 419 |   1.5
mutation_tree.go:74                                  |    367 |   1.3 | 367 |   1.3
uint256.go:1019                                      |    313 |   1.1 | 313 |   1.1
malloc.go:852                                        |    261 |   1.0 | 261 |   1.0
sha3.go:110                                          |    234 |   0.9 | 234 |   0.9
ffffffffb1e6abf9                                     |    214 |   0.8 | 214 |   0.8
instructions.go:946                                  |    204 |   0.7 | 204 |   0.7
stack.go:75                                          |    191 |   0.7 | 191 |   0.7
stack.go:103                                         |    187 |   0.7 | 187 |   0.7
interpreter.go:293                                   |    173 |   0.6 | 173 |   0.6
mutation_tree.go:161                                 |    153 |   0.6 | 153 |   0.6
7fffe5b6e7c8                                         |    153 |   0.6 | 153 |   0.6
ffffffffb21ff374                                     |    146 |   0.5 | 146 |   0.5
