### Automated

```
[ perf record: Woken up 28 times to write data ]
[ perf record: Captured and wrote 7.123 MB /tmp2/p (49841 samples) ]
Wall time: 86.117 seconds
```

#### stack_top_own

Name                                                 | Shared |   %   | Own  |   %
-----------------------------------------------------|--------|-------|------|------
core.go:241                                          |   3118 |   6.3 | 3118 |   6.3
uint256.go:1019                                      |   2175 |   4.4 | 2175 |   4.4
mutation_tree.go:165                                 |   1668 |   3.3 | 1668 |   3.3
43801c                                               |   1515 |   3.0 | 1515 |   3.0
binary.go:79                                         |   1495 |   3.0 | 1495 |   3.0
44331c                                               |   1443 |   2.9 | 1443 |   2.9
map.go:488                                           |   1377 |   2.8 | 1377 |   2.8
mutation_tree.go:74                                  |    986 |   2.0 |  986 |   2.0
instructions.go:41                                   |    761 |   1.5 |  761 |   1.5
core.go:235                                          |    642 |   1.3 |  642 |   1.3
mutation_tree.go:161                                 |    580 |   1.2 |  580 |   1.2
core.go:233                                          |    577 |   1.2 |  577 |   1.2
instructions.go:57                                   |    488 |   1.0 |  488 |   1.0
map.go:498                                           |    450 |   0.9 |  450 |   0.9
alg.go:27                                            |    439 |   0.9 |  439 |   0.9
instructions.go:69                                   |    433 |   0.9 |  433 |   0.9
map.go:472                                           |    419 |   0.8 |  419 |   0.8
uint256.go:110                                       |    381 |   0.8 |  381 |   0.8
sha3.go:110                                          |    362 |   0.7 |  362 |   0.7
instructions.go:47                                   |    272 |   0.5 |  272 |   0.5
