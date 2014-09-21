Cross Language Benchmark
========================

This is a collection of console programs written in various
programming languages that emulate a toy messaging application. Each
program reads data from the file and process them, then show the time
spent. The programming is kept very simple so that adding a new
language should not a pain.

The current supported languages are

- C++
- C#
- Java
- JavaScript (V8)
- Python

## Preparation

Before you start benchmarking, you need to generate test data. It
includes fake user information. To generate it, you need to get three
files from
[United States Census Bereau](http://www.census.gov/genealogy/www/data/1990surnames/names_files.html).
They are frequently occurring names from U.S. Census 1990.

- dist.all.last (3107965 bytes)
- dist.female.first (149625 bytes)
- dist.male.first (42665 bytes)

Place them in the root directory of this package. Run

> python genfakeusers.py 5000 xlangbench > userdata.csv

The second argument is the random seed. It can be any string but need
to be the same to generate the same data. With Python 2.7.8 on 32 bit
Windows, the third and the fifth person are

- Leonard Jones,male,leonard.jones@example.net
- Meghan Castor,female,meghan.castor@example.org

The generated user data is in the CSV format, that includes name, sex
and e-mail address.

## Execute Benchmark

Each program loads data from userdata.csv and executes the benchmark
and generates four numbers. They are the time since the start of the
benchmark to process 500,000 messages for 5,000 users. They are
cumulative. So the fourth number is the time spent to process
2,000,000 messages.

#### C++ for Microsoft Visual C++

```
> cl /O2 /EHsc /Fe:bench_msvc.exe bench.cc
> bench_msvc.exe
```

#### C++ for Linux GCC

```
$ g++ -O2 bench.cc -o bench_gcc
$ ./bench_gcc
```

#### C++ for Linux clang

```
$ clang++ -O2 bench.cc -o bench_clang
$ ./bench_clang
```

#### C++ for MinGW GCC

```
$ g++ -O2 bench.cc -o bench_mingw.exe
$ ./bench_mingw.exe
```

#### C# for Windows

```
> csc /out:bench_cs.exe Bench.cs
> bench_cs.exe
```

#### Java

```
$ javac Bench.java
$ java Bench
```

#### V8 (JavaScript)

You need to build V8. Run

```
$ /path/to/v8/shell bench.js
```

#### Mozilla SpiderMonkey (JavaScript)

```
$ js bench.js
```

#### Python

```
$ python bench.py
```
