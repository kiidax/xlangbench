Benchmark Results
=================

Tested on AMD A6-3500 2.10 GHz / 8GB ram on Windows 8.1 or Fedora 20
on VirtualBox.

#### C++ for Microsoft Visual C++ 2013

```
loading: 500000 test items
start
time: 1425ms
time: 2837ms
time: 4253ms
time: 5657ms
```

#### C++ for Fedora 20 64 bit GCC 4.8.3

```
loading: 500000 test items
start
time: 1673.76ms
time: 3439.98ms
time: 5315.46ms
time: 6853.5ms
```

#### C++ for Fedora 20 64 bit clang 3.4

```
loading: 500000 test items
start
time: 1551.59ms
time: 3113.26ms
time: 4875.91ms
time: 6311.61ms
```

#### C++ for MinGW GCC 4.8.1

Am I wrong here?

http://mingw-users.1079350.n2.nabble.com/GCC-compiled-code-very-slow-compared-to-MS-Visual-C-td5939586.html

```
loading: 500000 test items
start
time: 4842ms
time: 9643ms
time: 14646ms
time: 19252ms
```

#### C# for Windows

```
loading: 500000 test items
start
time: 2469ms
time: 4656ms
time: 7750ms
time: 10453ms
```

#### Oracle Java 1.8 64 bit on Windows

```
loading: 500000 test items
start
time: 3565.69983ms
time: 6610.798928ms
time: 9301.112781ms
time: 12324.496409ms
```

#### OpenJDK 1.7.0 64 bit on Fedora 20

```
loading: 500000 test items
start
time: 2398.4446ms
time: 4682.367723ms
time: 8389.044726ms
time: 12874.764229ms
```

#### Oracle Java 1.8.0 64 bit on Fedora 20

```
loading: 500000 test items
start
time: 1955.370338ms
time: 5603.980805ms
time: 7724.275917ms
time: 10524.098671ms
```

#### JavaScript V8 (2014-09-20) on Windows

```
loading: 500000 test items
start
time: 3140
time: 5550
time: 8052
time: 14691
```

#### JavaScript V8 (2014-09-20) on Fedora 20 clang 3.4

```
loading: 500000 test items
start
time: 3230
time: 5690
time: 8228
time: 15761
```

#### Mozilla SpiderMonkey (JavaScript) on Fedora 20

```
loading: 500000 test items
start
bench.js:16: out of memory
```

#### Python 2.7.8 32 bit Windows

```
loading: 500000 test items
start
time: 2387ms
time: 4798ms
time: 7251ms
time: 9623ms
```

#### Scala 2.11.2 on Oracle Java 1.8.0 64 bit Windows

```
Loading: 500000 test items
start
time: 2432.040664
time: 5570.00373
time: 9635.500601
time: 12141.395275
```