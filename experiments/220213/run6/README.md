### Automated

```
[ perf record: Woken up 16 times to write data ]
[ perf record: Captured and wrote 4.096 MB /tmp2/p (19253 samples) ]
Wall time: 98.619 seconds
```

#### stack_top_own

Name                                             | Shared |   %   | Own |   %
-------------------------------------------------|--------|-------|-----|------
compare_amd64.s:49                               |    707 |   3.7 | 707 |   3.7
mutation.go:89                                   |    651 |   3.4 | 651 |   3.4
interpreter.go:259                               |    532 |   2.8 | 532 |   2.8
interpreter.go:326                               |    445 |   2.3 | 445 |   2.3
interpreter.go:266                               |    359 |   1.9 | 359 |   1.9
btree.go:189                                     |    354 |   1.8 | 354 |   1.8
43801c                                           |    342 |   1.8 | 342 |   1.8
interpreter.go:262                               |    337 |   1.8 | 337 |   1.8
stack.go:62                                      |    305 |   1.6 | 305 |   1.6
44331c                                           |    274 |   1.4 | 274 |   1.4
stack.go:48                                      |    247 |   1.3 | 247 |   1.3
malloc.go:852                                    |    180 |   0.9 | 180 |   0.9
sha3.go:110                                      |    171 |   0.9 | 171 |   0.9
instructions.go:950                              |    149 |   0.8 | 149 |   0.8
7ffcdb6b87c8                                     |    136 |   0.7 | 136 |   0.7
stack.go:45                                      |    134 |   0.7 | 134 |   0.7
instructions.go:906                              |    122 |   0.6 | 122 |   0.6
uint256.go:110                                   |    118 |   0.6 | 118 |   0.6
memclr_amd64.s:81                                |    111 |   0.6 | 111 |   0.6
stack.go:91                                      |    110 |   0.6 | 110 |   0.6
