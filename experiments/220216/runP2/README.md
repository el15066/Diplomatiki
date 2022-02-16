### Automated

```
[ perf record: Woken up 6 times to write data ]
[ perf record: Captured and wrote 1.603 MB /tmp2/p (9551 samples) ]
Wall time: 87.718 seconds
```

#### stack_top_own

Name                                         | Shared |   %   | Own |   %
---------------------------------------------|--------|-------|-----|------
core.go:240                                  |    591 |   6.2 | 591 |   6.2
uint256.go:1019                              |    351 |   3.7 | 351 |   3.7
44331c                                       |    279 |   2.9 | 279 |   2.9
43801c                                       |    255 |   2.7 | 255 |   2.7
mutation_tree.go:165                         |    255 |   2.7 | 255 |   2.7
binary.go:79                                 |    247 |   2.6 | 247 |   2.6
map.go:488                                   |    198 |   2.1 | 198 |   2.1
mutation_tree.go:74                          |    184 |   1.9 | 184 |   1.9
instructions.go:41                           |    136 |   1.4 | 136 |   1.4
core.go:234                                  |    123 |   1.3 | 123 |   1.3
mutation_tree.go:161                         |    109 |   1.1 | 109 |   1.1
core.go:232                                  |    107 |   1.1 | 107 |   1.1
7fffb18fe7c8                                 |    100 |   1.0 | 100 |   1.0
map.go:498                                   |     91 |   1.0 |  91 |   1.0
alg.go:27                                    |     89 |   0.9 |  89 |   0.9
instructions.go:57                           |     78 |   0.8 |  78 |   0.8
map.go:472                                   |     77 |   0.8 |  77 |   0.8
instructions.go:69                           |     71 |   0.7 |  71 |   0.7
uint256.go:110                               |     67 |   0.7 |  67 |   0.7
asm_amd64.s:913                              |     63 |   0.7 |  63 |   0.7
