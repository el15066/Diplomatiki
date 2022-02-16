### Automated

```
[ perf record: Woken up 31 times to write data ]
[ perf record: Captured and wrote 7.880 MB /tmp2/p (54911 samples) ]
Wall time: 87.223 seconds
```

#### stack_top_own

Name                                         | Shared |   %   | Own  |   %
---------------------------------------------|--------|-------|------|------
core.go:240                                  |   2758 |   5.0 | 2758 |   5.0
uint256.go:1019                              |   2118 |   3.9 | 2118 |   3.9
mutation_tree.go:165                         |   1566 |   2.9 | 1566 |   2.9
43801c                                       |   1510 |   2.7 | 1510 |   2.7
44331c                                       |   1495 |   2.7 | 1495 |   2.7
binary.go:79                                 |   1415 |   2.6 | 1415 |   2.6
map.go:488                                   |   1182 |   2.2 | 1182 |   2.2
mutation_tree.go:74                          |   1014 |   1.8 | 1014 |   1.8
instructions.go:41                           |    971 |   1.8 |  971 |   1.8
core.go:232                                  |    795 |   1.4 |  795 |   1.4
core.go:234                                  |    662 |   1.2 |  662 |   1.2
alg.go:27                                    |    545 |   1.0 |  545 |   1.0
instructions.go:57                           |    533 |   1.0 |  533 |   1.0
mutation_tree.go:161                         |    525 |   1.0 |  525 |   1.0
instructions.go:69                           |    465 |   0.8 |  465 |   0.8
map.go:498                                   |    461 |   0.8 |  461 |   0.8
map.go:472                                   |    409 |   0.7 |  409 |   0.7
sha3.go:110                                  |    397 |   0.7 |  397 |   0.7
uint256.go:110                               |    360 |   0.7 |  360 |   0.7
asm_amd64.s:913                              |    342 |   0.6 |  342 |   0.6
