### Automated

```
[ perf record: Woken up 8 times to write data ]
[ perf record: Captured and wrote 2.050 MB /tmp2/p (9558 samples) ]
Wall time: 87.020 seconds
```

#### stack_top_own

Name                                             | Shared |   %   | Own |   %
-------------------------------------------------|--------|-------|-----|------
interpreter.go:326                               |    290 |   3.0 | 290 |   3.0
mutation_tree.go:165                             |    235 |   2.5 | 235 |   2.5
interpreter.go:266                               |    221 |   2.3 | 221 |   2.3
binary.go:79                                     |    201 |   2.1 | 201 |   2.1
interpreter.go:262                               |    183 |   1.9 | 183 |   1.9
43801c                                           |    171 |   1.8 | 171 |   1.8
44331c                                           |    169 |   1.8 | 169 |   1.8
uint256.go:1019                                  |    144 |   1.5 | 144 |   1.5
mutation_tree.go:74                              |    141 |   1.5 | 141 |   1.5
malloc.go:852                                    |    128 |   1.3 | 128 |   1.3
interpreter.go:260                               |    128 |   1.3 | 128 |   1.3
interpreter.go:259                               |    119 |   1.2 | 119 |   1.2
sha3.go:110                                      |    101 |   1.1 | 101 |   1.1
instructions.go:959                              |     92 |   1.0 |  92 |   1.0
<autogenerated>:1                                |     80 |   0.8 |  80 |   0.8
memclr_amd64.s:79                                |     65 |   0.7 |  65 |   0.7
malloc.go:1183                                   |     61 |   0.6 |  61 |   0.6
stack.go:103                                     |     61 |   0.6 |  61 |   0.6
instructions.go:915                              |     55 |   0.6 |  55 |   0.6
instructions.go:933                              |     54 |   0.6 |  54 |   0.6