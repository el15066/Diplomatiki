### Automated

```
[ perf record: Woken up 30 times to write data ]
[ perf record: Captured and wrote 7.703 MB /tmp2/p (53436 samples) ]
Wall time: 87.016 seconds
```

#### stack_top_own

Name                                         | Shared |   %   | Own  |   %
---------------------------------------------|--------|-------|------|------
core.go:240                                  |   3248 |   6.1 | 3248 |   6.1
uint256.go:1019                              |   2104 |   3.9 | 2104 |   3.9
mutation_tree.go:165                         |   1593 |   3.0 | 1593 |   3.0
44331c                                       |   1538 |   2.9 | 1538 |   2.9
43801c                                       |   1537 |   2.9 | 1537 |   2.9
binary.go:79                                 |   1406 |   2.6 | 1406 |   2.6
map.go:488                                   |   1178 |   2.2 | 1178 |   2.2
mutation_tree.go:74                          |    969 |   1.8 |  969 |   1.8
instructions.go:41                           |    844 |   1.6 |  844 |   1.6
core.go:234                                  |    668 |   1.3 |  668 |   1.3
core.go:232                                  |    584 |   1.1 |  584 |   1.1
alg.go:27                                    |    542 |   1.0 |  542 |   1.0
mutation_tree.go:161                         |    523 |   1.0 |  523 |   1.0
instructions.go:57                           |    473 |   0.9 |  473 |   0.9
instructions.go:69                           |    458 |   0.9 |  458 |   0.9
map.go:498                                   |    445 |   0.8 |  445 |   0.8
map.go:472                                   |    397 |   0.7 |  397 |   0.7
uint256.go:110                               |    368 |   0.7 |  368 |   0.7
sha3.go:110                                  |    360 |   0.7 |  360 |   0.7
memclr_amd64.s:79                            |    334 |   0.6 |  334 |   0.6
