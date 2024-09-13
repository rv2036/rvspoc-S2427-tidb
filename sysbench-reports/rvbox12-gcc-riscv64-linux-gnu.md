# RVBox12 gcc-riscv64-linux-gnu 编译器（默认参数）
## 编译
```shell
$ GOOS=linux GOARCH=riscv64 CC=riscv64-linux-gnu-gcc make server
```

## 测试
Point Select
```shell
hanbings@sophgo-farm-entrypoint:~$ ./sysbench --config-file=config oltp_point_select --tables=32 --table-size=1000000 --db-ps-mode=auto --rand-type=uniform run
sysbench 1.1.0-de18a03 (using bundled LuaJIT 2.1.0-beta3)

Running the test with following options:
Number of threads: 16
Report intermediate results every 10 second(s)
Initializing random number generator from current time


Initializing worker threads...

Threads started!

[ 10s ] thds: 16 tps: 202.66 qps: 202.66 (r/w/o: 202.66/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 20s ] thds: 16 tps: 197.30 qps: 197.30 (r/w/o: 197.30/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 30s ] thds: 16 tps: 196.80 qps: 196.80 (r/w/o: 196.80/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 40s ] thds: 16 tps: 198.40 qps: 198.40 (r/w/o: 198.40/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 50s ] thds: 16 tps: 196.80 qps: 196.80 (r/w/o: 196.80/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 60s ] thds: 16 tps: 198.30 qps: 198.30 (r/w/o: 198.30/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 70s ] thds: 16 tps: 196.90 qps: 196.90 (r/w/o: 196.90/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 80s ] thds: 16 tps: 198.40 qps: 198.40 (r/w/o: 198.40/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 90s ] thds: 16 tps: 196.80 qps: 196.80 (r/w/o: 196.80/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 100s ] thds: 16 tps: 198.40 qps: 198.40 (r/w/o: 198.40/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 110s ] thds: 16 tps: 198.20 qps: 198.20 (r/w/o: 198.20/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 120s ] thds: 16 tps: 197.00 qps: 197.00 (r/w/o: 197.00/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 130s ] thds: 16 tps: 198.20 qps: 198.20 (r/w/o: 198.20/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 140s ] thds: 16 tps: 197.00 qps: 197.00 (r/w/o: 197.00/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 150s ] thds: 16 tps: 198.20 qps: 198.20 (r/w/o: 198.20/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 160s ] thds: 16 tps: 197.00 qps: 197.00 (r/w/o: 197.00/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 170s ] thds: 16 tps: 198.20 qps: 198.20 (r/w/o: 198.20/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 180s ] thds: 16 tps: 197.00 qps: 197.00 (r/w/o: 197.00/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 190s ] thds: 16 tps: 198.20 qps: 198.20 (r/w/o: 198.20/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 200s ] thds: 16 tps: 197.00 qps: 197.00 (r/w/o: 197.00/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 210s ] thds: 16 tps: 196.80 qps: 196.80 (r/w/o: 196.80/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 220s ] thds: 16 tps: 198.40 qps: 198.40 (r/w/o: 198.40/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 230s ] thds: 16 tps: 196.80 qps: 196.80 (r/w/o: 196.80/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 240s ] thds: 16 tps: 204.80 qps: 204.80 (r/w/o: 204.80/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 250s ] thds: 16 tps: 196.80 qps: 196.80 (r/w/o: 196.80/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 260s ] thds: 16 tps: 198.40 qps: 198.40 (r/w/o: 198.40/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 270s ] thds: 16 tps: 198.40 qps: 198.40 (r/w/o: 198.40/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 280s ] thds: 16 tps: 197.00 qps: 197.00 (r/w/o: 197.00/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 290s ] thds: 16 tps: 198.30 qps: 198.30 (r/w/o: 198.30/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 300s ] thds: 16 tps: 198.30 qps: 198.30 (r/w/o: 198.30/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 310s ] thds: 16 tps: 197.00 qps: 197.00 (r/w/o: 197.00/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 320s ] thds: 16 tps: 198.40 qps: 198.40 (r/w/o: 198.40/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 330s ] thds: 16 tps: 198.30 qps: 198.30 (r/w/o: 198.30/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 340s ] thds: 16 tps: 198.20 qps: 198.20 (r/w/o: 198.20/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 350s ] thds: 16 tps: 197.10 qps: 197.10 (r/w/o: 197.10/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 360s ] thds: 16 tps: 198.30 qps: 198.30 (r/w/o: 198.30/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 370s ] thds: 16 tps: 198.00 qps: 198.00 (r/w/o: 198.00/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 380s ] thds: 16 tps: 197.30 qps: 197.30 (r/w/o: 197.30/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 390s ] thds: 16 tps: 198.40 qps: 198.40 (r/w/o: 198.40/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 400s ] thds: 16 tps: 198.30 qps: 198.30 (r/w/o: 198.30/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 410s ] thds: 16 tps: 198.00 qps: 198.00 (r/w/o: 198.00/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 420s ] thds: 16 tps: 197.30 qps: 197.30 (r/w/o: 197.30/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 430s ] thds: 16 tps: 198.40 qps: 198.40 (r/w/o: 198.40/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 440s ] thds: 16 tps: 198.30 qps: 198.30 (r/w/o: 198.30/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 450s ] thds: 16 tps: 198.10 qps: 198.10 (r/w/o: 198.10/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 460s ] thds: 16 tps: 198.30 qps: 198.30 (r/w/o: 198.30/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 470s ] thds: 16 tps: 197.30 qps: 197.30 (r/w/o: 197.30/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 480s ] thds: 16 tps: 198.30 qps: 198.30 (r/w/o: 198.30/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 490s ] thds: 16 tps: 198.00 qps: 198.00 (r/w/o: 198.00/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 500s ] thds: 16 tps: 197.30 qps: 197.30 (r/w/o: 197.30/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 510s ] thds: 16 tps: 198.30 qps: 198.30 (r/w/o: 198.30/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 520s ] thds: 16 tps: 198.00 qps: 198.00 (r/w/o: 198.00/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 530s ] thds: 16 tps: 197.30 qps: 197.30 (r/w/o: 197.30/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 540s ] thds: 16 tps: 198.30 qps: 198.30 (r/w/o: 198.30/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 550s ] thds: 16 tps: 198.00 qps: 198.00 (r/w/o: 198.00/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 560s ] thds: 16 tps: 198.40 qps: 198.40 (r/w/o: 198.40/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 570s ] thds: 16 tps: 197.20 qps: 197.20 (r/w/o: 197.20/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 580s ] thds: 16 tps: 198.00 qps: 198.00 (r/w/o: 198.00/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 590s ] thds: 16 tps: 197.30 qps: 197.30 (r/w/o: 197.30/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 600s ] thds: 16 tps: 198.30 qps: 198.30 (r/w/o: 198.30/0.00/0.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
SQL statistics:
    queries performed:
        read:                            118801
        write:                           0
        other:                           0
        total:                           118801
    transactions:                        118801 (197.98 per sec.)
    queries:                             118801 (197.98 per sec.)
    ignored errors:                      0      (0.00 per sec.)
    reconnects:                          0      (0.00 per sec.)

Throughput:
    events/s (eps):                      197.9794
    time elapsed:                        600.0676s
    total number of events:              118801

Latency (ms):
         min:                                   53.88
         avg:                                   80.81
         max:                                  116.93
         95th percentile:                       81.48
         sum:                              9600623.17

Threads fairness:
    events (avg/stddev):           7425.0625/0.24
    execution time (avg/stddev):   600.0389/0.01
```

Update Index
```shell
hanbings@sophgo-farm-entrypoint:~$ ./sysbench --config-file=config oltp_update_index --tables=32 --table-size=1000000 --db-ps-mode=auto --rand-type=uniform run
sysbench 1.1.0-de18a03 (using bundled LuaJIT 2.1.0-beta3)

Running the test with following options:
Number of threads: 16
Report intermediate results every 10 second(s)
Initializing random number generator from current time


Initializing worker threads...

Threads started!

[ 10s ] thds: 16 tps: 225.65 qps: 225.65 (r/w/o: 0.00/222.66/3.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 20s ] thds: 16 tps: 198.31 qps: 198.31 (r/w/o: 0.00/195.31/3.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 30s ] thds: 16 tps: 197.00 qps: 197.00 (r/w/o: 0.00/194.90/2.10) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 40s ] thds: 16 tps: 199.80 qps: 199.80 (r/w/o: 0.00/197.30/2.50) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 50s ] thds: 16 tps: 197.00 qps: 197.00 (r/w/o: 0.00/193.70/3.30) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 60s ] thds: 16 tps: 198.30 qps: 198.30 (r/w/o: 0.00/195.20/3.10) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 70s ] thds: 16 tps: 198.30 qps: 198.30 (r/w/o: 0.00/195.50/2.80) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 80s ] thds: 16 tps: 198.40 qps: 198.40 (r/w/o: 0.00/195.70/2.70) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 90s ] thds: 16 tps: 197.00 qps: 197.00 (r/w/o: 0.00/194.20/2.80) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 100s ] thds: 16 tps: 198.40 qps: 198.40 (r/w/o: 0.00/196.00/2.40) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 110s ] thds: 16 tps: 197.70 qps: 197.70 (r/w/o: 0.00/195.80/1.90) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 120s ] thds: 16 tps: 198.40 qps: 198.40 (r/w/o: 0.00/196.20/2.20) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 130s ] thds: 16 tps: 197.60 qps: 197.60 (r/w/o: 0.00/194.40/3.20) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 140s ] thds: 16 tps: 197.60 qps: 197.60 (r/w/o: 0.00/194.80/2.80) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 150s ] thds: 16 tps: 198.20 qps: 198.20 (r/w/o: 0.00/194.90/3.30) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 160s ] thds: 16 tps: 198.50 qps: 198.50 (r/w/o: 0.00/196.00/2.50) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 170s ] thds: 16 tps: 198.30 qps: 198.30 (r/w/o: 0.00/194.30/4.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 180s ] thds: 16 tps: 198.50 qps: 198.50 (r/w/o: 0.00/195.40/3.10) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 190s ] thds: 16 tps: 199.20 qps: 199.20 (r/w/o: 0.00/196.60/2.60) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 200s ] thds: 16 tps: 199.10 qps: 199.10 (r/w/o: 0.00/196.50/2.60) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 210s ] thds: 16 tps: 198.40 qps: 198.40 (r/w/o: 0.00/195.00/3.40) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 220s ] thds: 16 tps: 197.70 qps: 197.70 (r/w/o: 0.00/194.80/2.90) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 230s ] thds: 16 tps: 197.60 qps: 197.60 (r/w/o: 0.00/194.60/3.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 240s ] thds: 16 tps: 198.30 qps: 198.30 (r/w/o: 0.00/195.10/3.20) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 250s ] thds: 16 tps: 198.40 qps: 198.40 (r/w/o: 0.00/195.30/3.10) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 260s ] thds: 16 tps: 197.70 qps: 197.70 (r/w/o: 0.00/194.60/3.10) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 270s ] thds: 16 tps: 197.60 qps: 197.60 (r/w/o: 0.00/194.30/3.30) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 280s ] thds: 16 tps: 199.20 qps: 199.20 (r/w/o: 0.00/196.00/3.20) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 290s ] thds: 16 tps: 197.60 qps: 197.60 (r/w/o: 0.00/194.80/2.80) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 300s ] thds: 16 tps: 198.30 qps: 198.30 (r/w/o: 0.00/195.00/3.30) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 310s ] thds: 16 tps: 197.50 qps: 197.50 (r/w/o: 0.00/195.80/1.70) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 320s ] thds: 16 tps: 198.40 qps: 198.40 (r/w/o: 0.00/195.40/3.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 330s ] thds: 16 tps: 197.80 qps: 197.80 (r/w/o: 0.00/194.00/3.80) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 340s ] thds: 16 tps: 198.40 qps: 198.40 (r/w/o: 0.00/195.00/3.40) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 350s ] thds: 16 tps: 197.20 qps: 197.20 (r/w/o: 0.00/194.40/2.80) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 360s ] thds: 16 tps: 198.40 qps: 198.40 (r/w/o: 0.00/195.10/3.30) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 370s ] thds: 16 tps: 198.40 qps: 198.40 (r/w/o: 0.00/195.30/3.10) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 380s ] thds: 16 tps: 196.90 qps: 196.90 (r/w/o: 0.00/195.40/1.50) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 390s ] thds: 16 tps: 197.70 qps: 197.70 (r/w/o: 0.00/194.30/3.40) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 400s ] thds: 16 tps: 198.40 qps: 198.40 (r/w/o: 0.00/194.60/3.80) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 410s ] thds: 16 tps: 198.40 qps: 198.40 (r/w/o: 0.00/195.30/3.10) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 420s ] thds: 16 tps: 198.40 qps: 198.40 (r/w/o: 0.00/195.70/2.70) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 430s ] thds: 16 tps: 198.20 qps: 198.20 (r/w/o: 0.00/195.10/3.10) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 440s ] thds: 16 tps: 198.40 qps: 198.40 (r/w/o: 0.00/195.40/3.00) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 450s ] thds: 16 tps: 198.40 qps: 198.40 (r/w/o: 0.00/194.70/3.70) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 460s ] thds: 16 tps: 197.40 qps: 197.40 (r/w/o: 0.00/195.20/2.20) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 470s ] thds: 16 tps: 198.00 qps: 198.00 (r/w/o: 0.00/195.90/2.10) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 480s ] thds: 16 tps: 198.40 qps: 198.40 (r/w/o: 0.00/195.50/2.90) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 490s ] thds: 16 tps: 197.90 qps: 197.90 (r/w/o: 0.00/194.20/3.70) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 500s ] thds: 16 tps: 197.70 qps: 197.70 (r/w/o: 0.00/194.80/2.90) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 510s ] thds: 16 tps: 198.40 qps: 198.40 (r/w/o: 0.00/195.80/2.60) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 520s ] thds: 16 tps: 198.00 qps: 198.00 (r/w/o: 0.00/195.70/2.30) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 530s ] thds: 16 tps: 198.40 qps: 198.40 (r/w/o: 0.00/195.10/3.30) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 540s ] thds: 16 tps: 209.30 qps: 209.30 (r/w/o: 0.00/206.60/2.70) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 550s ] thds: 16 tps: 198.20 qps: 198.20 (r/w/o: 0.00/194.90/3.30) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 560s ] thds: 16 tps: 197.50 qps: 197.50 (r/w/o: 0.00/195.40/2.10) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 570s ] thds: 16 tps: 199.20 qps: 199.20 (r/w/o: 0.00/196.70/2.50) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 580s ] thds: 16 tps: 198.40 qps: 198.40 (r/w/o: 0.00/195.90/2.50) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 590s ] thds: 16 tps: 197.60 qps: 197.60 (r/w/o: 0.00/195.20/2.40) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
[ 600s ] thds: 16 tps: 198.40 qps: 198.40 (r/w/o: 0.00/195.50/2.90) lat (ms,95%): 81.48 err/s: 0.00 reconn/s: 0.00
SQL statistics:
    queries performed:
        read:                            0
        write:                           117544
        other:                           1730
        total:                           119274
    transactions:                        119274 (198.77 per sec.)
    queries:                             119274 (198.77 per sec.)
    ignored errors:                      0      (0.00 per sec.)
    reconnects:                          0      (0.00 per sec.)

Throughput:
    events/s (eps):                      198.7684
    time elapsed:                        600.0652s
    total number of events:              119274

Latency (ms):
         min:                                   33.52
         avg:                                   80.49
         max:                                  219.21
         95th percentile:                       81.48
         sum:                              9600401.91

Threads fairness:
    events (avg/stddev):           7454.6250/0.93
    execution time (avg/stddev):   600.0251/0.02
```

Read Only
```shell
hanbings@sophgo-farm-entrypoint:~$ ./sysbench --config-file=config oltp_read_only --tables=32 --table-size=1000000 --db-ps-mode=auto --rand-type=uniform run
sysbench 1.1.0-de18a03 (using bundled LuaJIT 2.1.0-beta3)

Running the test with following options:
Number of threads: 16
Report intermediate results every 10 second(s)
Initializing random number generator from current time


Initializing worker threads...

Threads started!

[ 10s ] thds: 16 tps: 11.80 qps: 204.06 (r/w/o: 179.36/0.00/24.69) lat (ms,95%): 1327.91 err/s: 0.00 reconn/s: 0.00
[ 20s ] thds: 16 tps: 12.30 qps: 202.21 (r/w/o: 177.11/0.00/25.10) lat (ms,95%): 1304.21 err/s: 0.00 reconn/s: 0.00
[ 30s ] thds: 16 tps: 12.80 qps: 202.30 (r/w/o: 176.70/0.00/25.60) lat (ms,95%): 1304.21 err/s: 0.00 reconn/s: 0.00
[ 40s ] thds: 16 tps: 12.80 qps: 200.90 (r/w/o: 175.30/0.00/25.60) lat (ms,95%): 1327.91 err/s: 0.00 reconn/s: 0.00
[ 50s ] thds: 16 tps: 12.80 qps: 200.70 (r/w/o: 175.10/0.00/25.60) lat (ms,95%): 1304.21 err/s: 0.00 reconn/s: 0.00
[ 60s ] thds: 16 tps: 12.80 qps: 197.60 (r/w/o: 172.00/0.00/25.60) lat (ms,95%): 1304.21 err/s: 0.00 reconn/s: 0.00
[ 70s ] thds: 16 tps: 11.30 qps: 198.30 (r/w/o: 175.80/0.00/22.50) lat (ms,95%): 1327.91 err/s: 0.00 reconn/s: 0.00
[ 80s ] thds: 16 tps: 12.70 qps: 203.80 (r/w/o: 178.30/0.00/25.50) lat (ms,95%): 1304.21 err/s: 0.00 reconn/s: 0.00
[ 90s ] thds: 16 tps: 12.80 qps: 202.70 (r/w/o: 177.10/0.00/25.60) lat (ms,95%): 1304.21 err/s: 0.00 reconn/s: 0.00
[ 100s ] thds: 16 tps: 12.80 qps: 209.10 (r/w/o: 183.50/0.00/25.60) lat (ms,95%): 1280.93 err/s: 0.00 reconn/s: 0.00
[ 110s ] thds: 16 tps: 12.80 qps: 198.80 (r/w/o: 173.20/0.00/25.60) lat (ms,95%): 1304.21 err/s: 0.00 reconn/s: 0.00
[ 120s ] thds: 16 tps: 12.80 qps: 201.90 (r/w/o: 176.30/0.00/25.60) lat (ms,95%): 1327.91 err/s: 0.00 reconn/s: 0.00
[ 130s ] thds: 16 tps: 12.90 qps: 205.90 (r/w/o: 180.20/0.00/25.70) lat (ms,95%): 1304.21 err/s: 0.00 reconn/s: 0.00
[ 140s ] thds: 16 tps: 12.80 qps: 204.10 (r/w/o: 178.40/0.00/25.70) lat (ms,95%): 1304.21 err/s: 0.00 reconn/s: 0.00
[ 150s ] thds: 16 tps: 12.80 qps: 202.30 (r/w/o: 176.70/0.00/25.60) lat (ms,95%): 1304.21 err/s: 0.00 reconn/s: 0.00
[ 160s ] thds: 16 tps: 12.80 qps: 203.20 (r/w/o: 177.60/0.00/25.60) lat (ms,95%): 1304.21 err/s: 0.00 reconn/s: 0.00
[ 170s ] thds: 16 tps: 12.80 qps: 201.70 (r/w/o: 176.10/0.00/25.60) lat (ms,95%): 1352.03 err/s: 0.00 reconn/s: 0.00
[ 180s ] thds: 16 tps: 12.80 qps: 205.80 (r/w/o: 180.20/0.00/25.60) lat (ms,95%): 1304.21 err/s: 0.00 reconn/s: 0.00
[ 190s ] thds: 16 tps: 12.80 qps: 203.00 (r/w/o: 177.40/0.00/25.60) lat (ms,95%): 1327.91 err/s: 0.00 reconn/s: 0.00
[ 200s ] thds: 16 tps: 12.90 qps: 203.60 (r/w/o: 177.80/0.00/25.80) lat (ms,95%): 1327.91 err/s: 0.00 reconn/s: 0.00
[ 210s ] thds: 16 tps: 12.80 qps: 202.90 (r/w/o: 178.50/0.00/24.40) lat (ms,95%): 1304.21 err/s: 0.00 reconn/s: 0.00
[ 220s ] thds: 16 tps: 12.10 qps: 204.40 (r/w/o: 179.40/0.00/25.00) lat (ms,95%): 1304.21 err/s: 0.00 reconn/s: 0.00
[ 230s ] thds: 16 tps: 13.10 qps: 205.30 (r/w/o: 179.60/0.00/25.70) lat (ms,95%): 1304.21 err/s: 0.00 reconn/s: 0.00
[ 240s ] thds: 16 tps: 11.80 qps: 202.00 (r/w/o: 177.50/0.00/24.50) lat (ms,95%): 1304.21 err/s: 0.00 reconn/s: 0.00
[ 250s ] thds: 16 tps: 12.70 qps: 198.90 (r/w/o: 173.50/0.00/25.40) lat (ms,95%): 1304.21 err/s: 0.00 reconn/s: 0.00
[ 260s ] thds: 16 tps: 12.80 qps: 199.90 (r/w/o: 174.30/0.00/25.60) lat (ms,95%): 1327.91 err/s: 0.00 reconn/s: 0.00
[ 270s ] thds: 16 tps: 12.80 qps: 202.10 (r/w/o: 176.50/0.00/25.60) lat (ms,95%): 1327.91 err/s: 0.00 reconn/s: 0.00
[ 280s ] thds: 16 tps: 12.80 qps: 200.00 (r/w/o: 174.40/0.00/25.60) lat (ms,95%): 1304.21 err/s: 0.00 reconn/s: 0.00
[ 290s ] thds: 16 tps: 12.10 qps: 201.60 (r/w/o: 177.90/0.00/23.70) lat (ms,95%): 1304.21 err/s: 0.00 reconn/s: 0.00
[ 300s ] thds: 16 tps: 12.10 qps: 203.70 (r/w/o: 179.00/0.00/24.70) lat (ms,95%): 1304.21 err/s: 0.00 reconn/s: 0.00
[ 310s ] thds: 16 tps: 13.40 qps: 206.50 (r/w/o: 180.30/0.00/26.20) lat (ms,95%): 1304.21 err/s: 0.00 reconn/s: 0.00
[ 320s ] thds: 16 tps: 12.20 qps: 201.40 (r/w/o: 176.40/0.00/25.00) lat (ms,95%): 1304.21 err/s: 0.00 reconn/s: 0.00
[ 330s ] thds: 16 tps: 12.80 qps: 201.80 (r/w/o: 176.20/0.00/25.60) lat (ms,95%): 1304.21 err/s: 0.00 reconn/s: 0.00
[ 340s ] thds: 16 tps: 12.80 qps: 205.00 (r/w/o: 179.40/0.00/25.60) lat (ms,95%): 1304.21 err/s: 0.00 reconn/s: 0.00
[ 350s ] thds: 16 tps: 12.80 qps: 204.40 (r/w/o: 178.80/0.00/25.60) lat (ms,95%): 1304.21 err/s: 0.00 reconn/s: 0.00
[ 360s ] thds: 16 tps: 12.80 qps: 203.10 (r/w/o: 177.50/0.00/25.60) lat (ms,95%): 1304.21 err/s: 0.00 reconn/s: 0.00
[ 370s ] thds: 16 tps: 12.90 qps: 205.30 (r/w/o: 179.50/0.00/25.80) lat (ms,95%): 1304.21 err/s: 0.00 reconn/s: 0.00
[ 380s ] thds: 16 tps: 12.80 qps: 204.80 (r/w/o: 179.20/0.00/25.60) lat (ms,95%): 1304.21 err/s: 0.00 reconn/s: 0.00
[ 390s ] thds: 16 tps: 12.80 qps: 204.00 (r/w/o: 178.40/0.00/25.60) lat (ms,95%): 1304.21 err/s: 0.00 reconn/s: 0.00
[ 400s ] thds: 16 tps: 12.80 qps: 201.90 (r/w/o: 176.30/0.00/25.60) lat (ms,95%): 1304.21 err/s: 0.00 reconn/s: 0.00
[ 410s ] thds: 16 tps: 12.80 qps: 197.40 (r/w/o: 171.80/0.00/25.60) lat (ms,95%): 1327.91 err/s: 0.00 reconn/s: 0.00
[ 420s ] thds: 16 tps: 12.80 qps: 203.00 (r/w/o: 178.20/0.00/24.80) lat (ms,95%): 1304.21 err/s: 0.00 reconn/s: 0.00
[ 430s ] thds: 16 tps: 11.30 qps: 201.60 (r/w/o: 178.30/0.00/23.30) lat (ms,95%): 1352.03 err/s: 0.00 reconn/s: 0.00
[ 440s ] thds: 16 tps: 12.80 qps: 202.60 (r/w/o: 177.00/0.00/25.60) lat (ms,95%): 1304.21 err/s: 0.00 reconn/s: 0.00
[ 450s ] thds: 16 tps: 12.70 qps: 200.80 (r/w/o: 175.30/0.00/25.50) lat (ms,95%): 1327.91 err/s: 0.00 reconn/s: 0.00
[ 460s ] thds: 16 tps: 12.90 qps: 209.60 (r/w/o: 183.90/0.00/25.70) lat (ms,95%): 1327.91 err/s: 0.00 reconn/s: 0.00
[ 470s ] thds: 16 tps: 12.70 qps: 203.50 (r/w/o: 178.00/0.00/25.50) lat (ms,95%): 1304.21 err/s: 0.00 reconn/s: 0.00
[ 480s ] thds: 16 tps: 12.80 qps: 196.90 (r/w/o: 171.30/0.00/25.60) lat (ms,95%): 1304.21 err/s: 0.00 reconn/s: 0.00
[ 490s ] thds: 16 tps: 12.80 qps: 194.60 (r/w/o: 169.10/0.00/25.50) lat (ms,95%): 1327.91 err/s: 0.00 reconn/s: 0.00
[ 500s ] thds: 16 tps: 11.20 qps: 197.00 (r/w/o: 174.50/0.00/22.50) lat (ms,95%): 1327.91 err/s: 0.00 reconn/s: 0.00
[ 510s ] thds: 16 tps: 12.90 qps: 204.10 (r/w/o: 178.30/0.00/25.80) lat (ms,95%): 1304.21 err/s: 0.00 reconn/s: 0.00
[ 520s ] thds: 16 tps: 12.80 qps: 201.60 (r/w/o: 176.00/0.00/25.60) lat (ms,95%): 1304.21 err/s: 0.00 reconn/s: 0.00
[ 530s ] thds: 16 tps: 12.80 qps: 204.10 (r/w/o: 178.50/0.00/25.60) lat (ms,95%): 1304.21 err/s: 0.00 reconn/s: 0.00
[ 540s ] thds: 16 tps: 12.80 qps: 200.30 (r/w/o: 174.70/0.00/25.60) lat (ms,95%): 1304.21 err/s: 0.00 reconn/s: 0.00
[ 550s ] thds: 16 tps: 12.20 qps: 195.10 (r/w/o: 171.10/0.00/24.00) lat (ms,95%): 1327.91 err/s: 0.00 reconn/s: 0.00
[ 560s ] thds: 16 tps: 11.80 qps: 196.00 (r/w/o: 172.00/0.00/24.00) lat (ms,95%): 1327.91 err/s: 0.00 reconn/s: 0.00
[ 570s ] thds: 16 tps: 12.80 qps: 203.60 (r/w/o: 178.00/0.00/25.60) lat (ms,95%): 1304.21 err/s: 0.00 reconn/s: 0.00
[ 580s ] thds: 16 tps: 12.80 qps: 202.00 (r/w/o: 176.40/0.00/25.60) lat (ms,95%): 1304.21 err/s: 0.00 reconn/s: 0.00
[ 590s ] thds: 16 tps: 12.80 qps: 201.80 (r/w/o: 176.20/0.00/25.60) lat (ms,95%): 1304.21 err/s: 0.00 reconn/s: 0.00
[ 600s ] thds: 16 tps: 12.80 qps: 202.30 (r/w/o: 176.70/0.00/25.60) lat (ms,95%): 1304.21 err/s: 0.00 reconn/s: 0.00
SQL statistics:
    queries performed:
        read:                            106288
        write:                           0
        other:                           15184
        total:                           121472
    transactions:                        7592   (12.63 per sec.)
    queries:                             121472 (202.12 per sec.)
    ignored errors:                      0      (0.00 per sec.)
    reconnects:                          0      (0.00 per sec.)

Throughput:
    events/s (eps):                      12.6327
    time elapsed:                        600.9789s
    total number of events:              7592

Latency (ms):
         min:                                  909.25
         avg:                                 1266.35
         max:                                 1394.78
         95th percentile:                     1304.21
         sum:                              9614119.40

Threads fairness:
    events (avg/stddev):           474.5000/1.46
    execution time (avg/stddev):   600.8825/0.21

```