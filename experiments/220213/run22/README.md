### Automated

```
[ perf record: Woken up 16 times to write data ]
[ perf record: Captured and wrote 3.977 MB /tmp2/p (18704 samples) ]
Wall time: 95.838 seconds
```

#### stack_top_own

Name                                             | Shared |   %   | Own |   %
-------------------------------------------------|--------|-------|-----|------
compare_amd64.s:49                               |    768 |   4.1 | 768 |   4.1
mutation.go:89                                   |    683 |   3.7 | 683 |   3.7
interpreter.go:259                               |    510 |   2.7 | 510 |   2.7
interpreter.go:326                               |    493 |   2.6 | 493 |   2.6
interpreter.go:262                               |    395 |   2.1 | 395 |   2.1
interpreter.go:266                               |    336 |   1.8 | 336 |   1.8
btree.go:189                                     |    322 |   1.7 | 322 |   1.7
43801c                                           |    319 |   1.7 | 319 |   1.7
44331c                                           |    300 |   1.6 | 300 |   1.6
uint256.go:1019                                  |    238 |   1.3 | 238 |   1.3
malloc.go:852                                    |    197 |   1.1 | 197 |   1.1
sha3.go:110                                      |    151 |   0.8 | 151 |   0.8
7ffdd30d77c8                                     |    133 |   0.7 | 133 |   0.7
stack.go:75                                      |    130 |   0.7 | 130 |   0.7
stack.go:103                                     |    127 |   0.7 | 127 |   0.7
instructions.go:946                              |    126 |   0.7 | 126 |   0.7
interpreter.go:293                               |    116 |   0.6 | 116 |   0.6
<autogenerated>:1                                |    105 |   0.6 | 105 |   0.6
malloc.go:1183                                   |     98 |   0.5 |  98 |   0.5
memclr_amd64.s:81                                |     97 |   0.5 |  97 |   0.5