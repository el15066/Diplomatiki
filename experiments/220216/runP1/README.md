### Automated

```
[ perf record: Woken up 6 times to write data ]
[ perf record: Captured and wrote 1.619 MB /tmp2/p (9626 samples) ]
Wall time: 87.619 seconds
```

#### stack_top_own

Name                                         | Shared |   %   | Own |   %
---------------------------------------------|--------|-------|-----|------
core.go:240                                  |    527 |   5.5 | 527 |   5.5
uint256.go:1019                              |    397 |   4.1 | 397 |   4.1
mutation_tree.go:165                         |    276 |   2.9 | 276 |   2.9
43801c                                       |    268 |   2.8 | 268 |   2.8
binary.go:79                                 |    268 |   2.8 | 268 |   2.8
44331c                                       |    265 |   2.8 | 265 |   2.8
map.go:488                                   |    172 |   1.8 | 172 |   1.8
instructions.go:41                           |    162 |   1.7 | 162 |   1.7
mutation_tree.go:74                          |    157 |   1.6 | 157 |   1.6
core.go:232                                  |    148 |   1.5 | 148 |   1.5
core.go:234                                  |    128 |   1.3 | 128 |   1.3
mutation_tree.go:161                         |    104 |   1.1 | 104 |   1.1
alg.go:27                                    |    102 |   1.1 | 102 |   1.1
7ffe2f51f7c8                                 |     95 |   1.0 |  95 |   1.0
instructions.go:69                           |     92 |   1.0 |  92 |   1.0
instructions.go:57                           |     84 |   0.9 |  84 |   0.9
map.go:472                                   |     81 |   0.8 |  81 |   0.8
map.go:498                                   |     76 |   0.8 |  76 |   0.8
sha3.go:110                                  |     67 |   0.7 |  67 |   0.7
instructions.go:58                           |     63 |   0.7 |  63 |   0.7
