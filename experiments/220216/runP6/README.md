### Automated

```
[ perf record: Woken up 30 times to write data ]
[ perf record: Captured and wrote 7.697 MB /tmp2/p (53391 samples) ]
Wall time: 87.201 seconds
```

#### stack_top_own

Name                                         | Shared |   %   | Own  |   %
---------------------------------------------|--------|-------|------|------
core.go:240                                  |   3069 |   5.7 | 3069 |   5.7
uint256.go:1019                              |   2034 |   3.8 | 2034 |   3.8
mutation_tree.go:165                         |   1653 |   3.1 | 1653 |   3.1
43801c                                       |   1564 |   2.9 | 1564 |   2.9
44331c                                       |   1557 |   2.9 | 1557 |   2.9
binary.go:79                                 |   1455 |   2.7 | 1455 |   2.7
map.go:488                                   |   1210 |   2.3 | 1210 |   2.3
mutation_tree.go:74                          |    996 |   1.9 |  996 |   1.9
instructions.go:41                           |    755 |   1.4 |  755 |   1.4
core.go:234                                  |    673 |   1.3 |  673 |   1.3
core.go:232                                  |    628 |   1.2 |  628 |   1.2
mutation_tree.go:161                         |    560 |   1.0 |  560 |   1.0
alg.go:27                                    |    546 |   1.0 |  546 |   1.0
instructions.go:57                           |    523 |   1.0 |  523 |   1.0
map.go:498                                   |    450 |   0.8 |  450 |   0.8
instructions.go:69                           |    415 |   0.8 |  415 |   0.8
map.go:472                                   |    393 |   0.7 |  393 |   0.7
sha3.go:110                                  |    370 |   0.7 |  370 |   0.7
uint256.go:110                               |    367 |   0.7 |  367 |   0.7
asm_amd64.s:913                              |    360 |   0.7 |  360 |   0.7
