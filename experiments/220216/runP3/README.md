### Automated

```
[ perf record: Woken up 6 times to write data ]
[ perf record: Captured and wrote 1.620 MB /tmp2/p (9714 samples) ]
Wall time: 87.823 seconds
```

#### stack_top_own

Name                                         | Shared |   %   | Own |   %
---------------------------------------------|--------|-------|-----|------
core.go:240                                  |    394 |   4.1 | 394 |   4.1
uint256.go:1019                              |    386 |   4.0 | 386 |   4.0
instructions.go:42                           |    353 |   3.6 | 353 |   3.6
43801c                                       |    286 |   2.9 | 286 |   2.9
44331c                                       |    278 |   2.9 | 278 |   2.9
binary.go:79                                 |    271 |   2.8 | 271 |   2.8
mutation_tree.go:165                         |    261 |   2.7 | 261 |   2.7
map.go:488                                   |    207 |   2.1 | 207 |   2.1
mutation_tree.go:74                          |    188 |   1.9 | 188 |   1.9
core.go:232                                  |    131 |   1.3 | 131 |   1.3
mutation_tree.go:161                         |     98 |   1.0 |  98 |   1.0
core.go:234                                  |     98 |   1.0 |  98 |   1.0
alg.go:27                                    |     97 |   1.0 |  97 |   1.0
7fff15ff67c8                                 |     97 |   1.0 |  97 |   1.0
instructions.go:58                           |     93 |   1.0 |  93 |   1.0
instructions.go:65                           |     92 |   0.9 |  92 |   0.9
map.go:472                                   |     80 |   0.8 |  80 |   0.8
map.go:498                                   |     68 |   0.7 |  68 |   0.7
instructions.go:70                           |     68 |   0.7 |  68 |   0.7
sha3.go:110                                  |     68 |   0.7 |  68 |   0.7
