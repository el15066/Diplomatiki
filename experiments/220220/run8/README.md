### Automated

```
[ perf record: Woken up 8 times to write data ]
[ perf record: Captured and wrote 2.079 MB /tmp2/p (9665 samples) ]
Wall time: 87.891 seconds
```

#### stack_top_own

Name                                             | Shared |   %   | Own |   %
-------------------------------------------------|--------|-------|-----|------
mutation_tree.go:165                             |    260 |   2.7 | 260 |   2.7
interpreter.go:326                               |    251 |   2.6 | 251 |   2.6
binary.go:79                                     |    229 |   2.4 | 229 |   2.4
interpreter.go:266                               |    200 |   2.1 | 200 |   2.1
interpreter.go:262                               |    197 |   2.0 | 197 |   2.0
44331c                                           |    182 |   1.9 | 182 |   1.9
mutation_tree.go:74                              |    175 |   1.8 | 175 |   1.8
43801c                                           |    168 |   1.7 | 168 |   1.7
interpreter.go:259                               |    139 |   1.4 | 139 |   1.4
interpreter.go:260                               |    125 |   1.3 | 125 |   1.3
uint256.go:1019                                  |    117 |   1.2 | 117 |   1.2
malloc.go:852                                    |    107 |   1.1 | 107 |   1.1
sha3.go:110                                      |     80 |   0.8 |  80 |   0.8
stack.go:103                                     |     76 |   0.8 |  76 |   0.8
instructions.go:959                              |     75 |   0.8 |  75 |   0.8
mutation_tree.go:161                             |     65 |   0.7 |  65 |   0.7
instructions.go:969                              |     61 |   0.6 |  61 |   0.6
stack.go:75                                      |     54 |   0.6 |  54 |   0.6
memclr_amd64.s:79                                |     52 |   0.5 |  52 |   0.5
instructions.go:915                              |     52 |   0.5 |  52 |   0.5
