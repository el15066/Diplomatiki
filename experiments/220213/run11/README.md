### Automated

```
[ perf record: Woken up 16 times to write data ]
[ perf record: Captured and wrote 4.080 MB /tmp2/p (19106 samples) ]
Wall time: 97.872 seconds
```

#### stack_top_own

Name                                             | Shared |   %   | Own |   %
-------------------------------------------------|--------|-------|-----|------
mutation.go:89                                   |    727 |   3.8 | 727 |   3.8
compare_amd64.s:49                               |    714 |   3.7 | 714 |   3.7
interpreter.go:326                               |    500 |   2.6 | 500 |   2.6
interpreter.go:259                               |    487 |   2.5 | 487 |   2.5
interpreter.go:266                               |    368 |   1.9 | 368 |   1.9
interpreter.go:262                               |    327 |   1.7 | 327 |   1.7
43801c                                           |    307 |   1.6 | 307 |   1.6
stack.go:67                                      |    304 |   1.6 | 304 |   1.6
stack.go:96                                      |    269 |   1.4 | 269 |   1.4
btree.go:189                                     |    267 |   1.4 | 267 |   1.4
44331c                                           |    250 |   1.3 | 250 |   1.3
uint256.go:1019                                  |    185 |   1.0 | 185 |   1.0
malloc.go:852                                    |    176 |   0.9 | 176 |   0.9
sha3.go:110                                      |    144 |   0.8 | 144 |   0.8
instructions.go:950                              |    132 |   0.7 | 132 |   0.7
interpreter.go:293                               |    130 |   0.7 | 130 |   0.7
7ffe7936c7c8                                     |    124 |   0.6 | 124 |   0.6
memclr_amd64.s:79                                |    115 |   0.6 | 115 |   0.6
uint256.go:110                                   |    114 |   0.6 | 114 |   0.6
stack.go:48                                      |    106 |   0.6 | 106 |   0.6
