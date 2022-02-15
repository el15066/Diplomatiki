### Automated

```
[ perf record: Woken up 15 times to write data ]
[ perf record: Captured and wrote 3.848 MB /tmp2/p (18324 samples) ]
Wall time: 93.897 seconds
```

#### stack_top_own

Name                                                | Shared |   %   | Own |   %
----------------------------------------------------|--------|-------|-----|------
mutation_tree.go:66                                 |    720 |   3.9 | 720 |   3.9
compare_amd64.s:49                                  |    644 |   3.5 | 644 |   3.5
interpreter.go:259                                  |    528 |   2.9 | 528 |   2.9
interpreter.go:326                                  |    455 |   2.5 | 455 |   2.5
interpreter.go:266                                  |    369 |   2.0 | 369 |   2.0
interpreter.go:262                                  |    342 |   1.9 | 342 |   1.9
44331c                                              |    322 |   1.8 | 322 |   1.8
43801c                                              |    297 |   1.6 | 297 |   1.6
uint256.go:1019                                     |    207 |   1.1 | 207 |   1.1
malloc.go:852                                       |    189 |   1.0 | 189 |   1.0
sha3.go:110                                         |    175 |   1.0 | 175 |   1.0
instructions.go:946                                 |    163 |   0.9 | 163 |   0.9
stack.go:75                                         |    140 |   0.8 | 140 |   0.8
interpreter.go:293                                  |    137 |   0.7 | 137 |   0.7
7ffc12bc37c8                                        |    134 |   0.7 | 134 |   0.7
stack.go:103                                        |    134 |   0.7 | 134 |   0.7
<autogenerated>:1                                   |    112 |   0.6 | 112 |   0.6
malloc.go:1183                                      |    102 |   0.6 | 102 |   0.6
instructions.go:902                                 |     92 |   0.5 |  92 |   0.5
memclr_amd64.s:81                                   |     90 |   0.5 |  90 |   0.5