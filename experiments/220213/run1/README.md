### Automated

```
[ perf record: Woken up 24 times to write data ]
[ perf record: Captured and wrote 6.019 MB /tmp2/p (29142 samples) ]
Wall time: 152.663 seconds
```

#### stack_top_own

Name                                              | Shared |   %   | Own  |   %
--------------------------------------------------|--------|-------|------|------
compare_amd64.s:49                                |   1054 |   3.6 | 1054 |   3.6
mutation.go:89                                    |    964 |   3.3 |  964 |   3.3
interpreter.go:326                                |    673 |   2.3 |  673 |   2.3
interpreter.go:259                                |    669 |   2.3 |  669 |   2.3
interpreter.go:266                                |    455 |   1.6 |  455 |   1.6
interpreter.go:262                                |    454 |   1.6 |  454 |   1.6
43801c                                            |    441 |   1.5 |  441 |   1.5
44331c                                            |    407 |   1.4 |  407 |   1.4
btree.go:189                                      |    405 |   1.4 |  405 |   1.4
stack.go:48                                       |    370 |   1.3 |  370 |   1.3
stack.go:62                                       |    367 |   1.3 |  367 |   1.3
malloc.go:852                                     |    248 |   0.9 |  248 |   0.9
sha3.go:110                                       |    248 |   0.9 |  248 |   0.9
stack.go:72                                       |    220 |   0.8 |  220 |   0.8
ffffffffb1e6abf9                                  |    213 |   0.7 |  213 |   0.7
instructions.go:950                               |    181 |   0.6 |  181 |   0.6
interpreter.go:293                                |    178 |   0.6 |  178 |   0.6
malloc.go:1183                                    |    161 |   0.6 |  161 |   0.6
keccakf_amd64.s:378                               |    161 |   0.6 |  161 |   0.6
7ffeedbf87c8                                      |    154 |   0.5 |  154 |   0.5
