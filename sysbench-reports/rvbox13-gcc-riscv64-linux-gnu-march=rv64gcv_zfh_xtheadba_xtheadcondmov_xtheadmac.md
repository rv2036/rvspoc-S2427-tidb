# RVBox13 gcc-riscv64-linux-gnu 编译器（-march=rv64gcv_zfh_xtheadba_xtheadcondmov_xtheadmac）
## 编译
```shell
$ CGO_CFLAGS=-march=rv64gcv_zfh_xtheadba_xtheadcondmov_xtheadmac GOOS=linux GOARCH=riscv64 CC=riscv64-l
inux-gnu-gcc make server
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

[ 10s ] thds: 16 tps: 1634.01 qps: 1634.01 (r/w/o: 1634.01/0.00/0.00) lat (ms,95%): 11.65 err/s: 0.00 reconn/s: 0.00
[ 20s ] thds: 16 tps: 1683.60 qps: 1683.60 (r/w/o: 1683.60/0.00/0.00) lat (ms,95%): 11.24 err/s: 0.00 reconn/s: 0.00
[ 30s ] thds: 16 tps: 1705.51 qps: 1705.51 (r/w/o: 1705.51/0.00/0.00) lat (ms,95%): 10.84 err/s: 0.00 reconn/s: 0.00
[ 40s ] thds: 16 tps: 1658.80 qps: 1658.80 (r/w/o: 1658.80/0.00/0.00) lat (ms,95%): 11.87 err/s: 0.00 reconn/s: 0.00
[ 50s ] thds: 16 tps: 1736.21 qps: 1736.21 (r/w/o: 1736.21/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 60s ] thds: 16 tps: 1773.00 qps: 1773.00 (r/w/o: 1773.00/0.00/0.00) lat (ms,95%): 10.84 err/s: 0.00 reconn/s: 0.00
[ 70s ] thds: 16 tps: 1750.90 qps: 1750.90 (r/w/o: 1750.90/0.00/0.00) lat (ms,95%): 10.84 err/s: 0.00 reconn/s: 0.00
[ 80s ] thds: 16 tps: 1698.49 qps: 1698.49 (r/w/o: 1698.49/0.00/0.00) lat (ms,95%): 11.24 err/s: 0.00 reconn/s: 0.00
[ 90s ] thds: 16 tps: 1663.62 qps: 1663.62 (r/w/o: 1663.62/0.00/0.00) lat (ms,95%): 11.65 err/s: 0.00 reconn/s: 0.00
[ 100s ] thds: 16 tps: 1679.90 qps: 1679.90 (r/w/o: 1679.90/0.00/0.00) lat (ms,95%): 11.65 err/s: 0.00 reconn/s: 0.00
[ 110s ] thds: 16 tps: 1675.40 qps: 1675.40 (r/w/o: 1675.40/0.00/0.00) lat (ms,95%): 11.65 err/s: 0.00 reconn/s: 0.00
[ 120s ] thds: 16 tps: 1721.70 qps: 1721.70 (r/w/o: 1721.70/0.00/0.00) lat (ms,95%): 10.46 err/s: 0.00 reconn/s: 0.00
[ 130s ] thds: 16 tps: 1715.80 qps: 1715.80 (r/w/o: 1715.80/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 140s ] thds: 16 tps: 1758.10 qps: 1758.10 (r/w/o: 1758.10/0.00/0.00) lat (ms,95%): 10.46 err/s: 0.00 reconn/s: 0.00
[ 150s ] thds: 16 tps: 1746.20 qps: 1746.20 (r/w/o: 1746.20/0.00/0.00) lat (ms,95%): 10.46 err/s: 0.00 reconn/s: 0.00
[ 160s ] thds: 16 tps: 1725.40 qps: 1725.40 (r/w/o: 1725.40/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 170s ] thds: 16 tps: 1754.49 qps: 1754.49 (r/w/o: 1754.49/0.00/0.00) lat (ms,95%): 10.46 err/s: 0.00 reconn/s: 0.00
[ 180s ] thds: 16 tps: 1768.51 qps: 1768.51 (r/w/o: 1768.51/0.00/0.00) lat (ms,95%): 10.46 err/s: 0.00 reconn/s: 0.00
[ 190s ] thds: 16 tps: 1719.80 qps: 1719.80 (r/w/o: 1719.80/0.00/0.00) lat (ms,95%): 10.46 err/s: 0.00 reconn/s: 0.00
[ 200s ] thds: 16 tps: 1733.49 qps: 1733.49 (r/w/o: 1733.49/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 210s ] thds: 16 tps: 1711.71 qps: 1711.71 (r/w/o: 1711.71/0.00/0.00) lat (ms,95%): 10.46 err/s: 0.00 reconn/s: 0.00
[ 220s ] thds: 16 tps: 1735.00 qps: 1735.00 (r/w/o: 1735.00/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 230s ] thds: 16 tps: 1731.30 qps: 1731.30 (r/w/o: 1731.30/0.00/0.00) lat (ms,95%): 10.46 err/s: 0.00 reconn/s: 0.00
[ 240s ] thds: 16 tps: 1745.90 qps: 1745.90 (r/w/o: 1745.90/0.00/0.00) lat (ms,95%): 10.46 err/s: 0.00 reconn/s: 0.00
[ 250s ] thds: 16 tps: 1737.31 qps: 1737.31 (r/w/o: 1737.31/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 260s ] thds: 16 tps: 1735.30 qps: 1735.30 (r/w/o: 1735.30/0.00/0.00) lat (ms,95%): 10.46 err/s: 0.00 reconn/s: 0.00
[ 270s ] thds: 16 tps: 1729.50 qps: 1729.50 (r/w/o: 1729.50/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 280s ] thds: 16 tps: 1732.50 qps: 1732.50 (r/w/o: 1732.50/0.00/0.00) lat (ms,95%): 10.84 err/s: 0.00 reconn/s: 0.00
[ 290s ] thds: 16 tps: 1719.80 qps: 1719.80 (r/w/o: 1719.80/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 300s ] thds: 16 tps: 1743.00 qps: 1743.00 (r/w/o: 1743.00/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 310s ] thds: 16 tps: 1732.41 qps: 1732.41 (r/w/o: 1732.41/0.00/0.00) lat (ms,95%): 10.46 err/s: 0.00 reconn/s: 0.00
[ 320s ] thds: 16 tps: 1731.70 qps: 1731.70 (r/w/o: 1731.70/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 330s ] thds: 16 tps: 1763.58 qps: 1763.58 (r/w/o: 1763.58/0.00/0.00) lat (ms,95%): 10.46 err/s: 0.00 reconn/s: 0.00
[ 340s ] thds: 16 tps: 1753.82 qps: 1753.82 (r/w/o: 1753.82/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 350s ] thds: 16 tps: 1741.89 qps: 1741.89 (r/w/o: 1741.89/0.00/0.00) lat (ms,95%): 10.46 err/s: 0.00 reconn/s: 0.00
[ 360s ] thds: 16 tps: 1758.71 qps: 1758.71 (r/w/o: 1758.71/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 370s ] thds: 16 tps: 1728.39 qps: 1728.39 (r/w/o: 1728.39/0.00/0.00) lat (ms,95%): 10.46 err/s: 0.00 reconn/s: 0.00
[ 380s ] thds: 16 tps: 1725.00 qps: 1725.00 (r/w/o: 1725.00/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 390s ] thds: 16 tps: 1731.71 qps: 1731.71 (r/w/o: 1731.71/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 400s ] thds: 16 tps: 1727.70 qps: 1727.70 (r/w/o: 1727.70/0.00/0.00) lat (ms,95%): 10.84 err/s: 0.00 reconn/s: 0.00
[ 410s ] thds: 16 tps: 1717.29 qps: 1717.29 (r/w/o: 1717.29/0.00/0.00) lat (ms,95%): 10.46 err/s: 0.00 reconn/s: 0.00
[ 420s ] thds: 16 tps: 1724.21 qps: 1724.21 (r/w/o: 1724.21/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 430s ] thds: 16 tps: 1720.30 qps: 1720.30 (r/w/o: 1720.30/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 440s ] thds: 16 tps: 1735.39 qps: 1735.39 (r/w/o: 1735.39/0.00/0.00) lat (ms,95%): 10.46 err/s: 0.00 reconn/s: 0.00
[ 450s ] thds: 16 tps: 1736.41 qps: 1736.41 (r/w/o: 1736.41/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 460s ] thds: 16 tps: 1704.90 qps: 1704.90 (r/w/o: 1704.90/0.00/0.00) lat (ms,95%): 11.04 err/s: 0.00 reconn/s: 0.00
[ 470s ] thds: 16 tps: 1717.40 qps: 1717.40 (r/w/o: 1717.40/0.00/0.00) lat (ms,95%): 11.04 err/s: 0.00 reconn/s: 0.00
[ 480s ] thds: 16 tps: 1722.60 qps: 1722.60 (r/w/o: 1722.60/0.00/0.00) lat (ms,95%): 10.46 err/s: 0.00 reconn/s: 0.00
[ 490s ] thds: 16 tps: 1751.30 qps: 1751.30 (r/w/o: 1751.30/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 500s ] thds: 16 tps: 1732.68 qps: 1732.68 (r/w/o: 1732.68/0.00/0.00) lat (ms,95%): 10.46 err/s: 0.00 reconn/s: 0.00
[ 510s ] thds: 16 tps: 1736.31 qps: 1736.31 (r/w/o: 1736.31/0.00/0.00) lat (ms,95%): 10.46 err/s: 0.00 reconn/s: 0.00
[ 520s ] thds: 16 tps: 1749.70 qps: 1749.70 (r/w/o: 1749.70/0.00/0.00) lat (ms,95%): 11.04 err/s: 0.00 reconn/s: 0.00
[ 530s ] thds: 16 tps: 1727.90 qps: 1727.90 (r/w/o: 1727.90/0.00/0.00) lat (ms,95%): 10.84 err/s: 0.00 reconn/s: 0.00
[ 540s ] thds: 16 tps: 1719.70 qps: 1719.70 (r/w/o: 1719.70/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 550s ] thds: 16 tps: 1721.91 qps: 1721.91 (r/w/o: 1721.91/0.00/0.00) lat (ms,95%): 10.46 err/s: 0.00 reconn/s: 0.00
[ 560s ] thds: 16 tps: 1733.30 qps: 1733.30 (r/w/o: 1733.30/0.00/0.00) lat (ms,95%): 10.46 err/s: 0.00 reconn/s: 0.00
[ 570s ] thds: 16 tps: 1745.39 qps: 1745.39 (r/w/o: 1745.39/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 580s ] thds: 16 tps: 1834.20 qps: 1834.20 (r/w/o: 1834.20/0.00/0.00) lat (ms,95%): 10.46 err/s: 0.00 reconn/s: 0.00
[ 590s ] thds: 16 tps: 1776.00 qps: 1776.00 (r/w/o: 1776.00/0.00/0.00) lat (ms,95%): 10.46 err/s: 0.00 reconn/s: 0.00
[ 600s ] thds: 16 tps: 1737.40 qps: 1737.40 (r/w/o: 1737.40/0.00/0.00) lat (ms,95%): 10.46 err/s: 0.00 reconn/s: 0.00
SQL statistics:
    queries performed:
        read:                            1037653
        write:                           0
        other:                           0
        total:                           1037653
    transactions:                        1037653 (1729.39 per sec.)
    queries:                             1037653 (1729.39 per sec.)
    ignored errors:                      0      (0.00 per sec.)
    reconnects:                          0      (0.00 per sec.)

Throughput:
    events/s (eps):                      1729.3882
    time elapsed:                        600.0116s
    total number of events:              1037653

Latency (ms):
         min:                                    5.30
         avg:                                    9.25
         max:                                   60.33
         95th percentile:                       10.84
         sum:                              9599530.92

Threads fairness:
    events (avg/stddev):           64853.3125/5644.24
    execution time (avg/stddev):   599.9707/0.02
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

[ 10s ] thds: 16 tps: 1489.04 qps: 1489.04 (r/w/o: 0.00/1466.14/22.90) lat (ms,95%): 12.98 err/s: 0.00 reconn/s: 0.00
[ 20s ] thds: 16 tps: 1497.51 qps: 1497.51 (r/w/o: 0.00/1477.91/19.60) lat (ms,95%): 12.98 err/s: 0.00 reconn/s: 0.00
[ 30s ] thds: 16 tps: 1513.39 qps: 1513.39 (r/w/o: 0.00/1491.59/21.80) lat (ms,95%): 12.52 err/s: 0.00 reconn/s: 0.00
[ 40s ] thds: 16 tps: 1530.19 qps: 1530.19 (r/w/o: 0.00/1503.29/26.90) lat (ms,95%): 12.52 err/s: 0.00 reconn/s: 0.00
[ 50s ] thds: 16 tps: 1530.01 qps: 1530.01 (r/w/o: 0.00/1507.81/22.20) lat (ms,95%): 12.75 err/s: 0.00 reconn/s: 0.00
[ 60s ] thds: 16 tps: 1511.00 qps: 1511.00 (r/w/o: 0.00/1488.40/22.60) lat (ms,95%): 12.98 err/s: 0.00 reconn/s: 0.00
[ 70s ] thds: 16 tps: 1531.31 qps: 1531.31 (r/w/o: 0.00/1509.31/22.00) lat (ms,95%): 12.52 err/s: 0.00 reconn/s: 0.00
[ 80s ] thds: 16 tps: 1523.30 qps: 1523.30 (r/w/o: 0.00/1504.00/19.30) lat (ms,95%): 12.52 err/s: 0.00 reconn/s: 0.00
[ 90s ] thds: 16 tps: 1513.69 qps: 1513.69 (r/w/o: 0.00/1488.79/24.90) lat (ms,95%): 12.08 err/s: 0.00 reconn/s: 0.00
[ 100s ] thds: 16 tps: 1541.61 qps: 1541.61 (r/w/o: 0.00/1517.31/24.30) lat (ms,95%): 12.30 err/s: 0.00 reconn/s: 0.00
[ 110s ] thds: 16 tps: 1521.10 qps: 1521.10 (r/w/o: 0.00/1498.80/22.30) lat (ms,95%): 12.75 err/s: 0.00 reconn/s: 0.00
[ 120s ] thds: 16 tps: 1474.60 qps: 1474.60 (r/w/o: 0.00/1452.70/21.90) lat (ms,95%): 13.22 err/s: 0.00 reconn/s: 0.00
[ 130s ] thds: 16 tps: 1491.81 qps: 1491.81 (r/w/o: 0.00/1469.11/22.70) lat (ms,95%): 13.22 err/s: 0.00 reconn/s: 0.00
[ 140s ] thds: 16 tps: 1580.79 qps: 1580.79 (r/w/o: 0.00/1557.39/23.40) lat (ms,95%): 10.84 err/s: 0.00 reconn/s: 0.00
[ 150s ] thds: 16 tps: 1545.20 qps: 1545.20 (r/w/o: 0.00/1523.40/21.80) lat (ms,95%): 12.08 err/s: 0.00 reconn/s: 0.00
[ 160s ] thds: 16 tps: 1553.00 qps: 1553.00 (r/w/o: 0.00/1530.70/22.30) lat (ms,95%): 11.45 err/s: 0.00 reconn/s: 0.00
[ 170s ] thds: 16 tps: 1561.01 qps: 1561.01 (r/w/o: 0.00/1541.21/19.80) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 180s ] thds: 16 tps: 1500.70 qps: 1500.70 (r/w/o: 0.00/1479.30/21.40) lat (ms,95%): 12.98 err/s: 0.00 reconn/s: 0.00
[ 190s ] thds: 16 tps: 1531.30 qps: 1531.30 (r/w/o: 0.00/1512.90/18.40) lat (ms,95%): 12.52 err/s: 0.00 reconn/s: 0.00
[ 200s ] thds: 16 tps: 1548.90 qps: 1548.90 (r/w/o: 0.00/1527.20/21.70) lat (ms,95%): 12.30 err/s: 0.00 reconn/s: 0.00
[ 210s ] thds: 16 tps: 1589.31 qps: 1589.31 (r/w/o: 0.00/1569.51/19.80) lat (ms,95%): 11.04 err/s: 0.00 reconn/s: 0.00
[ 220s ] thds: 16 tps: 1583.79 qps: 1583.79 (r/w/o: 0.00/1558.09/25.70) lat (ms,95%): 12.08 err/s: 0.00 reconn/s: 0.00
[ 230s ] thds: 16 tps: 1543.90 qps: 1543.90 (r/w/o: 0.00/1523.00/20.90) lat (ms,95%): 12.52 err/s: 0.00 reconn/s: 0.00
[ 240s ] thds: 16 tps: 1513.09 qps: 1513.09 (r/w/o: 0.00/1492.09/21.00) lat (ms,95%): 12.75 err/s: 0.00 reconn/s: 0.00
[ 250s ] thds: 16 tps: 1535.11 qps: 1535.11 (r/w/o: 0.00/1514.71/20.40) lat (ms,95%): 12.52 err/s: 0.00 reconn/s: 0.00
[ 260s ] thds: 16 tps: 1528.40 qps: 1528.40 (r/w/o: 0.00/1507.50/20.90) lat (ms,95%): 12.08 err/s: 0.00 reconn/s: 0.00
[ 270s ] thds: 16 tps: 1546.80 qps: 1546.80 (r/w/o: 0.00/1524.30/22.50) lat (ms,95%): 12.30 err/s: 0.00 reconn/s: 0.00
[ 280s ] thds: 16 tps: 1525.09 qps: 1525.09 (r/w/o: 0.00/1505.09/20.00) lat (ms,95%): 12.75 err/s: 0.00 reconn/s: 0.00
[ 290s ] thds: 16 tps: 1399.80 qps: 1399.80 (r/w/o: 0.00/1380.80/19.00) lat (ms,95%): 13.22 err/s: 0.00 reconn/s: 0.00
[ 300s ] thds: 16 tps: 1478.70 qps: 1478.70 (r/w/o: 0.00/1458.50/20.20) lat (ms,95%): 12.98 err/s: 0.00 reconn/s: 0.00
[ 310s ] thds: 16 tps: 1541.81 qps: 1541.81 (r/w/o: 0.00/1521.01/20.80) lat (ms,95%): 11.24 err/s: 0.00 reconn/s: 0.00
[ 320s ] thds: 16 tps: 1514.40 qps: 1514.40 (r/w/o: 0.00/1493.00/21.40) lat (ms,95%): 12.30 err/s: 0.00 reconn/s: 0.00
[ 330s ] thds: 16 tps: 1522.68 qps: 1522.68 (r/w/o: 0.00/1501.08/21.60) lat (ms,95%): 12.52 err/s: 0.00 reconn/s: 0.00
[ 340s ] thds: 16 tps: 1521.41 qps: 1521.41 (r/w/o: 0.00/1496.51/24.90) lat (ms,95%): 12.08 err/s: 0.00 reconn/s: 0.00
[ 350s ] thds: 16 tps: 1531.59 qps: 1531.59 (r/w/o: 0.00/1507.59/24.00) lat (ms,95%): 12.30 err/s: 0.00 reconn/s: 0.00
[ 360s ] thds: 16 tps: 1485.50 qps: 1485.50 (r/w/o: 0.00/1462.50/23.00) lat (ms,95%): 12.98 err/s: 0.00 reconn/s: 0.00
[ 370s ] thds: 16 tps: 1588.20 qps: 1588.20 (r/w/o: 0.00/1565.00/23.20) lat (ms,95%): 10.84 err/s: 0.00 reconn/s: 0.00
[ 380s ] thds: 16 tps: 1596.00 qps: 1596.00 (r/w/o: 0.00/1573.70/22.30) lat (ms,95%): 10.46 err/s: 0.00 reconn/s: 0.00
[ 390s ] thds: 16 tps: 1563.40 qps: 1563.40 (r/w/o: 0.00/1539.70/23.70) lat (ms,95%): 12.30 err/s: 0.00 reconn/s: 0.00
[ 400s ] thds: 16 tps: 1545.10 qps: 1545.10 (r/w/o: 0.00/1524.80/20.30) lat (ms,95%): 11.04 err/s: 0.00 reconn/s: 0.00
[ 410s ] thds: 16 tps: 1548.60 qps: 1548.60 (r/w/o: 0.00/1526.90/21.70) lat (ms,95%): 10.84 err/s: 0.00 reconn/s: 0.00
[ 420s ] thds: 16 tps: 1483.10 qps: 1483.10 (r/w/o: 0.00/1463.40/19.70) lat (ms,95%): 12.98 err/s: 0.00 reconn/s: 0.00
[ 430s ] thds: 16 tps: 1528.50 qps: 1528.50 (r/w/o: 0.00/1506.10/22.40) lat (ms,95%): 12.75 err/s: 0.00 reconn/s: 0.00
[ 440s ] thds: 16 tps: 1535.10 qps: 1535.10 (r/w/o: 0.00/1511.70/23.40) lat (ms,95%): 12.52 err/s: 0.00 reconn/s: 0.00
[ 450s ] thds: 16 tps: 1514.79 qps: 1514.79 (r/w/o: 0.00/1494.19/20.60) lat (ms,95%): 12.75 err/s: 0.00 reconn/s: 0.00
[ 460s ] thds: 16 tps: 1530.91 qps: 1530.91 (r/w/o: 0.00/1511.61/19.30) lat (ms,95%): 12.75 err/s: 0.00 reconn/s: 0.00
[ 470s ] thds: 16 tps: 1538.20 qps: 1538.20 (r/w/o: 0.00/1514.90/23.30) lat (ms,95%): 12.52 err/s: 0.00 reconn/s: 0.00
[ 480s ] thds: 16 tps: 1523.79 qps: 1523.79 (r/w/o: 0.00/1502.99/20.80) lat (ms,95%): 12.52 err/s: 0.00 reconn/s: 0.00
[ 490s ] thds: 16 tps: 1554.11 qps: 1554.11 (r/w/o: 0.00/1532.81/21.30) lat (ms,95%): 12.08 err/s: 0.00 reconn/s: 0.00
[ 500s ] thds: 16 tps: 1482.30 qps: 1482.30 (r/w/o: 0.00/1462.40/19.90) lat (ms,95%): 12.75 err/s: 0.00 reconn/s: 0.00
[ 510s ] thds: 16 tps: 1541.10 qps: 1541.10 (r/w/o: 0.00/1519.80/21.30) lat (ms,95%): 12.75 err/s: 0.00 reconn/s: 0.00
[ 520s ] thds: 16 tps: 1570.70 qps: 1570.70 (r/w/o: 0.00/1549.40/21.30) lat (ms,95%): 11.65 err/s: 0.00 reconn/s: 0.00
[ 530s ] thds: 16 tps: 1543.20 qps: 1543.20 (r/w/o: 0.00/1524.10/19.10) lat (ms,95%): 12.52 err/s: 0.00 reconn/s: 0.00
[ 540s ] thds: 16 tps: 1481.49 qps: 1481.49 (r/w/o: 0.00/1460.89/20.60) lat (ms,95%): 12.98 err/s: 0.00 reconn/s: 0.00
[ 550s ] thds: 16 tps: 1549.00 qps: 1549.00 (r/w/o: 0.00/1526.40/22.60) lat (ms,95%): 12.52 err/s: 0.00 reconn/s: 0.00
[ 560s ] thds: 16 tps: 1538.61 qps: 1538.61 (r/w/o: 0.00/1517.41/21.20) lat (ms,95%): 12.75 err/s: 0.00 reconn/s: 0.00
[ 570s ] thds: 16 tps: 1580.00 qps: 1580.00 (r/w/o: 0.00/1557.30/22.70) lat (ms,95%): 12.30 err/s: 0.00 reconn/s: 0.00
[ 580s ] thds: 16 tps: 1572.60 qps: 1572.60 (r/w/o: 0.00/1548.50/24.10) lat (ms,95%): 10.84 err/s: 0.00 reconn/s: 0.00
[ 590s ] thds: 16 tps: 1567.11 qps: 1567.11 (r/w/o: 0.00/1544.21/22.90) lat (ms,95%): 12.08 err/s: 0.00 reconn/s: 0.00
[ 600s ] thds: 16 tps: 1523.60 qps: 1523.60 (r/w/o: 0.00/1502.10/21.50) lat (ms,95%): 12.75 err/s: 0.00 reconn/s: 0.00
SQL statistics:
    queries performed:
        read:                            0
        write:                           905446
        other:                           13076
        total:                           918522
    transactions:                        918522 (1530.84 per sec.)
    queries:                             918522 (1530.84 per sec.)
    ignored errors:                      0      (0.00 per sec.)
    reconnects:                          0      (0.00 per sec.)

Throughput:
    events/s (eps):                      1530.8406
    time elapsed:                        600.0115s
    total number of events:              918522

Latency (ms):
         min:                                    5.14
         avg:                                   10.45
         max:                                  152.03
         95th percentile:                       12.52
         sum:                              9599587.03

Threads fairness:
    events (avg/stddev):           57407.6250/373.74
    execution time (avg/stddev):   599.9742/0.01
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

[ 10s ] thds: 16 tps: 90.58 qps: 1464.30 (r/w/o: 1281.54/0.00/182.76) lat (ms,95%): 204.11 err/s: 0.00 reconn/s: 0.00
[ 20s ] thds: 16 tps: 83.80 qps: 1340.44 (r/w/o: 1172.84/0.00/167.61) lat (ms,95%): 253.35 err/s: 0.00 reconn/s: 0.00
[ 30s ] thds: 16 tps: 75.80 qps: 1214.69 (r/w/o: 1063.19/0.00/151.50) lat (ms,95%): 320.17 err/s: 0.00 reconn/s: 0.00
[ 40s ] thds: 16 tps: 86.90 qps: 1388.11 (r/w/o: 1214.21/0.00/173.90) lat (ms,95%): 227.40 err/s: 0.00 reconn/s: 0.00
[ 50s ] thds: 16 tps: 93.40 qps: 1493.90 (r/w/o: 1307.10/0.00/186.80) lat (ms,95%): 219.36 err/s: 0.00 reconn/s: 0.00
[ 60s ] thds: 16 tps: 99.50 qps: 1590.87 (r/w/o: 1392.08/0.00/198.80) lat (ms,95%): 173.58 err/s: 0.00 reconn/s: 0.00
[ 70s ] thds: 16 tps: 98.80 qps: 1579.53 (r/w/o: 1381.93/0.00/197.60) lat (ms,95%): 170.48 err/s: 0.00 reconn/s: 0.00
[ 80s ] thds: 16 tps: 96.60 qps: 1546.60 (r/w/o: 1353.40/0.00/193.20) lat (ms,95%): 211.60 err/s: 0.00 reconn/s: 0.00
[ 90s ] thds: 16 tps: 97.10 qps: 1557.09 (r/w/o: 1362.69/0.00/194.40) lat (ms,95%): 173.58 err/s: 0.00 reconn/s: 0.00
[ 100s ] thds: 16 tps: 97.30 qps: 1553.11 (r/w/o: 1358.61/0.00/194.50) lat (ms,95%): 183.21 err/s: 0.00 reconn/s: 0.00
[ 110s ] thds: 16 tps: 100.10 qps: 1602.20 (r/w/o: 1402.00/0.00/200.20) lat (ms,95%): 170.48 err/s: 0.00 reconn/s: 0.00
[ 120s ] thds: 16 tps: 103.30 qps: 1654.50 (r/w/o: 1447.80/0.00/206.70) lat (ms,95%): 164.45 err/s: 0.00 reconn/s: 0.00
[ 130s ] thds: 16 tps: 100.20 qps: 1603.70 (r/w/o: 1403.30/0.00/200.40) lat (ms,95%): 170.48 err/s: 0.00 reconn/s: 0.00
[ 140s ] thds: 16 tps: 98.30 qps: 1572.80 (r/w/o: 1376.20/0.00/196.60) lat (ms,95%): 176.73 err/s: 0.00 reconn/s: 0.00
[ 150s ] thds: 16 tps: 102.60 qps: 1637.80 (r/w/o: 1432.70/0.00/205.10) lat (ms,95%): 164.45 err/s: 0.00 reconn/s: 0.00
[ 160s ] thds: 16 tps: 99.10 qps: 1587.20 (r/w/o: 1389.00/0.00/198.20) lat (ms,95%): 173.58 err/s: 0.00 reconn/s: 0.00
[ 170s ] thds: 16 tps: 98.20 qps: 1573.99 (r/w/o: 1377.50/0.00/196.50) lat (ms,95%): 173.58 err/s: 0.00 reconn/s: 0.00
[ 180s ] thds: 16 tps: 101.40 qps: 1620.61 (r/w/o: 1417.81/0.00/202.80) lat (ms,95%): 167.44 err/s: 0.00 reconn/s: 0.00
[ 190s ] thds: 16 tps: 101.10 qps: 1619.00 (r/w/o: 1416.90/0.00/202.10) lat (ms,95%): 170.48 err/s: 0.00 reconn/s: 0.00
[ 200s ] thds: 16 tps: 101.00 qps: 1611.60 (r/w/o: 1409.60/0.00/202.00) lat (ms,95%): 170.48 err/s: 0.00 reconn/s: 0.00
[ 210s ] thds: 16 tps: 101.30 qps: 1623.60 (r/w/o: 1420.90/0.00/202.70) lat (ms,95%): 167.44 err/s: 0.00 reconn/s: 0.00
[ 220s ] thds: 16 tps: 95.90 qps: 1534.18 (r/w/o: 1342.39/0.00/191.80) lat (ms,95%): 211.60 err/s: 0.00 reconn/s: 0.00
[ 230s ] thds: 16 tps: 95.90 qps: 1535.20 (r/w/o: 1343.60/0.00/191.60) lat (ms,95%): 173.58 err/s: 0.00 reconn/s: 0.00
[ 240s ] thds: 16 tps: 101.10 qps: 1617.52 (r/w/o: 1415.22/0.00/202.30) lat (ms,95%): 170.48 err/s: 0.00 reconn/s: 0.00
[ 250s ] thds: 16 tps: 99.10 qps: 1582.79 (r/w/o: 1384.49/0.00/198.30) lat (ms,95%): 176.73 err/s: 0.00 reconn/s: 0.00
[ 260s ] thds: 16 tps: 101.80 qps: 1629.80 (r/w/o: 1426.20/0.00/203.60) lat (ms,95%): 164.45 err/s: 0.00 reconn/s: 0.00
[ 270s ] thds: 16 tps: 102.20 qps: 1638.10 (r/w/o: 1433.70/0.00/204.40) lat (ms,95%): 167.44 err/s: 0.00 reconn/s: 0.00
[ 280s ] thds: 16 tps: 100.70 qps: 1609.11 (r/w/o: 1407.71/0.00/201.40) lat (ms,95%): 167.44 err/s: 0.00 reconn/s: 0.00
[ 290s ] thds: 16 tps: 101.70 qps: 1626.80 (r/w/o: 1423.70/0.00/203.10) lat (ms,95%): 167.44 err/s: 0.00 reconn/s: 0.00
[ 300s ] thds: 16 tps: 98.80 qps: 1584.28 (r/w/o: 1386.39/0.00/197.90) lat (ms,95%): 170.48 err/s: 0.00 reconn/s: 0.00
[ 310s ] thds: 16 tps: 99.70 qps: 1593.02 (r/w/o: 1393.71/0.00/199.30) lat (ms,95%): 173.58 err/s: 0.00 reconn/s: 0.00
[ 320s ] thds: 16 tps: 101.90 qps: 1629.30 (r/w/o: 1425.50/0.00/203.80) lat (ms,95%): 167.44 err/s: 0.00 reconn/s: 0.00
[ 330s ] thds: 16 tps: 99.30 qps: 1588.39 (r/w/o: 1389.89/0.00/198.50) lat (ms,95%): 170.48 err/s: 0.00 reconn/s: 0.00
[ 340s ] thds: 16 tps: 96.70 qps: 1546.10 (r/w/o: 1352.80/0.00/193.30) lat (ms,95%): 173.58 err/s: 0.00 reconn/s: 0.00
[ 350s ] thds: 16 tps: 101.50 qps: 1625.51 (r/w/o: 1422.20/0.00/203.30) lat (ms,95%): 167.44 err/s: 0.00 reconn/s: 0.00
[ 360s ] thds: 16 tps: 100.20 qps: 1605.60 (r/w/o: 1405.20/0.00/200.40) lat (ms,95%): 176.73 err/s: 0.00 reconn/s: 0.00
[ 370s ] thds: 16 tps: 102.50 qps: 1637.30 (r/w/o: 1432.30/0.00/205.00) lat (ms,95%): 164.45 err/s: 0.00 reconn/s: 0.00
[ 380s ] thds: 16 tps: 99.40 qps: 1589.10 (r/w/o: 1390.40/0.00/198.70) lat (ms,95%): 173.58 err/s: 0.00 reconn/s: 0.00
[ 390s ] thds: 16 tps: 101.60 qps: 1626.30 (r/w/o: 1423.00/0.00/203.30) lat (ms,95%): 167.44 err/s: 0.00 reconn/s: 0.00
[ 400s ] thds: 16 tps: 95.40 qps: 1528.30 (r/w/o: 1337.70/0.00/190.60) lat (ms,95%): 193.38 err/s: 0.00 reconn/s: 0.00
[ 410s ] thds: 16 tps: 94.70 qps: 1514.90 (r/w/o: 1325.40/0.00/189.50) lat (ms,95%): 179.94 err/s: 0.00 reconn/s: 0.00
[ 420s ] thds: 16 tps: 94.60 qps: 1510.60 (r/w/o: 1321.40/0.00/189.20) lat (ms,95%): 211.60 err/s: 0.00 reconn/s: 0.00
[ 430s ] thds: 16 tps: 93.90 qps: 1504.70 (r/w/o: 1316.80/0.00/187.90) lat (ms,95%): 219.36 err/s: 0.00 reconn/s: 0.00
[ 440s ] thds: 16 tps: 95.40 qps: 1527.20 (r/w/o: 1336.70/0.00/190.50) lat (ms,95%): 186.54 err/s: 0.00 reconn/s: 0.00
[ 450s ] thds: 16 tps: 98.20 qps: 1568.30 (r/w/o: 1371.60/0.00/196.70) lat (ms,95%): 179.94 err/s: 0.00 reconn/s: 0.00
[ 460s ] thds: 16 tps: 96.60 qps: 1545.71 (r/w/o: 1352.51/0.00/193.20) lat (ms,95%): 183.21 err/s: 0.00 reconn/s: 0.00
[ 470s ] thds: 16 tps: 93.90 qps: 1503.59 (r/w/o: 1315.89/0.00/187.70) lat (ms,95%): 227.40 err/s: 0.00 reconn/s: 0.00
[ 480s ] thds: 16 tps: 98.80 qps: 1582.81 (r/w/o: 1385.41/0.00/197.40) lat (ms,95%): 176.73 err/s: 0.00 reconn/s: 0.00
[ 490s ] thds: 16 tps: 95.70 qps: 1532.90 (r/w/o: 1341.20/0.00/191.70) lat (ms,95%): 179.94 err/s: 0.00 reconn/s: 0.00
[ 500s ] thds: 16 tps: 93.50 qps: 1494.41 (r/w/o: 1307.41/0.00/187.00) lat (ms,95%): 219.36 err/s: 0.00 reconn/s: 0.00
[ 510s ] thds: 16 tps: 86.60 qps: 1382.60 (r/w/o: 1209.50/0.00/173.10) lat (ms,95%): 257.95 err/s: 0.00 reconn/s: 0.00
[ 520s ] thds: 16 tps: 91.70 qps: 1470.10 (r/w/o: 1286.70/0.00/183.40) lat (ms,95%): 244.38 err/s: 0.00 reconn/s: 0.00
[ 530s ] thds: 16 tps: 85.50 qps: 1364.50 (r/w/o: 1193.50/0.00/171.00) lat (ms,95%): 257.95 err/s: 0.00 reconn/s: 0.00
[ 540s ] thds: 16 tps: 84.40 qps: 1354.29 (r/w/o: 1185.69/0.00/168.60) lat (ms,95%): 257.95 err/s: 0.00 reconn/s: 0.00
[ 550s ] thds: 16 tps: 93.70 qps: 1501.11 (r/w/o: 1313.51/0.00/187.60) lat (ms,95%): 215.44 err/s: 0.00 reconn/s: 0.00
[ 560s ] thds: 16 tps: 90.80 qps: 1447.90 (r/w/o: 1266.40/0.00/181.50) lat (ms,95%): 248.83 err/s: 0.00 reconn/s: 0.00
[ 570s ] thds: 16 tps: 95.40 qps: 1528.20 (r/w/o: 1337.30/0.00/190.90) lat (ms,95%): 200.47 err/s: 0.00 reconn/s: 0.00
[ 580s ] thds: 16 tps: 88.80 qps: 1423.80 (r/w/o: 1246.10/0.00/177.70) lat (ms,95%): 231.53 err/s: 0.00 reconn/s: 0.00
[ 590s ] thds: 16 tps: 95.60 qps: 1527.90 (r/w/o: 1336.90/0.00/191.00) lat (ms,95%): 227.40 err/s: 0.00 reconn/s: 0.00
[ 600s ] thds: 16 tps: 95.90 qps: 1532.00 (r/w/o: 1340.20/0.00/191.80) lat (ms,95%): 231.53 err/s: 0.00 reconn/s: 0.00
SQL statistics:
    queries performed:
        read:                            810194
        write:                           0
        other:                           115742
        total:                           925936
    transactions:                        57871  (96.42 per sec.)
    queries:                             925936 (1542.77 per sec.)
    ignored errors:                      0      (0.00 per sec.)
    reconnects:                          0      (0.00 per sec.)

Throughput:
    events/s (eps):                      96.4231
    time elapsed:                        600.1775s
    total number of events:              57871

Latency (ms):
         min:                                  140.44
         avg:                                  165.91
         max:                                  490.95
         95th percentile:                      200.47
         sum:                              9601272.86

Threads fairness:
    events (avg/stddev):           3616.9375/41.47
    execution time (avg/stddev):   600.0796/0.07
```