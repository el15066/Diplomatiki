### Automated

```
[ perf record: Woken up 30 times to write data ]
[ perf record: Captured and wrote 7.662 MB /tmp2/p (53114 samples) ]
Wall time: 86.502 seconds
```

#### stack_top_own

Name                                         | Shared |   %   | Own  |   %
---------------------------------------------|--------|-------|------|------
core.go:241                                  |   2993 |   5.6 | 2993 |   5.6
uint256.go:1019                              |   2171 |   4.1 | 2171 |   4.1
mutation_tree.go:165                         |   1633 |   3.1 | 1633 |   3.1
43801c                                       |   1552 |   2.9 | 1552 |   2.9
44331c                                       |   1537 |   2.9 | 1537 |   2.9
binary.go:79                                 |   1451 |   2.7 | 1451 |   2.7
map.go:488                                   |   1231 |   2.3 | 1231 |   2.3
mutation_tree.go:74                          |    948 |   1.8 |  948 |   1.8
instructions.go:41                           |    826 |   1.6 |  826 |   1.6
core.go:233                                  |    644 |   1.2 |  644 |   1.2
core.go:235                                  |    642 |   1.2 |  642 |   1.2
mutation_tree.go:161                         |    554 |   1.0 |  554 |   1.0
alg.go:27                                    |    510 |   1.0 |  510 |   1.0
instructions.go:57                           |    480 |   0.9 |  480 |   0.9
map.go:498                                   |    477 |   0.9 |  477 |   0.9
instructions.go:69                           |    431 |   0.8 |  431 |   0.8
map.go:472                                   |    404 |   0.8 |  404 |   0.8
uint256.go:110                               |    363 |   0.7 |  363 |   0.7
sha3.go:110                                  |    363 |   0.7 |  363 |   0.7
memclr_amd64.s:79                            |    336 |   0.6 |  336 |   0.6
