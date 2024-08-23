# RVBox13 Xuantie-900-gcc-linux-6.6.0-glibc-x86_64-V2.10.1 编译器（rv64imafdcv0p7_zfh_xtheadc）
## 编译
请注意替换 CC 的路径
```shell
$ CGO_CFLAGS=-march=rv64imafdcv0p7_zfh_xtheadc GOOS=linux GOARCH=riscv64 CC=/opt/Xuantie-900-gcc-linux-6.6.0-glibc-x86_64-V2.10.1/bin/riscv64-unknown-linux-gnu-gcc make server
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

[ 10s ] thds: 16 tps: 1726.98 qps: 1726.98 (r/w/o: 1726.98/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 20s ] thds: 16 tps: 1712.01 qps: 1712.01 (r/w/o: 1712.01/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 30s ] thds: 16 tps: 1698.20 qps: 1698.20 (r/w/o: 1698.20/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 40s ] thds: 16 tps: 1703.30 qps: 1703.30 (r/w/o: 1703.30/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 50s ] thds: 16 tps: 1700.40 qps: 1700.40 (r/w/o: 1700.40/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 60s ] thds: 16 tps: 1724.19 qps: 1724.19 (r/w/o: 1724.19/0.00/0.00) lat (ms,95%): 10.84 err/s: 0.00 reconn/s: 0.00
[ 70s ] thds: 16 tps: 1708.91 qps: 1708.91 (r/w/o: 1708.91/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 80s ] thds: 16 tps: 1707.50 qps: 1707.50 (r/w/o: 1707.50/0.00/0.00) lat (ms,95%): 10.46 err/s: 0.00 reconn/s: 0.00
[ 90s ] thds: 16 tps: 1707.80 qps: 1707.80 (r/w/o: 1707.80/0.00/0.00) lat (ms,95%): 10.46 err/s: 0.00 reconn/s: 0.00
[ 100s ] thds: 16 tps: 1721.19 qps: 1721.19 (r/w/o: 1721.19/0.00/0.00) lat (ms,95%): 10.46 err/s: 0.00 reconn/s: 0.00
[ 110s ] thds: 16 tps: 1661.00 qps: 1661.00 (r/w/o: 1661.00/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 120s ] thds: 16 tps: 1718.61 qps: 1718.61 (r/w/o: 1718.61/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 130s ] thds: 16 tps: 1711.80 qps: 1711.80 (r/w/o: 1711.80/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 140s ] thds: 16 tps: 1721.30 qps: 1721.30 (r/w/o: 1721.30/0.00/0.00) lat (ms,95%): 10.27 err/s: 0.00 reconn/s: 0.00
[ 150s ] thds: 16 tps: 1634.69 qps: 1634.69 (r/w/o: 1634.69/0.00/0.00) lat (ms,95%): 10.46 err/s: 0.00 reconn/s: 0.00
[ 160s ] thds: 16 tps: 1720.22 qps: 1720.22 (r/w/o: 1720.22/0.00/0.00) lat (ms,95%): 10.46 err/s: 0.00 reconn/s: 0.00
[ 170s ] thds: 16 tps: 1694.00 qps: 1694.00 (r/w/o: 1694.00/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 180s ] thds: 16 tps: 1702.40 qps: 1702.40 (r/w/o: 1702.40/0.00/0.00) lat (ms,95%): 10.84 err/s: 0.00 reconn/s: 0.00
[ 190s ] thds: 16 tps: 1718.39 qps: 1718.39 (r/w/o: 1718.39/0.00/0.00) lat (ms,95%): 10.46 err/s: 0.00 reconn/s: 0.00
[ 200s ] thds: 16 tps: 1699.31 qps: 1699.31 (r/w/o: 1699.31/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 210s ] thds: 16 tps: 1711.39 qps: 1711.39 (r/w/o: 1711.39/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 220s ] thds: 16 tps: 1714.01 qps: 1714.01 (r/w/o: 1714.01/0.00/0.00) lat (ms,95%): 10.27 err/s: 0.00 reconn/s: 0.00
[ 230s ] thds: 16 tps: 1719.30 qps: 1719.30 (r/w/o: 1719.30/0.00/0.00) lat (ms,95%): 10.46 err/s: 0.00 reconn/s: 0.00
[ 240s ] thds: 16 tps: 1738.10 qps: 1738.10 (r/w/o: 1738.10/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 250s ] thds: 16 tps: 1722.40 qps: 1722.40 (r/w/o: 1722.40/0.00/0.00) lat (ms,95%): 10.46 err/s: 0.00 reconn/s: 0.00
[ 260s ] thds: 16 tps: 1714.30 qps: 1714.30 (r/w/o: 1714.30/0.00/0.00) lat (ms,95%): 10.46 err/s: 0.00 reconn/s: 0.00
[ 270s ] thds: 16 tps: 1723.90 qps: 1723.90 (r/w/o: 1723.90/0.00/0.00) lat (ms,95%): 10.46 err/s: 0.00 reconn/s: 0.00
[ 280s ] thds: 16 tps: 1717.70 qps: 1717.70 (r/w/o: 1717.70/0.00/0.00) lat (ms,95%): 10.46 err/s: 0.00 reconn/s: 0.00
[ 290s ] thds: 16 tps: 1729.50 qps: 1729.50 (r/w/o: 1729.50/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 300s ] thds: 16 tps: 1708.60 qps: 1708.60 (r/w/o: 1708.60/0.00/0.00) lat (ms,95%): 10.84 err/s: 0.00 reconn/s: 0.00
[ 310s ] thds: 16 tps: 1731.11 qps: 1731.11 (r/w/o: 1731.11/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 320s ] thds: 16 tps: 1727.60 qps: 1727.60 (r/w/o: 1727.60/0.00/0.00) lat (ms,95%): 10.46 err/s: 0.00 reconn/s: 0.00
[ 330s ] thds: 16 tps: 1712.20 qps: 1712.20 (r/w/o: 1712.20/0.00/0.00) lat (ms,95%): 10.46 err/s: 0.00 reconn/s: 0.00
[ 340s ] thds: 16 tps: 1717.20 qps: 1717.20 (r/w/o: 1717.20/0.00/0.00) lat (ms,95%): 10.46 err/s: 0.00 reconn/s: 0.00
[ 350s ] thds: 16 tps: 1719.89 qps: 1719.89 (r/w/o: 1719.89/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 360s ] thds: 16 tps: 1711.31 qps: 1711.31 (r/w/o: 1711.31/0.00/0.00) lat (ms,95%): 10.84 err/s: 0.00 reconn/s: 0.00
[ 370s ] thds: 16 tps: 1717.30 qps: 1717.30 (r/w/o: 1717.30/0.00/0.00) lat (ms,95%): 10.46 err/s: 0.00 reconn/s: 0.00
[ 380s ] thds: 16 tps: 1719.70 qps: 1719.70 (r/w/o: 1719.70/0.00/0.00) lat (ms,95%): 10.46 err/s: 0.00 reconn/s: 0.00
[ 390s ] thds: 16 tps: 1715.40 qps: 1715.40 (r/w/o: 1715.40/0.00/0.00) lat (ms,95%): 10.46 err/s: 0.00 reconn/s: 0.00
[ 400s ] thds: 16 tps: 1720.40 qps: 1720.40 (r/w/o: 1720.40/0.00/0.00) lat (ms,95%): 10.46 err/s: 0.00 reconn/s: 0.00
[ 410s ] thds: 16 tps: 1698.59 qps: 1698.59 (r/w/o: 1698.59/0.00/0.00) lat (ms,95%): 10.46 err/s: 0.00 reconn/s: 0.00
[ 420s ] thds: 16 tps: 1715.01 qps: 1715.01 (r/w/o: 1715.01/0.00/0.00) lat (ms,95%): 10.46 err/s: 0.00 reconn/s: 0.00
[ 430s ] thds: 16 tps: 1708.30 qps: 1708.30 (r/w/o: 1708.30/0.00/0.00) lat (ms,95%): 10.46 err/s: 0.00 reconn/s: 0.00
[ 440s ] thds: 16 tps: 1715.69 qps: 1715.69 (r/w/o: 1715.69/0.00/0.00) lat (ms,95%): 10.46 err/s: 0.00 reconn/s: 0.00
[ 450s ] thds: 16 tps: 1717.31 qps: 1717.31 (r/w/o: 1717.31/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 460s ] thds: 16 tps: 1717.11 qps: 1717.11 (r/w/o: 1717.11/0.00/0.00) lat (ms,95%): 10.46 err/s: 0.00 reconn/s: 0.00
[ 470s ] thds: 16 tps: 1729.10 qps: 1729.10 (r/w/o: 1729.10/0.00/0.00) lat (ms,95%): 10.27 err/s: 0.00 reconn/s: 0.00
[ 480s ] thds: 16 tps: 1713.30 qps: 1713.30 (r/w/o: 1713.30/0.00/0.00) lat (ms,95%): 10.84 err/s: 0.00 reconn/s: 0.00
[ 490s ] thds: 16 tps: 1718.40 qps: 1718.40 (r/w/o: 1718.40/0.00/0.00) lat (ms,95%): 10.46 err/s: 0.00 reconn/s: 0.00
[ 500s ] thds: 16 tps: 1727.80 qps: 1727.80 (r/w/o: 1727.80/0.00/0.00) lat (ms,95%): 10.27 err/s: 0.00 reconn/s: 0.00
[ 510s ] thds: 16 tps: 1732.20 qps: 1732.20 (r/w/o: 1732.20/0.00/0.00) lat (ms,95%): 10.46 err/s: 0.00 reconn/s: 0.00
[ 520s ] thds: 16 tps: 1700.90 qps: 1700.90 (r/w/o: 1700.90/0.00/0.00) lat (ms,95%): 10.46 err/s: 0.00 reconn/s: 0.00
[ 530s ] thds: 16 tps: 1711.80 qps: 1711.80 (r/w/o: 1711.80/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 540s ] thds: 16 tps: 1712.01 qps: 1712.01 (r/w/o: 1712.01/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 550s ] thds: 16 tps: 1720.79 qps: 1720.79 (r/w/o: 1720.79/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 560s ] thds: 16 tps: 1736.31 qps: 1736.31 (r/w/o: 1736.31/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 570s ] thds: 16 tps: 1728.11 qps: 1728.11 (r/w/o: 1728.11/0.00/0.00) lat (ms,95%): 10.46 err/s: 0.00 reconn/s: 0.00
[ 580s ] thds: 16 tps: 1719.39 qps: 1719.39 (r/w/o: 1719.39/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 590s ] thds: 16 tps: 1730.80 qps: 1730.80 (r/w/o: 1730.80/0.00/0.00) lat (ms,95%): 10.46 err/s: 0.00 reconn/s: 0.00
[ 600s ] thds: 16 tps: 1713.33 qps: 1713.33 (r/w/o: 1713.33/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
SQL statistics:
    queries performed:
        read:                            1028516
        write:                           0
        other:                           0
        total:                           1028516
    transactions:                        1028516 (1714.17 per sec.)
    queries:                             1028516 (1714.17 per sec.)
    ignored errors:                      0      (0.00 per sec.)
    reconnects:                          0      (0.00 per sec.)

Throughput:
    events/s (eps):                      1714.1689
    time elapsed:                        600.0085s
    total number of events:              1028516

Latency (ms):
         min:                                    5.11
         avg:                                    9.33
         max:                                  232.14
         95th percentile:                       10.65
         sum:                              9599491.76

Threads fairness:
    events (avg/stddev):           64282.2500/6335.42
    execution time (avg/stddev):   599.9682/0.02
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

[ 10s ] thds: 16 tps: 1552.93 qps: 1552.93 (r/w/o: 0.00/1528.73/24.20) lat (ms,95%): 12.52 err/s: 0.00 reconn/s: 0.00
[ 20s ] thds: 16 tps: 1540.60 qps: 1540.60 (r/w/o: 0.00/1519.40/21.20) lat (ms,95%): 11.45 err/s: 0.00 reconn/s: 0.00
[ 30s ] thds: 16 tps: 1506.80 qps: 1506.80 (r/w/o: 0.00/1486.10/20.70) lat (ms,95%): 12.98 err/s: 0.00 reconn/s: 0.00
[ 40s ] thds: 16 tps: 1555.00 qps: 1555.00 (r/w/o: 0.00/1529.00/26.00) lat (ms,95%): 12.08 err/s: 0.00 reconn/s: 0.00
[ 50s ] thds: 16 tps: 1538.89 qps: 1538.89 (r/w/o: 0.00/1516.29/22.60) lat (ms,95%): 12.52 err/s: 0.00 reconn/s: 0.00
[ 60s ] thds: 16 tps: 1540.01 qps: 1540.01 (r/w/o: 0.00/1518.81/21.20) lat (ms,95%): 12.52 err/s: 0.00 reconn/s: 0.00
[ 70s ] thds: 16 tps: 1501.80 qps: 1501.80 (r/w/o: 0.00/1480.40/21.40) lat (ms,95%): 12.98 err/s: 0.00 reconn/s: 0.00
[ 80s ] thds: 16 tps: 1538.11 qps: 1538.11 (r/w/o: 0.00/1516.11/22.00) lat (ms,95%): 12.52 err/s: 0.00 reconn/s: 0.00
[ 90s ] thds: 16 tps: 1561.80 qps: 1561.80 (r/w/o: 0.00/1538.40/23.40) lat (ms,95%): 11.87 err/s: 0.00 reconn/s: 0.00
[ 100s ] thds: 16 tps: 1539.90 qps: 1539.90 (r/w/o: 0.00/1517.30/22.60) lat (ms,95%): 11.65 err/s: 0.00 reconn/s: 0.00
[ 110s ] thds: 16 tps: 1506.09 qps: 1506.09 (r/w/o: 0.00/1483.89/22.20) lat (ms,95%): 12.98 err/s: 0.00 reconn/s: 0.00
[ 120s ] thds: 16 tps: 1524.11 qps: 1524.11 (r/w/o: 0.00/1504.31/19.80) lat (ms,95%): 12.30 err/s: 0.00 reconn/s: 0.00
[ 130s ] thds: 16 tps: 1537.39 qps: 1537.39 (r/w/o: 0.00/1515.09/22.30) lat (ms,95%): 12.98 err/s: 0.00 reconn/s: 0.00
[ 140s ] thds: 16 tps: 1531.31 qps: 1531.31 (r/w/o: 0.00/1509.91/21.40) lat (ms,95%): 12.52 err/s: 0.00 reconn/s: 0.00
[ 150s ] thds: 16 tps: 1479.90 qps: 1479.90 (r/w/o: 0.00/1458.30/21.60) lat (ms,95%): 13.22 err/s: 0.00 reconn/s: 0.00
[ 160s ] thds: 16 tps: 1497.20 qps: 1497.20 (r/w/o: 0.00/1476.10/21.10) lat (ms,95%): 12.98 err/s: 0.00 reconn/s: 0.00
[ 170s ] thds: 16 tps: 1501.10 qps: 1501.10 (r/w/o: 0.00/1480.70/20.40) lat (ms,95%): 12.75 err/s: 0.00 reconn/s: 0.00
[ 180s ] thds: 16 tps: 1513.70 qps: 1513.70 (r/w/o: 0.00/1488.80/24.90) lat (ms,95%): 12.52 err/s: 0.00 reconn/s: 0.00
[ 190s ] thds: 16 tps: 1542.60 qps: 1542.60 (r/w/o: 0.00/1521.10/21.50) lat (ms,95%): 11.24 err/s: 0.00 reconn/s: 0.00
[ 200s ] thds: 16 tps: 1536.00 qps: 1536.00 (r/w/o: 0.00/1517.00/19.00) lat (ms,95%): 11.65 err/s: 0.00 reconn/s: 0.00
[ 210s ] thds: 16 tps: 1552.80 qps: 1552.80 (r/w/o: 0.00/1532.60/20.20) lat (ms,95%): 11.24 err/s: 0.00 reconn/s: 0.00
[ 220s ] thds: 16 tps: 1513.70 qps: 1513.70 (r/w/o: 0.00/1491.70/22.00) lat (ms,95%): 12.98 err/s: 0.00 reconn/s: 0.00
[ 230s ] thds: 16 tps: 1509.90 qps: 1509.90 (r/w/o: 0.00/1490.50/19.40) lat (ms,95%): 12.75 err/s: 0.00 reconn/s: 0.00
[ 240s ] thds: 16 tps: 1442.70 qps: 1442.70 (r/w/o: 0.00/1421.20/21.50) lat (ms,95%): 13.22 err/s: 0.00 reconn/s: 0.00
[ 250s ] thds: 16 tps: 1588.20 qps: 1588.20 (r/w/o: 0.00/1566.10/22.10) lat (ms,95%): 10.84 err/s: 0.00 reconn/s: 0.00
[ 260s ] thds: 16 tps: 1590.49 qps: 1590.49 (r/w/o: 0.00/1568.39/22.10) lat (ms,95%): 10.46 err/s: 0.00 reconn/s: 0.00
[ 270s ] thds: 16 tps: 1574.61 qps: 1574.61 (r/w/o: 0.00/1554.71/19.90) lat (ms,95%): 10.84 err/s: 0.00 reconn/s: 0.00
[ 280s ] thds: 16 tps: 1552.89 qps: 1552.89 (r/w/o: 0.00/1532.39/20.50) lat (ms,95%): 12.30 err/s: 0.00 reconn/s: 0.00
[ 290s ] thds: 16 tps: 1514.71 qps: 1514.71 (r/w/o: 0.00/1490.91/23.80) lat (ms,95%): 12.75 err/s: 0.00 reconn/s: 0.00
[ 300s ] thds: 16 tps: 1516.90 qps: 1516.90 (r/w/o: 0.00/1497.20/19.70) lat (ms,95%): 12.08 err/s: 0.00 reconn/s: 0.00
[ 310s ] thds: 16 tps: 1538.80 qps: 1538.80 (r/w/o: 0.00/1517.50/21.30) lat (ms,95%): 12.52 err/s: 0.00 reconn/s: 0.00
[ 320s ] thds: 16 tps: 1548.70 qps: 1548.70 (r/w/o: 0.00/1526.60/22.10) lat (ms,95%): 12.30 err/s: 0.00 reconn/s: 0.00
[ 330s ] thds: 16 tps: 1551.90 qps: 1551.90 (r/w/o: 0.00/1530.20/21.70) lat (ms,95%): 12.30 err/s: 0.00 reconn/s: 0.00
[ 340s ] thds: 16 tps: 1550.19 qps: 1550.19 (r/w/o: 0.00/1530.09/20.10) lat (ms,95%): 11.87 err/s: 0.00 reconn/s: 0.00
[ 350s ] thds: 16 tps: 1523.70 qps: 1523.70 (r/w/o: 0.00/1501.70/22.00) lat (ms,95%): 12.75 err/s: 0.00 reconn/s: 0.00
[ 360s ] thds: 16 tps: 1587.09 qps: 1587.09 (r/w/o: 0.00/1564.49/22.60) lat (ms,95%): 12.30 err/s: 0.00 reconn/s: 0.00
[ 370s ] thds: 16 tps: 1591.30 qps: 1591.30 (r/w/o: 0.00/1568.60/22.70) lat (ms,95%): 10.84 err/s: 0.00 reconn/s: 0.00
[ 380s ] thds: 16 tps: 1573.11 qps: 1573.11 (r/w/o: 0.00/1550.61/22.50) lat (ms,95%): 11.24 err/s: 0.00 reconn/s: 0.00
[ 390s ] thds: 16 tps: 1537.30 qps: 1537.30 (r/w/o: 0.00/1517.40/19.90) lat (ms,95%): 12.52 err/s: 0.00 reconn/s: 0.00
[ 400s ] thds: 16 tps: 1533.89 qps: 1533.89 (r/w/o: 0.00/1512.09/21.80) lat (ms,95%): 12.08 err/s: 0.00 reconn/s: 0.00
[ 410s ] thds: 16 tps: 1548.71 qps: 1548.71 (r/w/o: 0.00/1525.21/23.50) lat (ms,95%): 11.45 err/s: 0.00 reconn/s: 0.00
[ 420s ] thds: 16 tps: 1538.20 qps: 1538.20 (r/w/o: 0.00/1516.40/21.80) lat (ms,95%): 12.52 err/s: 0.00 reconn/s: 0.00
[ 430s ] thds: 16 tps: 1523.19 qps: 1523.19 (r/w/o: 0.00/1500.59/22.60) lat (ms,95%): 12.75 err/s: 0.00 reconn/s: 0.00
[ 440s ] thds: 16 tps: 1545.51 qps: 1545.51 (r/w/o: 0.00/1524.81/20.70) lat (ms,95%): 12.52 err/s: 0.00 reconn/s: 0.00
[ 450s ] thds: 16 tps: 1540.50 qps: 1540.50 (r/w/o: 0.00/1517.60/22.90) lat (ms,95%): 12.52 err/s: 0.00 reconn/s: 0.00
[ 460s ] thds: 16 tps: 1560.69 qps: 1560.69 (r/w/o: 0.00/1540.49/20.20) lat (ms,95%): 12.08 err/s: 0.00 reconn/s: 0.00
[ 470s ] thds: 16 tps: 1519.71 qps: 1519.71 (r/w/o: 0.00/1498.81/20.90) lat (ms,95%): 12.52 err/s: 0.00 reconn/s: 0.00
[ 480s ] thds: 16 tps: 1548.29 qps: 1548.29 (r/w/o: 0.00/1528.69/19.60) lat (ms,95%): 12.52 err/s: 0.00 reconn/s: 0.00
[ 490s ] thds: 16 tps: 1549.60 qps: 1549.60 (r/w/o: 0.00/1524.70/24.90) lat (ms,95%): 12.30 err/s: 0.00 reconn/s: 0.00
[ 500s ] thds: 16 tps: 1550.00 qps: 1550.00 (r/w/o: 0.00/1526.60/23.40) lat (ms,95%): 11.04 err/s: 0.00 reconn/s: 0.00
[ 510s ] thds: 16 tps: 1573.00 qps: 1573.00 (r/w/o: 0.00/1552.70/20.30) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 520s ] thds: 16 tps: 1551.09 qps: 1551.09 (r/w/o: 0.00/1527.69/23.40) lat (ms,95%): 11.65 err/s: 0.00 reconn/s: 0.00
[ 530s ] thds: 16 tps: 1535.00 qps: 1535.00 (r/w/o: 0.00/1509.30/25.70) lat (ms,95%): 12.52 err/s: 0.00 reconn/s: 0.00
[ 540s ] thds: 16 tps: 1519.00 qps: 1519.00 (r/w/o: 0.00/1496.50/22.50) lat (ms,95%): 12.30 err/s: 0.00 reconn/s: 0.00
[ 550s ] thds: 16 tps: 1519.60 qps: 1519.60 (r/w/o: 0.00/1499.20/20.40) lat (ms,95%): 12.30 err/s: 0.00 reconn/s: 0.00
[ 560s ] thds: 16 tps: 1557.10 qps: 1557.10 (r/w/o: 0.00/1533.90/23.20) lat (ms,95%): 11.45 err/s: 0.00 reconn/s: 0.00
[ 570s ] thds: 16 tps: 1526.49 qps: 1526.49 (r/w/o: 0.00/1502.19/24.30) lat (ms,95%): 12.75 err/s: 0.00 reconn/s: 0.00
[ 580s ] thds: 16 tps: 1515.71 qps: 1515.71 (r/w/o: 0.00/1490.61/25.10) lat (ms,95%): 12.75 err/s: 0.00 reconn/s: 0.00
[ 590s ] thds: 16 tps: 1550.50 qps: 1550.50 (r/w/o: 0.00/1528.80/21.70) lat (ms,95%): 12.08 err/s: 0.00 reconn/s: 0.00
[ 600s ] thds: 16 tps: 1551.20 qps: 1551.20 (r/w/o: 0.00/1527.60/23.60) lat (ms,95%): 11.24 err/s: 0.00 reconn/s: 0.00
SQL statistics:
    queries performed:
        read:                            0
        write:                           909450
        other:                           13181
        total:                           922631
    transactions:                        922631 (1537.69 per sec.)
    queries:                             922631 (1537.69 per sec.)
    ignored errors:                      0      (0.00 per sec.)
    reconnects:                          0      (0.00 per sec.)

Throughput:
    events/s (eps):                      1537.6895
    time elapsed:                        600.0112s
    total number of events:              922631

Latency (ms):
         min:                                    5.06
         avg:                                   10.40
         max:                                  253.81
         95th percentile:                       12.52
         sum:                              9599609.70

Threads fairness:
    events (avg/stddev):           57664.4375/373.62
    execution time (avg/stddev):   599.9756/0.01
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

[ 10s ] thds: 16 tps: 89.68 qps: 1447.11 (r/w/o: 1266.24/0.00/180.86) lat (ms,95%): 267.41 err/s: 0.00 reconn/s: 0.00
[ 20s ] thds: 16 tps: 100.10 qps: 1601.43 (r/w/o: 1401.13/0.00/200.30) lat (ms,95%): 173.58 err/s: 0.00 reconn/s: 0.00
[ 30s ] thds: 16 tps: 90.70 qps: 1448.61 (r/w/o: 1267.41/0.00/181.20) lat (ms,95%): 196.89 err/s: 0.00 reconn/s: 0.00
[ 40s ] thds: 16 tps: 100.20 qps: 1603.90 (r/w/o: 1403.60/0.00/200.30) lat (ms,95%): 170.48 err/s: 0.00 reconn/s: 0.00
[ 50s ] thds: 16 tps: 98.50 qps: 1578.20 (r/w/o: 1381.00/0.00/197.20) lat (ms,95%): 176.73 err/s: 0.00 reconn/s: 0.00
[ 60s ] thds: 16 tps: 98.10 qps: 1572.30 (r/w/o: 1376.00/0.00/196.30) lat (ms,95%): 176.73 err/s: 0.00 reconn/s: 0.00
[ 70s ] thds: 16 tps: 99.50 qps: 1590.20 (r/w/o: 1391.20/0.00/199.00) lat (ms,95%): 183.21 err/s: 0.00 reconn/s: 0.00
[ 80s ] thds: 16 tps: 97.00 qps: 1551.70 (r/w/o: 1357.70/0.00/194.00) lat (ms,95%): 186.54 err/s: 0.00 reconn/s: 0.00
[ 90s ] thds: 16 tps: 96.20 qps: 1537.70 (r/w/o: 1345.50/0.00/192.20) lat (ms,95%): 183.21 err/s: 0.00 reconn/s: 0.00
[ 100s ] thds: 16 tps: 100.70 qps: 1616.10 (r/w/o: 1414.50/0.00/201.60) lat (ms,95%): 167.44 err/s: 0.00 reconn/s: 0.00
[ 110s ] thds: 16 tps: 101.60 qps: 1623.69 (r/w/o: 1420.69/0.00/203.00) lat (ms,95%): 167.44 err/s: 0.00 reconn/s: 0.00
[ 120s ] thds: 16 tps: 101.30 qps: 1619.31 (r/w/o: 1416.61/0.00/202.70) lat (ms,95%): 167.44 err/s: 0.00 reconn/s: 0.00
[ 130s ] thds: 16 tps: 101.40 qps: 1620.90 (r/w/o: 1418.10/0.00/202.80) lat (ms,95%): 167.44 err/s: 0.00 reconn/s: 0.00
[ 140s ] thds: 16 tps: 102.70 qps: 1644.80 (r/w/o: 1439.40/0.00/205.40) lat (ms,95%): 164.45 err/s: 0.00 reconn/s: 0.00
[ 150s ] thds: 16 tps: 102.50 qps: 1641.00 (r/w/o: 1435.90/0.00/205.10) lat (ms,95%): 167.44 err/s: 0.00 reconn/s: 0.00
[ 160s ] thds: 16 tps: 99.40 qps: 1592.09 (r/w/o: 1393.39/0.00/198.70) lat (ms,95%): 176.73 err/s: 0.00 reconn/s: 0.00
[ 170s ] thds: 16 tps: 96.20 qps: 1535.20 (r/w/o: 1343.00/0.00/192.20) lat (ms,95%): 176.73 err/s: 0.00 reconn/s: 0.00
[ 180s ] thds: 16 tps: 94.10 qps: 1506.99 (r/w/o: 1318.49/0.00/188.50) lat (ms,95%): 240.02 err/s: 0.00 reconn/s: 0.00
[ 190s ] thds: 16 tps: 97.20 qps: 1557.20 (r/w/o: 1362.90/0.00/194.30) lat (ms,95%): 179.94 err/s: 0.00 reconn/s: 0.00
[ 200s ] thds: 16 tps: 103.50 qps: 1654.92 (r/w/o: 1447.92/0.00/207.00) lat (ms,95%): 164.45 err/s: 0.00 reconn/s: 0.00
[ 210s ] thds: 16 tps: 101.40 qps: 1622.59 (r/w/o: 1419.79/0.00/202.80) lat (ms,95%): 167.44 err/s: 0.00 reconn/s: 0.00
[ 220s ] thds: 16 tps: 100.70 qps: 1611.71 (r/w/o: 1410.21/0.00/201.50) lat (ms,95%): 167.44 err/s: 0.00 reconn/s: 0.00
[ 230s ] thds: 16 tps: 101.40 qps: 1620.30 (r/w/o: 1417.50/0.00/202.80) lat (ms,95%): 167.44 err/s: 0.00 reconn/s: 0.00
[ 240s ] thds: 16 tps: 101.60 qps: 1626.80 (r/w/o: 1423.60/0.00/203.20) lat (ms,95%): 167.44 err/s: 0.00 reconn/s: 0.00
[ 250s ] thds: 16 tps: 101.50 qps: 1619.50 (r/w/o: 1417.00/0.00/202.50) lat (ms,95%): 167.44 err/s: 0.00 reconn/s: 0.00
[ 260s ] thds: 16 tps: 100.40 qps: 1613.31 (r/w/o: 1412.21/0.00/201.10) lat (ms,95%): 170.48 err/s: 0.00 reconn/s: 0.00
[ 270s ] thds: 16 tps: 101.50 qps: 1623.40 (r/w/o: 1420.20/0.00/203.20) lat (ms,95%): 170.48 err/s: 0.00 reconn/s: 0.00
[ 280s ] thds: 16 tps: 97.00 qps: 1549.49 (r/w/o: 1355.59/0.00/193.90) lat (ms,95%): 183.21 err/s: 0.00 reconn/s: 0.00
[ 290s ] thds: 16 tps: 101.50 qps: 1623.09 (r/w/o: 1420.09/0.00/203.00) lat (ms,95%): 167.44 err/s: 0.00 reconn/s: 0.00
[ 300s ] thds: 16 tps: 98.20 qps: 1574.01 (r/w/o: 1377.61/0.00/196.40) lat (ms,95%): 170.48 err/s: 0.00 reconn/s: 0.00
[ 310s ] thds: 16 tps: 103.00 qps: 1646.11 (r/w/o: 1440.20/0.00/205.90) lat (ms,95%): 164.45 err/s: 0.00 reconn/s: 0.00
[ 320s ] thds: 16 tps: 100.80 qps: 1612.89 (r/w/o: 1411.30/0.00/201.60) lat (ms,95%): 167.44 err/s: 0.00 reconn/s: 0.00
[ 330s ] thds: 16 tps: 101.30 qps: 1620.40 (r/w/o: 1417.70/0.00/202.70) lat (ms,95%): 170.48 err/s: 0.00 reconn/s: 0.00
[ 340s ] thds: 16 tps: 99.80 qps: 1593.11 (r/w/o: 1393.71/0.00/199.40) lat (ms,95%): 170.48 err/s: 0.00 reconn/s: 0.00
[ 350s ] thds: 16 tps: 98.60 qps: 1584.90 (r/w/o: 1387.40/0.00/197.50) lat (ms,95%): 173.58 err/s: 0.00 reconn/s: 0.00
[ 360s ] thds: 16 tps: 98.50 qps: 1572.79 (r/w/o: 1375.99/0.00/196.80) lat (ms,95%): 176.73 err/s: 0.00 reconn/s: 0.00
[ 370s ] thds: 16 tps: 98.20 qps: 1573.10 (r/w/o: 1376.60/0.00/196.50) lat (ms,95%): 176.73 err/s: 0.00 reconn/s: 0.00
[ 380s ] thds: 16 tps: 102.80 qps: 1643.00 (r/w/o: 1437.50/0.00/205.50) lat (ms,95%): 164.45 err/s: 0.00 reconn/s: 0.00
[ 390s ] thds: 16 tps: 100.20 qps: 1603.90 (r/w/o: 1403.30/0.00/200.60) lat (ms,95%): 170.48 err/s: 0.00 reconn/s: 0.00
[ 400s ] thds: 16 tps: 99.70 qps: 1594.80 (r/w/o: 1395.40/0.00/199.40) lat (ms,95%): 173.58 err/s: 0.00 reconn/s: 0.00
[ 410s ] thds: 16 tps: 99.90 qps: 1595.09 (r/w/o: 1395.29/0.00/199.80) lat (ms,95%): 170.48 err/s: 0.00 reconn/s: 0.00
[ 420s ] thds: 16 tps: 101.70 qps: 1634.11 (r/w/o: 1430.81/0.00/203.30) lat (ms,95%): 167.44 err/s: 0.00 reconn/s: 0.00
[ 430s ] thds: 16 tps: 98.10 qps: 1559.70 (r/w/o: 1363.60/0.00/196.10) lat (ms,95%): 176.73 err/s: 0.00 reconn/s: 0.00
[ 440s ] thds: 16 tps: 94.70 qps: 1521.31 (r/w/o: 1331.81/0.00/189.50) lat (ms,95%): 179.94 err/s: 0.00 reconn/s: 0.00
[ 450s ] thds: 16 tps: 97.00 qps: 1554.69 (r/w/o: 1360.79/0.00/193.90) lat (ms,95%): 176.73 err/s: 0.00 reconn/s: 0.00
[ 460s ] thds: 16 tps: 97.90 qps: 1560.91 (r/w/o: 1365.10/0.00/195.80) lat (ms,95%): 186.54 err/s: 0.00 reconn/s: 0.00
[ 470s ] thds: 16 tps: 100.40 qps: 1610.09 (r/w/o: 1409.19/0.00/200.90) lat (ms,95%): 170.48 err/s: 0.00 reconn/s: 0.00
[ 480s ] thds: 16 tps: 97.50 qps: 1557.50 (r/w/o: 1362.60/0.00/194.90) lat (ms,95%): 176.73 err/s: 0.00 reconn/s: 0.00
[ 490s ] thds: 16 tps: 100.20 qps: 1605.69 (r/w/o: 1405.19/0.00/200.50) lat (ms,95%): 167.44 err/s: 0.00 reconn/s: 0.00
[ 500s ] thds: 16 tps: 100.00 qps: 1597.52 (r/w/o: 1397.52/0.00/200.00) lat (ms,95%): 170.48 err/s: 0.00 reconn/s: 0.00
[ 510s ] thds: 16 tps: 101.80 qps: 1628.49 (r/w/o: 1424.89/0.00/203.60) lat (ms,95%): 167.44 err/s: 0.00 reconn/s: 0.00
[ 520s ] thds: 16 tps: 95.70 qps: 1530.80 (r/w/o: 1339.40/0.00/191.40) lat (ms,95%): 179.94 err/s: 0.00 reconn/s: 0.00
[ 530s ] thds: 16 tps: 98.40 qps: 1575.70 (r/w/o: 1378.90/0.00/196.80) lat (ms,95%): 173.58 err/s: 0.00 reconn/s: 0.00
[ 540s ] thds: 16 tps: 97.80 qps: 1563.21 (r/w/o: 1367.50/0.00/195.70) lat (ms,95%): 176.73 err/s: 0.00 reconn/s: 0.00
[ 550s ] thds: 16 tps: 102.20 qps: 1639.20 (r/w/o: 1434.80/0.00/204.40) lat (ms,95%): 164.45 err/s: 0.00 reconn/s: 0.00
[ 560s ] thds: 16 tps: 95.20 qps: 1524.10 (r/w/o: 1333.70/0.00/190.40) lat (ms,95%): 183.21 err/s: 0.00 reconn/s: 0.00
[ 570s ] thds: 16 tps: 95.90 qps: 1535.60 (r/w/o: 1343.80/0.00/191.80) lat (ms,95%): 176.73 err/s: 0.00 reconn/s: 0.00
[ 580s ] thds: 16 tps: 94.00 qps: 1499.61 (r/w/o: 1311.81/0.00/187.80) lat (ms,95%): 183.21 err/s: 0.00 reconn/s: 0.00
[ 590s ] thds: 16 tps: 98.20 qps: 1571.30 (r/w/o: 1375.00/0.00/196.30) lat (ms,95%): 176.73 err/s: 0.00 reconn/s: 0.00
[ 600s ] thds: 16 tps: 100.10 qps: 1602.49 (r/w/o: 1402.09/0.00/200.40) lat (ms,95%): 170.48 err/s: 0.00 reconn/s: 0.00
SQL statistics:
    queries performed:
        read:                            832580
        write:                           0
        other:                           118940
        total:                           951520
    transactions:                        59470  (99.09 per sec.)
    queries:                             951520 (1585.47 per sec.)
    ignored errors:                      0      (0.00 per sec.)
    reconnects:                          0      (0.00 per sec.)

Throughput:
    events/s (eps):                      99.0921
    time elapsed:                        600.1487s
    total number of events:              59470

Latency (ms):
         min:                                  138.66
         avg:                                  161.44
         max:                                  492.35
         95th percentile:                      176.73
         sum:                              9601029.08

Threads fairness:
    events (avg/stddev):           3716.8750/40.19
    execution time (avg/stddev):   600.0643/0.05
```