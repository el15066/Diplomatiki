### Automated

```
[ perf record: Woken up 8 times to write data ]
[ perf record: Captured and wrote 2.084 MB /tmp2/p (9673 samples) ]
Wall time: 88.004 seconds
```

#### stack_top_own

Name                                                | Shared |   %   | Own |   %
----------------------------------------------------|--------|-------|-----|------
binary.go:79                                        |    263 |   2.7 | 263 |   2.7
interpreter.go:326                                  |    235 |   2.4 | 235 |   2.4
mutation_tree.go:165                                |    225 |   2.3 | 225 |   2.3
interpreter.go:266                                  |    223 |   2.3 | 223 |   2.3
43801c                                              |    175 |   1.8 | 175 |   1.8
interpreter.go:262                                  |    172 |   1.8 | 172 |   1.8
44331c                                              |    171 |   1.8 | 171 |   1.8
mutation_tree.go:74                                 |    147 |   1.5 | 147 |   1.5
interpreter.go:259                                  |    136 |   1.4 | 136 |   1.4
uint256.go:1019                                     |    112 |   1.2 | 112 |   1.2
malloc.go:852                                       |    109 |   1.1 | 109 |   1.1
interpreter.go:260                                  |    106 |   1.1 | 106 |   1.1
sha3.go:110                                         |    105 |   1.1 | 105 |   1.1
stack.go:75                                         |     71 |   0.7 |  71 |   0.7
<autogenerated>:1                                   |     69 |   0.7 |  69 |   0.7
stack.go:103                                        |     69 |   0.7 |  69 |   0.7
instructions.go:959                                 |     62 |   0.6 |  62 |   0.6
malloc.go:1183                                      |     60 |   0.6 |  60 |   0.6
mutation_tree.go:161                                |     55 |   0.6 |  55 |   0.6
instructions.go:915                                 |     54 |   0.6 |  54 |   0.6