# RVBox13 gcc-riscv64-linux-gnu 编译器（-mtune=thead-c906）
## 编译
```shell
$ CGO_CFLAGS=-mtune=thead-c906 GOOS=linux GOARCH=riscv64 CC=riscv64-linux-gnu-gcc make server
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

[ 10s ] thds: 16 tps: 1651.11 qps: 1651.11 (r/w/o: 1651.11/0.00/0.00) lat (ms,95%): 12.30 err/s: 0.00 reconn/s: 0.00
[ 20s ] thds: 16 tps: 1632.10 qps: 1632.10 (r/w/o: 1632.10/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 30s ] thds: 16 tps: 1459.70 qps: 1459.70 (r/w/o: 1459.70/0.00/0.00) lat (ms,95%): 17.63 err/s: 0.00 reconn/s: 0.00
[ 40s ] thds: 16 tps: 1516.39 qps: 1516.39 (r/w/o: 1516.39/0.00/0.00) lat (ms,95%): 17.32 err/s: 0.00 reconn/s: 0.00
[ 50s ] thds: 16 tps: 1693.61 qps: 1693.61 (r/w/o: 1693.61/0.00/0.00) lat (ms,95%): 12.08 err/s: 0.00 reconn/s: 0.00
[ 60s ] thds: 16 tps: 1689.80 qps: 1689.80 (r/w/o: 1689.80/0.00/0.00) lat (ms,95%): 10.84 err/s: 0.00 reconn/s: 0.00
[ 70s ] thds: 16 tps: 1725.10 qps: 1725.10 (r/w/o: 1725.10/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 80s ] thds: 16 tps: 1755.70 qps: 1755.70 (r/w/o: 1755.70/0.00/0.00) lat (ms,95%): 10.46 err/s: 0.00 reconn/s: 0.00
[ 90s ] thds: 16 tps: 1740.10 qps: 1740.10 (r/w/o: 1740.10/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 100s ] thds: 16 tps: 1796.89 qps: 1796.89 (r/w/o: 1796.89/0.00/0.00) lat (ms,95%): 10.84 err/s: 0.00 reconn/s: 0.00
[ 110s ] thds: 16 tps: 1690.91 qps: 1690.91 (r/w/o: 1690.91/0.00/0.00) lat (ms,95%): 12.08 err/s: 0.00 reconn/s: 0.00
[ 120s ] thds: 16 tps: 1721.20 qps: 1721.20 (r/w/o: 1721.20/0.00/0.00) lat (ms,95%): 11.04 err/s: 0.00 reconn/s: 0.00
[ 130s ] thds: 16 tps: 1504.80 qps: 1504.80 (r/w/o: 1504.80/0.00/0.00) lat (ms,95%): 17.01 err/s: 0.00 reconn/s: 0.00
[ 140s ] thds: 16 tps: 1684.89 qps: 1684.89 (r/w/o: 1684.89/0.00/0.00) lat (ms,95%): 11.24 err/s: 0.00 reconn/s: 0.00
[ 150s ] thds: 16 tps: 1625.61 qps: 1625.61 (r/w/o: 1625.61/0.00/0.00) lat (ms,95%): 13.70 err/s: 0.00 reconn/s: 0.00
[ 160s ] thds: 16 tps: 1715.20 qps: 1715.20 (r/w/o: 1715.20/0.00/0.00) lat (ms,95%): 11.24 err/s: 0.00 reconn/s: 0.00
[ 170s ] thds: 16 tps: 1621.00 qps: 1621.00 (r/w/o: 1621.00/0.00/0.00) lat (ms,95%): 12.98 err/s: 0.00 reconn/s: 0.00
[ 180s ] thds: 16 tps: 1684.11 qps: 1684.11 (r/w/o: 1684.11/0.00/0.00) lat (ms,95%): 12.08 err/s: 0.00 reconn/s: 0.00
[ 190s ] thds: 16 tps: 1676.60 qps: 1676.60 (r/w/o: 1676.60/0.00/0.00) lat (ms,95%): 11.65 err/s: 0.00 reconn/s: 0.00
[ 200s ] thds: 16 tps: 1711.40 qps: 1711.40 (r/w/o: 1711.40/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 210s ] thds: 16 tps: 1698.81 qps: 1698.81 (r/w/o: 1698.81/0.00/0.00) lat (ms,95%): 11.24 err/s: 0.00 reconn/s: 0.00
[ 220s ] thds: 16 tps: 1706.70 qps: 1706.70 (r/w/o: 1706.70/0.00/0.00) lat (ms,95%): 10.84 err/s: 0.00 reconn/s: 0.00
[ 230s ] thds: 16 tps: 1726.00 qps: 1726.00 (r/w/o: 1726.00/0.00/0.00) lat (ms,95%): 11.04 err/s: 0.00 reconn/s: 0.00
[ 240s ] thds: 16 tps: 1774.90 qps: 1774.90 (r/w/o: 1774.90/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 250s ] thds: 16 tps: 1659.80 qps: 1659.80 (r/w/o: 1659.80/0.00/0.00) lat (ms,95%): 13.22 err/s: 0.00 reconn/s: 0.00
[ 260s ] thds: 16 tps: 1706.11 qps: 1706.11 (r/w/o: 1706.11/0.00/0.00) lat (ms,95%): 10.84 err/s: 0.00 reconn/s: 0.00
[ 270s ] thds: 16 tps: 1743.79 qps: 1743.79 (r/w/o: 1743.79/0.00/0.00) lat (ms,95%): 10.84 err/s: 0.00 reconn/s: 0.00
[ 280s ] thds: 16 tps: 1728.90 qps: 1728.90 (r/w/o: 1728.90/0.00/0.00) lat (ms,95%): 10.84 err/s: 0.00 reconn/s: 0.00
[ 290s ] thds: 16 tps: 1713.91 qps: 1713.91 (r/w/o: 1713.91/0.00/0.00) lat (ms,95%): 10.84 err/s: 0.00 reconn/s: 0.00
[ 300s ] thds: 16 tps: 1691.60 qps: 1691.60 (r/w/o: 1691.60/0.00/0.00) lat (ms,95%): 11.45 err/s: 0.00 reconn/s: 0.00
[ 310s ] thds: 16 tps: 1727.60 qps: 1727.60 (r/w/o: 1727.60/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 320s ] thds: 16 tps: 1692.29 qps: 1692.29 (r/w/o: 1692.29/0.00/0.00) lat (ms,95%): 11.04 err/s: 0.00 reconn/s: 0.00
[ 330s ] thds: 16 tps: 1703.10 qps: 1703.10 (r/w/o: 1703.10/0.00/0.00) lat (ms,95%): 11.24 err/s: 0.00 reconn/s: 0.00
[ 340s ] thds: 16 tps: 1698.81 qps: 1698.81 (r/w/o: 1698.81/0.00/0.00) lat (ms,95%): 10.84 err/s: 0.00 reconn/s: 0.00
[ 350s ] thds: 16 tps: 1678.19 qps: 1678.19 (r/w/o: 1678.19/0.00/0.00) lat (ms,95%): 11.24 err/s: 0.00 reconn/s: 0.00
[ 360s ] thds: 16 tps: 1696.10 qps: 1696.10 (r/w/o: 1696.10/0.00/0.00) lat (ms,95%): 11.65 err/s: 0.00 reconn/s: 0.00
[ 370s ] thds: 16 tps: 1709.41 qps: 1709.41 (r/w/o: 1709.41/0.00/0.00) lat (ms,95%): 11.45 err/s: 0.00 reconn/s: 0.00
[ 380s ] thds: 16 tps: 1723.79 qps: 1723.79 (r/w/o: 1723.79/0.00/0.00) lat (ms,95%): 11.04 err/s: 0.00 reconn/s: 0.00
[ 390s ] thds: 16 tps: 1690.10 qps: 1690.10 (r/w/o: 1690.10/0.00/0.00) lat (ms,95%): 11.45 err/s: 0.00 reconn/s: 0.00
[ 400s ] thds: 16 tps: 1656.41 qps: 1656.41 (r/w/o: 1656.41/0.00/0.00) lat (ms,95%): 12.08 err/s: 0.00 reconn/s: 0.00
[ 410s ] thds: 16 tps: 1617.89 qps: 1617.89 (r/w/o: 1617.89/0.00/0.00) lat (ms,95%): 12.52 err/s: 0.00 reconn/s: 0.00
[ 420s ] thds: 16 tps: 1703.71 qps: 1703.71 (r/w/o: 1703.71/0.00/0.00) lat (ms,95%): 10.84 err/s: 0.00 reconn/s: 0.00
[ 430s ] thds: 16 tps: 1703.20 qps: 1703.20 (r/w/o: 1703.20/0.00/0.00) lat (ms,95%): 11.04 err/s: 0.00 reconn/s: 0.00
[ 440s ] thds: 16 tps: 1662.50 qps: 1662.50 (r/w/o: 1662.50/0.00/0.00) lat (ms,95%): 12.75 err/s: 0.00 reconn/s: 0.00
[ 450s ] thds: 16 tps: 1739.90 qps: 1739.90 (r/w/o: 1739.90/0.00/0.00) lat (ms,95%): 10.84 err/s: 0.00 reconn/s: 0.00
[ 460s ] thds: 16 tps: 1709.09 qps: 1709.09 (r/w/o: 1709.09/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 470s ] thds: 16 tps: 1703.71 qps: 1703.71 (r/w/o: 1703.71/0.00/0.00) lat (ms,95%): 10.84 err/s: 0.00 reconn/s: 0.00
[ 480s ] thds: 16 tps: 1620.29 qps: 1620.29 (r/w/o: 1620.29/0.00/0.00) lat (ms,95%): 11.65 err/s: 0.00 reconn/s: 0.00
[ 490s ] thds: 16 tps: 1750.61 qps: 1750.61 (r/w/o: 1750.61/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 500s ] thds: 16 tps: 1767.79 qps: 1767.79 (r/w/o: 1767.79/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 510s ] thds: 16 tps: 1718.10 qps: 1718.10 (r/w/o: 1718.10/0.00/0.00) lat (ms,95%): 11.24 err/s: 0.00 reconn/s: 0.00
[ 520s ] thds: 16 tps: 1714.51 qps: 1714.51 (r/w/o: 1714.51/0.00/0.00) lat (ms,95%): 11.45 err/s: 0.00 reconn/s: 0.00
[ 530s ] thds: 16 tps: 1723.50 qps: 1723.50 (r/w/o: 1723.50/0.00/0.00) lat (ms,95%): 10.84 err/s: 0.00 reconn/s: 0.00
[ 540s ] thds: 16 tps: 1638.90 qps: 1638.90 (r/w/o: 1638.90/0.00/0.00) lat (ms,95%): 12.98 err/s: 0.00 reconn/s: 0.00
[ 550s ] thds: 16 tps: 1722.09 qps: 1722.09 (r/w/o: 1722.09/0.00/0.00) lat (ms,95%): 10.84 err/s: 0.00 reconn/s: 0.00
[ 560s ] thds: 16 tps: 1726.90 qps: 1726.90 (r/w/o: 1726.90/0.00/0.00) lat (ms,95%): 10.84 err/s: 0.00 reconn/s: 0.00
[ 570s ] thds: 16 tps: 1694.71 qps: 1694.71 (r/w/o: 1694.71/0.00/0.00) lat (ms,95%): 11.45 err/s: 0.00 reconn/s: 0.00
[ 580s ] thds: 16 tps: 1710.00 qps: 1710.00 (r/w/o: 1710.00/0.00/0.00) lat (ms,95%): 10.84 err/s: 0.00 reconn/s: 0.00
[ 590s ] thds: 16 tps: 1743.29 qps: 1743.29 (r/w/o: 1743.29/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 600s ] thds: 16 tps: 1762.20 qps: 1762.20 (r/w/o: 1762.20/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
SQL statistics:
    queries performed:
        read:                            1015573
        write:                           0
        other:                           0
        total:                           1015573
    transactions:                        1015573 (1692.59 per sec.)
    queries:                             1015573 (1692.59 per sec.)
    ignored errors:                      0      (0.00 per sec.)
    reconnects:                          0      (0.00 per sec.)

Throughput:
    events/s (eps):                      1692.5950
    time elapsed:                        600.0095s
    total number of events:              1015573

Latency (ms):
         min:                                    5.25
         avg:                                    9.45
         max:                                  154.02
         95th percentile:                       11.45
         sum:                              9599517.95

Threads fairness:
    events (avg/stddev):           63473.3125/5157.91
    execution time (avg/stddev):   599.9699/0.02
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

[ 10s ] thds: 16 tps: 1517.83 qps: 1517.83 (r/w/o: 0.00/1496.23/21.60) lat (ms,95%): 12.75 err/s: 0.00 reconn/s: 0.00
[ 20s ] thds: 16 tps: 1585.50 qps: 1585.50 (r/w/o: 0.00/1563.00/22.50) lat (ms,95%): 10.84 err/s: 0.00 reconn/s: 0.00
[ 30s ] thds: 16 tps: 1481.60 qps: 1481.60 (r/w/o: 0.00/1457.20/24.40) lat (ms,95%): 13.22 err/s: 0.00 reconn/s: 0.00
[ 40s ] thds: 16 tps: 1536.81 qps: 1536.81 (r/w/o: 0.00/1515.21/21.60) lat (ms,95%): 12.75 err/s: 0.00 reconn/s: 0.00
[ 50s ] thds: 16 tps: 1551.70 qps: 1551.70 (r/w/o: 0.00/1528.80/22.90) lat (ms,95%): 11.65 err/s: 0.00 reconn/s: 0.00
[ 60s ] thds: 16 tps: 1517.50 qps: 1517.50 (r/w/o: 0.00/1495.70/21.80) lat (ms,95%): 12.98 err/s: 0.00 reconn/s: 0.00
[ 70s ] thds: 16 tps: 1505.90 qps: 1505.90 (r/w/o: 0.00/1484.70/21.20) lat (ms,95%): 12.98 err/s: 0.00 reconn/s: 0.00
[ 80s ] thds: 16 tps: 1511.90 qps: 1511.90 (r/w/o: 0.00/1490.90/21.00) lat (ms,95%): 12.98 err/s: 0.00 reconn/s: 0.00
[ 90s ] thds: 16 tps: 1518.70 qps: 1518.70 (r/w/o: 0.00/1496.60/22.10) lat (ms,95%): 12.75 err/s: 0.00 reconn/s: 0.00
[ 100s ] thds: 16 tps: 1543.81 qps: 1543.81 (r/w/o: 0.00/1521.51/22.30) lat (ms,95%): 12.52 err/s: 0.00 reconn/s: 0.00
[ 110s ] thds: 16 tps: 1515.60 qps: 1515.60 (r/w/o: 0.00/1496.20/19.40) lat (ms,95%): 12.75 err/s: 0.00 reconn/s: 0.00
[ 120s ] thds: 16 tps: 1564.79 qps: 1564.79 (r/w/o: 0.00/1540.19/24.60) lat (ms,95%): 11.24 err/s: 0.00 reconn/s: 0.00
[ 130s ] thds: 16 tps: 1572.00 qps: 1572.00 (r/w/o: 0.00/1550.50/21.50) lat (ms,95%): 10.84 err/s: 0.00 reconn/s: 0.00
[ 140s ] thds: 16 tps: 1553.81 qps: 1553.81 (r/w/o: 0.00/1533.21/20.60) lat (ms,95%): 10.84 err/s: 0.00 reconn/s: 0.00
[ 150s ] thds: 16 tps: 1505.80 qps: 1505.80 (r/w/o: 0.00/1483.50/22.30) lat (ms,95%): 11.45 err/s: 0.00 reconn/s: 0.00
[ 160s ] thds: 16 tps: 1552.50 qps: 1552.50 (r/w/o: 0.00/1531.30/21.20) lat (ms,95%): 12.52 err/s: 0.00 reconn/s: 0.00
[ 170s ] thds: 16 tps: 1522.31 qps: 1522.31 (r/w/o: 0.00/1501.91/20.40) lat (ms,95%): 12.75 err/s: 0.00 reconn/s: 0.00
[ 180s ] thds: 16 tps: 1579.79 qps: 1579.79 (r/w/o: 0.00/1559.39/20.40) lat (ms,95%): 11.04 err/s: 0.00 reconn/s: 0.00
[ 190s ] thds: 16 tps: 1519.79 qps: 1519.79 (r/w/o: 0.00/1499.69/20.10) lat (ms,95%): 12.75 err/s: 0.00 reconn/s: 0.00
[ 200s ] thds: 16 tps: 1518.81 qps: 1518.81 (r/w/o: 0.00/1496.71/22.10) lat (ms,95%): 12.75 err/s: 0.00 reconn/s: 0.00
[ 210s ] thds: 16 tps: 1524.00 qps: 1524.00 (r/w/o: 0.00/1506.10/17.90) lat (ms,95%): 12.75 err/s: 0.00 reconn/s: 0.00
[ 220s ] thds: 16 tps: 1545.29 qps: 1545.29 (r/w/o: 0.00/1523.39/21.90) lat (ms,95%): 12.52 err/s: 0.00 reconn/s: 0.00
[ 230s ] thds: 16 tps: 1499.40 qps: 1499.40 (r/w/o: 0.00/1480.40/19.00) lat (ms,95%): 12.98 err/s: 0.00 reconn/s: 0.00
[ 240s ] thds: 16 tps: 1542.39 qps: 1542.39 (r/w/o: 0.00/1520.89/21.50) lat (ms,95%): 11.04 err/s: 0.00 reconn/s: 0.00
[ 250s ] thds: 16 tps: 1542.11 qps: 1542.11 (r/w/o: 0.00/1520.31/21.80) lat (ms,95%): 12.52 err/s: 0.00 reconn/s: 0.00
[ 260s ] thds: 16 tps: 1559.70 qps: 1559.70 (r/w/o: 0.00/1536.00/23.70) lat (ms,95%): 11.65 err/s: 0.00 reconn/s: 0.00
[ 270s ] thds: 16 tps: 1546.10 qps: 1546.10 (r/w/o: 0.00/1525.40/20.70) lat (ms,95%): 11.45 err/s: 0.00 reconn/s: 0.00
[ 280s ] thds: 16 tps: 1544.30 qps: 1544.30 (r/w/o: 0.00/1521.70/22.60) lat (ms,95%): 12.30 err/s: 0.00 reconn/s: 0.00
[ 290s ] thds: 16 tps: 1502.91 qps: 1502.91 (r/w/o: 0.00/1481.91/21.00) lat (ms,95%): 12.98 err/s: 0.00 reconn/s: 0.00
[ 300s ] thds: 16 tps: 1547.00 qps: 1547.00 (r/w/o: 0.00/1527.20/19.80) lat (ms,95%): 12.52 err/s: 0.00 reconn/s: 0.00
[ 310s ] thds: 16 tps: 1542.30 qps: 1542.30 (r/w/o: 0.00/1519.20/23.10) lat (ms,95%): 11.45 err/s: 0.00 reconn/s: 0.00
[ 320s ] thds: 16 tps: 1569.50 qps: 1569.50 (r/w/o: 0.00/1546.10/23.40) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 330s ] thds: 16 tps: 1570.31 qps: 1570.31 (r/w/o: 0.00/1547.01/23.30) lat (ms,95%): 11.04 err/s: 0.00 reconn/s: 0.00
[ 340s ] thds: 16 tps: 1582.40 qps: 1582.40 (r/w/o: 0.00/1559.40/23.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 350s ] thds: 16 tps: 1560.30 qps: 1560.30 (r/w/o: 0.00/1537.90/22.40) lat (ms,95%): 12.30 err/s: 0.00 reconn/s: 0.00
[ 360s ] thds: 16 tps: 1584.70 qps: 1584.70 (r/w/o: 0.00/1560.90/23.80) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 370s ] thds: 16 tps: 1582.30 qps: 1582.30 (r/w/o: 0.00/1559.90/22.40) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 380s ] thds: 16 tps: 1565.90 qps: 1565.90 (r/w/o: 0.00/1542.80/23.10) lat (ms,95%): 11.04 err/s: 0.00 reconn/s: 0.00
[ 390s ] thds: 16 tps: 1551.81 qps: 1551.81 (r/w/o: 0.00/1526.71/25.10) lat (ms,95%): 12.52 err/s: 0.00 reconn/s: 0.00
[ 400s ] thds: 16 tps: 1569.20 qps: 1569.20 (r/w/o: 0.00/1548.40/20.80) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 410s ] thds: 16 tps: 1505.99 qps: 1505.99 (r/w/o: 0.00/1485.09/20.90) lat (ms,95%): 12.75 err/s: 0.00 reconn/s: 0.00
[ 420s ] thds: 16 tps: 1543.59 qps: 1543.59 (r/w/o: 0.00/1519.39/24.20) lat (ms,95%): 12.52 err/s: 0.00 reconn/s: 0.00
[ 430s ] thds: 16 tps: 1542.91 qps: 1542.91 (r/w/o: 0.00/1521.41/21.50) lat (ms,95%): 12.52 err/s: 0.00 reconn/s: 0.00
[ 440s ] thds: 16 tps: 1563.50 qps: 1563.50 (r/w/o: 0.00/1540.70/22.80) lat (ms,95%): 12.52 err/s: 0.00 reconn/s: 0.00
[ 450s ] thds: 16 tps: 1563.90 qps: 1563.90 (r/w/o: 0.00/1543.30/20.60) lat (ms,95%): 12.30 err/s: 0.00 reconn/s: 0.00
[ 460s ] thds: 16 tps: 1578.00 qps: 1578.00 (r/w/o: 0.00/1556.10/21.90) lat (ms,95%): 11.04 err/s: 0.00 reconn/s: 0.00
[ 470s ] thds: 16 tps: 1530.00 qps: 1530.00 (r/w/o: 0.00/1505.90/24.10) lat (ms,95%): 12.75 err/s: 0.00 reconn/s: 0.00
[ 480s ] thds: 16 tps: 1562.50 qps: 1562.50 (r/w/o: 0.00/1541.50/21.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 490s ] thds: 16 tps: 1587.10 qps: 1587.10 (r/w/o: 0.00/1565.70/21.40) lat (ms,95%): 10.84 err/s: 0.00 reconn/s: 0.00
[ 500s ] thds: 16 tps: 1555.99 qps: 1555.99 (r/w/o: 0.00/1532.49/23.50) lat (ms,95%): 10.84 err/s: 0.00 reconn/s: 0.00
[ 510s ] thds: 16 tps: 1579.00 qps: 1579.00 (r/w/o: 0.00/1558.30/20.70) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 520s ] thds: 16 tps: 1557.31 qps: 1557.31 (r/w/o: 0.00/1533.11/24.20) lat (ms,95%): 12.08 err/s: 0.00 reconn/s: 0.00
[ 530s ] thds: 16 tps: 1535.69 qps: 1535.69 (r/w/o: 0.00/1511.59/24.10) lat (ms,95%): 11.45 err/s: 0.00 reconn/s: 0.00
[ 540s ] thds: 16 tps: 1520.10 qps: 1520.10 (r/w/o: 0.00/1497.40/22.70) lat (ms,95%): 12.75 err/s: 0.00 reconn/s: 0.00
[ 550s ] thds: 16 tps: 1525.00 qps: 1525.00 (r/w/o: 0.00/1505.60/19.40) lat (ms,95%): 12.75 err/s: 0.00 reconn/s: 0.00
[ 560s ] thds: 16 tps: 1560.70 qps: 1560.70 (r/w/o: 0.00/1537.00/23.70) lat (ms,95%): 12.30 err/s: 0.00 reconn/s: 0.00
[ 570s ] thds: 16 tps: 1559.90 qps: 1559.90 (r/w/o: 0.00/1535.80/24.10) lat (ms,95%): 12.30 err/s: 0.00 reconn/s: 0.00
[ 580s ] thds: 16 tps: 1569.80 qps: 1569.80 (r/w/o: 0.00/1547.40/22.40) lat (ms,95%): 12.30 err/s: 0.00 reconn/s: 0.00
[ 590s ] thds: 16 tps: 1538.70 qps: 1538.70 (r/w/o: 0.00/1519.00/19.70) lat (ms,95%): 12.30 err/s: 0.00 reconn/s: 0.00
[ 600s ] thds: 16 tps: 1563.50 qps: 1563.50 (r/w/o: 0.00/1541.70/21.80) lat (ms,95%): 11.65 err/s: 0.00 reconn/s: 0.00
SQL statistics:
    queries performed:
        read:                            0
        write:                           914344
        other:                           13190
        total:                           927534
    transactions:                        927534 (1545.86 per sec.)
    queries:                             927534 (1545.86 per sec.)
    ignored errors:                      0      (0.00 per sec.)
    reconnects:                          0      (0.00 per sec.)

Throughput:
    events/s (eps):                      1545.8622
    time elapsed:                        600.0108s
    total number of events:              927534

Latency (ms):
         min:                                    5.01
         avg:                                   10.35
         max:                                  339.49
         95th percentile:                       12.52
         sum:                              9599586.06

Threads fairness:
    events (avg/stddev):           57970.8750/337.16
    execution time (avg/stddev):   599.9741/0.01
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

[ 10s ] thds: 16 tps: 89.58 qps: 1446.61 (r/w/o: 1266.15/0.00/180.46) lat (ms,95%): 196.89 err/s: 0.00 reconn/s: 0.00
[ 20s ] thds: 16 tps: 97.00 qps: 1550.14 (r/w/o: 1355.94/0.00/194.21) lat (ms,95%): 176.73 err/s: 0.00 reconn/s: 0.00
[ 30s ] thds: 16 tps: 96.50 qps: 1546.40 (r/w/o: 1353.40/0.00/193.00) lat (ms,95%): 179.94 err/s: 0.00 reconn/s: 0.00
[ 40s ] thds: 16 tps: 94.40 qps: 1510.30 (r/w/o: 1321.50/0.00/188.80) lat (ms,95%): 179.94 err/s: 0.00 reconn/s: 0.00
[ 50s ] thds: 16 tps: 96.10 qps: 1536.70 (r/w/o: 1344.50/0.00/192.20) lat (ms,95%): 179.94 err/s: 0.00 reconn/s: 0.00
[ 60s ] thds: 16 tps: 97.60 qps: 1560.40 (r/w/o: 1365.40/0.00/195.00) lat (ms,95%): 173.58 err/s: 0.00 reconn/s: 0.00
[ 70s ] thds: 16 tps: 95.30 qps: 1525.39 (r/w/o: 1334.69/0.00/190.70) lat (ms,95%): 179.94 err/s: 0.00 reconn/s: 0.00
[ 80s ] thds: 16 tps: 93.50 qps: 1497.20 (r/w/o: 1310.30/0.00/186.90) lat (ms,95%): 183.21 err/s: 0.00 reconn/s: 0.00
[ 90s ] thds: 16 tps: 94.80 qps: 1514.99 (r/w/o: 1325.29/0.00/189.70) lat (ms,95%): 186.54 err/s: 0.00 reconn/s: 0.00
[ 100s ] thds: 16 tps: 97.00 qps: 1552.61 (r/w/o: 1358.41/0.00/194.20) lat (ms,95%): 176.73 err/s: 0.00 reconn/s: 0.00
[ 110s ] thds: 16 tps: 97.20 qps: 1555.10 (r/w/o: 1360.70/0.00/194.40) lat (ms,95%): 173.58 err/s: 0.00 reconn/s: 0.00
[ 120s ] thds: 16 tps: 98.00 qps: 1567.99 (r/w/o: 1372.00/0.00/196.00) lat (ms,95%): 176.73 err/s: 0.00 reconn/s: 0.00
[ 130s ] thds: 16 tps: 97.10 qps: 1556.61 (r/w/o: 1362.41/0.00/194.20) lat (ms,95%): 176.73 err/s: 0.00 reconn/s: 0.00
[ 140s ] thds: 16 tps: 99.00 qps: 1578.30 (r/w/o: 1380.40/0.00/197.90) lat (ms,95%): 170.48 err/s: 0.00 reconn/s: 0.00
[ 150s ] thds: 16 tps: 97.60 qps: 1566.09 (r/w/o: 1370.79/0.00/195.30) lat (ms,95%): 173.58 err/s: 0.00 reconn/s: 0.00
[ 160s ] thds: 16 tps: 94.60 qps: 1514.21 (r/w/o: 1325.01/0.00/189.20) lat (ms,95%): 176.73 err/s: 0.00 reconn/s: 0.00
[ 170s ] thds: 16 tps: 97.70 qps: 1560.80 (r/w/o: 1365.50/0.00/195.30) lat (ms,95%): 176.73 err/s: 0.00 reconn/s: 0.00
[ 180s ] thds: 16 tps: 99.20 qps: 1584.60 (r/w/o: 1386.10/0.00/198.50) lat (ms,95%): 170.48 err/s: 0.00 reconn/s: 0.00
[ 190s ] thds: 16 tps: 96.60 qps: 1549.80 (r/w/o: 1356.70/0.00/193.10) lat (ms,95%): 176.73 err/s: 0.00 reconn/s: 0.00
[ 200s ] thds: 16 tps: 97.40 qps: 1557.49 (r/w/o: 1362.80/0.00/194.70) lat (ms,95%): 173.58 err/s: 0.00 reconn/s: 0.00
[ 210s ] thds: 16 tps: 99.00 qps: 1582.50 (r/w/o: 1384.40/0.00/198.10) lat (ms,95%): 170.48 err/s: 0.00 reconn/s: 0.00
[ 220s ] thds: 16 tps: 96.30 qps: 1543.70 (r/w/o: 1351.20/0.00/192.50) lat (ms,95%): 176.73 err/s: 0.00 reconn/s: 0.00
[ 230s ] thds: 16 tps: 95.40 qps: 1525.40 (r/w/o: 1334.50/0.00/190.90) lat (ms,95%): 179.94 err/s: 0.00 reconn/s: 0.00
[ 240s ] thds: 16 tps: 99.00 qps: 1581.00 (r/w/o: 1383.00/0.00/198.00) lat (ms,95%): 173.58 err/s: 0.00 reconn/s: 0.00
[ 250s ] thds: 16 tps: 99.00 qps: 1588.30 (r/w/o: 1390.20/0.00/198.10) lat (ms,95%): 170.48 err/s: 0.00 reconn/s: 0.00
[ 260s ] thds: 16 tps: 97.00 qps: 1554.70 (r/w/o: 1360.80/0.00/193.90) lat (ms,95%): 173.58 err/s: 0.00 reconn/s: 0.00
[ 270s ] thds: 16 tps: 96.90 qps: 1546.90 (r/w/o: 1353.20/0.00/193.70) lat (ms,95%): 179.94 err/s: 0.00 reconn/s: 0.00
[ 280s ] thds: 16 tps: 96.70 qps: 1547.50 (r/w/o: 1353.90/0.00/193.60) lat (ms,95%): 176.73 err/s: 0.00 reconn/s: 0.00
[ 290s ] thds: 16 tps: 97.60 qps: 1559.30 (r/w/o: 1364.20/0.00/195.10) lat (ms,95%): 176.73 err/s: 0.00 reconn/s: 0.00
[ 300s ] thds: 16 tps: 97.80 qps: 1565.79 (r/w/o: 1370.19/0.00/195.60) lat (ms,95%): 173.58 err/s: 0.00 reconn/s: 0.00
[ 310s ] thds: 16 tps: 97.80 qps: 1567.50 (r/w/o: 1371.90/0.00/195.60) lat (ms,95%): 173.58 err/s: 0.00 reconn/s: 0.00
[ 320s ] thds: 16 tps: 98.20 qps: 1566.90 (r/w/o: 1370.40/0.00/196.50) lat (ms,95%): 173.58 err/s: 0.00 reconn/s: 0.00
[ 330s ] thds: 16 tps: 99.60 qps: 1595.01 (r/w/o: 1395.80/0.00/199.20) lat (ms,95%): 170.48 err/s: 0.00 reconn/s: 0.00
[ 340s ] thds: 16 tps: 97.40 qps: 1556.69 (r/w/o: 1361.99/0.00/194.70) lat (ms,95%): 173.58 err/s: 0.00 reconn/s: 0.00
[ 350s ] thds: 16 tps: 98.40 qps: 1573.91 (r/w/o: 1377.21/0.00/196.70) lat (ms,95%): 173.58 err/s: 0.00 reconn/s: 0.00
[ 360s ] thds: 16 tps: 99.30 qps: 1591.90 (r/w/o: 1393.20/0.00/198.70) lat (ms,95%): 170.48 err/s: 0.00 reconn/s: 0.00
[ 370s ] thds: 16 tps: 99.00 qps: 1582.39 (r/w/o: 1384.39/0.00/198.00) lat (ms,95%): 170.48 err/s: 0.00 reconn/s: 0.00
[ 380s ] thds: 16 tps: 95.00 qps: 1524.01 (r/w/o: 1333.91/0.00/190.10) lat (ms,95%): 176.73 err/s: 0.00 reconn/s: 0.00
[ 390s ] thds: 16 tps: 97.70 qps: 1559.00 (r/w/o: 1363.90/0.00/195.10) lat (ms,95%): 179.94 err/s: 0.00 reconn/s: 0.00
[ 400s ] thds: 16 tps: 99.30 qps: 1590.90 (r/w/o: 1392.10/0.00/198.80) lat (ms,95%): 170.48 err/s: 0.00 reconn/s: 0.00
[ 410s ] thds: 16 tps: 98.40 qps: 1575.29 (r/w/o: 1378.49/0.00/196.80) lat (ms,95%): 170.48 err/s: 0.00 reconn/s: 0.00
[ 420s ] thds: 16 tps: 98.60 qps: 1577.00 (r/w/o: 1379.70/0.00/197.30) lat (ms,95%): 173.58 err/s: 0.00 reconn/s: 0.00
[ 430s ] thds: 16 tps: 97.40 qps: 1558.91 (r/w/o: 1364.11/0.00/194.80) lat (ms,95%): 170.48 err/s: 0.00 reconn/s: 0.00
[ 440s ] thds: 16 tps: 98.30 qps: 1572.10 (r/w/o: 1375.50/0.00/196.60) lat (ms,95%): 173.58 err/s: 0.00 reconn/s: 0.00
[ 450s ] thds: 16 tps: 99.70 qps: 1592.70 (r/w/o: 1393.50/0.00/199.20) lat (ms,95%): 170.48 err/s: 0.00 reconn/s: 0.00
[ 460s ] thds: 16 tps: 98.20 qps: 1569.99 (r/w/o: 1373.79/0.00/196.20) lat (ms,95%): 170.48 err/s: 0.00 reconn/s: 0.00
[ 470s ] thds: 16 tps: 97.30 qps: 1558.80 (r/w/o: 1363.80/0.00/195.00) lat (ms,95%): 173.58 err/s: 0.00 reconn/s: 0.00
[ 480s ] thds: 16 tps: 98.30 qps: 1569.80 (r/w/o: 1373.30/0.00/196.50) lat (ms,95%): 176.73 err/s: 0.00 reconn/s: 0.00
[ 490s ] thds: 16 tps: 97.40 qps: 1563.00 (r/w/o: 1368.10/0.00/194.90) lat (ms,95%): 173.58 err/s: 0.00 reconn/s: 0.00
[ 500s ] thds: 16 tps: 95.10 qps: 1525.00 (r/w/o: 1334.90/0.00/190.10) lat (ms,95%): 176.73 err/s: 0.00 reconn/s: 0.00
[ 510s ] thds: 16 tps: 94.90 qps: 1512.59 (r/w/o: 1322.69/0.00/189.90) lat (ms,95%): 200.47 err/s: 0.00 reconn/s: 0.00
[ 520s ] thds: 16 tps: 97.30 qps: 1558.10 (r/w/o: 1363.90/0.00/194.20) lat (ms,95%): 173.58 err/s: 0.00 reconn/s: 0.00
[ 530s ] thds: 16 tps: 97.80 qps: 1565.50 (r/w/o: 1369.70/0.00/195.80) lat (ms,95%): 176.73 err/s: 0.00 reconn/s: 0.00
[ 540s ] thds: 16 tps: 97.90 qps: 1567.19 (r/w/o: 1371.39/0.00/195.80) lat (ms,95%): 173.58 err/s: 0.00 reconn/s: 0.00
[ 550s ] thds: 16 tps: 100.40 qps: 1605.60 (r/w/o: 1404.70/0.00/200.90) lat (ms,95%): 167.44 err/s: 0.00 reconn/s: 0.00
[ 560s ] thds: 16 tps: 100.00 qps: 1599.10 (r/w/o: 1399.00/0.00/200.10) lat (ms,95%): 167.44 err/s: 0.00 reconn/s: 0.00
[ 570s ] thds: 16 tps: 100.70 qps: 1613.00 (r/w/o: 1411.60/0.00/201.40) lat (ms,95%): 167.44 err/s: 0.00 reconn/s: 0.00
[ 580s ] thds: 16 tps: 102.90 qps: 1644.21 (r/w/o: 1438.41/0.00/205.80) lat (ms,95%): 164.45 err/s: 0.00 reconn/s: 0.00
[ 590s ] thds: 16 tps: 100.60 qps: 1609.80 (r/w/o: 1408.70/0.00/201.10) lat (ms,95%): 170.48 err/s: 0.00 reconn/s: 0.00
[ 600s ] thds: 16 tps: 99.90 qps: 1599.80 (r/w/o: 1400.20/0.00/199.60) lat (ms,95%): 170.48 err/s: 0.00 reconn/s: 0.00
SQL statistics:
    queries performed:
        read:                            819742
        write:                           0
        other:                           117106
        total:                           936848
    transactions:                        58553  (97.56 per sec.)
    queries:                             936848 (1561.00 per sec.)
    ignored errors:                      0      (0.00 per sec.)
    reconnects:                          0      (0.00 per sec.)

Throughput:
    events/s (eps):                      97.5627
    time elapsed:                        600.1575s
    total number of events:              58553

Latency (ms):
         min:                                  141.92
         avg:                                  163.97
         max:                                  469.82
         95th percentile:                      176.73
         sum:                              9600983.06

Threads fairness:
    events (avg/stddev):           3659.5625/35.46
    execution time (avg/stddev):   600.0614/0.06
```