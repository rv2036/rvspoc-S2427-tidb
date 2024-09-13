# RVBox13 gcc-riscv64-linux-gnu 编译器（默认参数）

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

[ 10s ] thds: 16 tps: 1675.81 qps: 1675.81 (r/w/o: 1675.81/0.00/0.00) lat (ms,95%): 10.84 err/s: 0.00 reconn/s: 0.00
[ 20s ] thds: 16 tps: 1622.30 qps: 1622.30 (r/w/o: 1622.30/0.00/0.00) lat (ms,95%): 13.22 err/s: 0.00 reconn/s: 0.00
[ 30s ] thds: 16 tps: 1680.80 qps: 1680.80 (r/w/o: 1680.80/0.00/0.00) lat (ms,95%): 10.84 err/s: 0.00 reconn/s: 0.00
[ 40s ] thds: 16 tps: 1638.60 qps: 1638.60 (r/w/o: 1638.60/0.00/0.00) lat (ms,95%): 12.30 err/s: 0.00 reconn/s: 0.00
[ 50s ] thds: 16 tps: 1688.39 qps: 1688.39 (r/w/o: 1688.39/0.00/0.00) lat (ms,95%): 11.04 err/s: 0.00 reconn/s: 0.00
[ 60s ] thds: 16 tps: 1668.19 qps: 1668.19 (r/w/o: 1668.19/0.00/0.00) lat (ms,95%): 11.04 err/s: 0.00 reconn/s: 0.00
[ 70s ] thds: 16 tps: 1671.92 qps: 1671.92 (r/w/o: 1671.92/0.00/0.00) lat (ms,95%): 11.45 err/s: 0.00 reconn/s: 0.00
[ 80s ] thds: 16 tps: 1586.99 qps: 1586.99 (r/w/o: 1586.99/0.00/0.00) lat (ms,95%): 11.24 err/s: 0.00 reconn/s: 0.00
[ 90s ] thds: 16 tps: 1701.31 qps: 1701.31 (r/w/o: 1701.31/0.00/0.00) lat (ms,95%): 11.45 err/s: 0.00 reconn/s: 0.00
[ 100s ] thds: 16 tps: 1715.89 qps: 1715.89 (r/w/o: 1715.89/0.00/0.00) lat (ms,95%): 11.04 err/s: 0.00 reconn/s: 0.00
[ 110s ] thds: 16 tps: 1703.11 qps: 1703.11 (r/w/o: 1703.11/0.00/0.00) lat (ms,95%): 10.84 err/s: 0.00 reconn/s: 0.00
[ 120s ] thds: 16 tps: 1657.79 qps: 1657.79 (r/w/o: 1657.79/0.00/0.00) lat (ms,95%): 11.04 err/s: 0.00 reconn/s: 0.00
[ 130s ] thds: 16 tps: 1677.80 qps: 1677.80 (r/w/o: 1677.80/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 140s ] thds: 16 tps: 1638.60 qps: 1638.60 (r/w/o: 1638.60/0.00/0.00) lat (ms,95%): 12.08 err/s: 0.00 reconn/s: 0.00
[ 150s ] thds: 16 tps: 1659.40 qps: 1659.40 (r/w/o: 1659.40/0.00/0.00) lat (ms,95%): 11.45 err/s: 0.00 reconn/s: 0.00
[ 160s ] thds: 16 tps: 1661.00 qps: 1661.00 (r/w/o: 1661.00/0.00/0.00) lat (ms,95%): 11.65 err/s: 0.00 reconn/s: 0.00
[ 170s ] thds: 16 tps: 1676.30 qps: 1676.30 (r/w/o: 1676.30/0.00/0.00) lat (ms,95%): 11.04 err/s: 0.00 reconn/s: 0.00
[ 180s ] thds: 16 tps: 1661.69 qps: 1661.69 (r/w/o: 1661.69/0.00/0.00) lat (ms,95%): 11.04 err/s: 0.00 reconn/s: 0.00
[ 190s ] thds: 16 tps: 1670.01 qps: 1670.01 (r/w/o: 1670.01/0.00/0.00) lat (ms,95%): 11.24 err/s: 0.00 reconn/s: 0.00
[ 200s ] thds: 16 tps: 1668.80 qps: 1668.80 (r/w/o: 1668.80/0.00/0.00) lat (ms,95%): 11.87 err/s: 0.00 reconn/s: 0.00
[ 210s ] thds: 16 tps: 1665.40 qps: 1665.40 (r/w/o: 1665.40/0.00/0.00) lat (ms,95%): 11.87 err/s: 0.00 reconn/s: 0.00
[ 220s ] thds: 16 tps: 1655.60 qps: 1655.60 (r/w/o: 1655.60/0.00/0.00) lat (ms,95%): 11.65 err/s: 0.00 reconn/s: 0.00
[ 230s ] thds: 16 tps: 1667.10 qps: 1667.10 (r/w/o: 1667.10/0.00/0.00) lat (ms,95%): 10.84 err/s: 0.00 reconn/s: 0.00
[ 240s ] thds: 16 tps: 1681.50 qps: 1681.50 (r/w/o: 1681.50/0.00/0.00) lat (ms,95%): 11.04 err/s: 0.00 reconn/s: 0.00
[ 250s ] thds: 16 tps: 1664.60 qps: 1664.60 (r/w/o: 1664.60/0.00/0.00) lat (ms,95%): 11.24 err/s: 0.00 reconn/s: 0.00
[ 260s ] thds: 16 tps: 1625.90 qps: 1625.90 (r/w/o: 1625.90/0.00/0.00) lat (ms,95%): 12.75 err/s: 0.00 reconn/s: 0.00
[ 270s ] thds: 16 tps: 1613.10 qps: 1613.10 (r/w/o: 1613.10/0.00/0.00) lat (ms,95%): 12.98 err/s: 0.00 reconn/s: 0.00
[ 280s ] thds: 16 tps: 1658.01 qps: 1658.01 (r/w/o: 1658.01/0.00/0.00) lat (ms,95%): 11.24 err/s: 0.00 reconn/s: 0.00
[ 290s ] thds: 16 tps: 1662.80 qps: 1662.80 (r/w/o: 1662.80/0.00/0.00) lat (ms,95%): 11.24 err/s: 0.00 reconn/s: 0.00
[ 300s ] thds: 16 tps: 1685.30 qps: 1685.30 (r/w/o: 1685.30/0.00/0.00) lat (ms,95%): 10.84 err/s: 0.00 reconn/s: 0.00
[ 310s ] thds: 16 tps: 1656.49 qps: 1656.49 (r/w/o: 1656.49/0.00/0.00) lat (ms,95%): 11.65 err/s: 0.00 reconn/s: 0.00
[ 320s ] thds: 16 tps: 1690.31 qps: 1690.31 (r/w/o: 1690.31/0.00/0.00) lat (ms,95%): 11.04 err/s: 0.00 reconn/s: 0.00
[ 330s ] thds: 16 tps: 1665.10 qps: 1665.10 (r/w/o: 1665.10/0.00/0.00) lat (ms,95%): 11.04 err/s: 0.00 reconn/s: 0.00
[ 340s ] thds: 16 tps: 1675.49 qps: 1675.49 (r/w/o: 1675.49/0.00/0.00) lat (ms,95%): 11.04 err/s: 0.00 reconn/s: 0.00
[ 350s ] thds: 16 tps: 1641.01 qps: 1641.01 (r/w/o: 1641.01/0.00/0.00) lat (ms,95%): 12.08 err/s: 0.00 reconn/s: 0.00
[ 360s ] thds: 16 tps: 1688.40 qps: 1688.40 (r/w/o: 1688.40/0.00/0.00) lat (ms,95%): 10.84 err/s: 0.00 reconn/s: 0.00
[ 370s ] thds: 16 tps: 1653.70 qps: 1653.70 (r/w/o: 1653.70/0.00/0.00) lat (ms,95%): 11.65 err/s: 0.00 reconn/s: 0.00
[ 380s ] thds: 16 tps: 1472.90 qps: 1472.90 (r/w/o: 1472.90/0.00/0.00) lat (ms,95%): 18.95 err/s: 0.00 reconn/s: 0.00
[ 390s ] thds: 16 tps: 1658.69 qps: 1658.69 (r/w/o: 1658.69/0.00/0.00) lat (ms,95%): 11.45 err/s: 0.00 reconn/s: 0.00
[ 400s ] thds: 16 tps: 1654.40 qps: 1654.40 (r/w/o: 1654.40/0.00/0.00) lat (ms,95%): 11.87 err/s: 0.00 reconn/s: 0.00
[ 410s ] thds: 16 tps: 1672.01 qps: 1672.01 (r/w/o: 1672.01/0.00/0.00) lat (ms,95%): 10.84 err/s: 0.00 reconn/s: 0.00
[ 420s ] thds: 16 tps: 1690.10 qps: 1690.10 (r/w/o: 1690.10/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 430s ] thds: 16 tps: 1701.60 qps: 1701.60 (r/w/o: 1701.60/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 440s ] thds: 16 tps: 1702.90 qps: 1702.90 (r/w/o: 1702.90/0.00/0.00) lat (ms,95%): 10.84 err/s: 0.00 reconn/s: 0.00
[ 450s ] thds: 16 tps: 1691.80 qps: 1691.80 (r/w/o: 1691.80/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 460s ] thds: 16 tps: 1704.30 qps: 1704.30 (r/w/o: 1704.30/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 470s ] thds: 16 tps: 1672.80 qps: 1672.80 (r/w/o: 1672.80/0.00/0.00) lat (ms,95%): 10.84 err/s: 0.00 reconn/s: 0.00
[ 480s ] thds: 16 tps: 1694.80 qps: 1694.80 (r/w/o: 1694.80/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 490s ] thds: 16 tps: 1693.40 qps: 1693.40 (r/w/o: 1693.40/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 500s ] thds: 16 tps: 1680.60 qps: 1680.60 (r/w/o: 1680.60/0.00/0.00) lat (ms,95%): 11.04 err/s: 0.00 reconn/s: 0.00
[ 510s ] thds: 16 tps: 1680.10 qps: 1680.10 (r/w/o: 1680.10/0.00/0.00) lat (ms,95%): 10.84 err/s: 0.00 reconn/s: 0.00
[ 520s ] thds: 16 tps: 1614.70 qps: 1614.70 (r/w/o: 1614.70/0.00/0.00) lat (ms,95%): 10.84 err/s: 0.00 reconn/s: 0.00
[ 530s ] thds: 16 tps: 1615.99 qps: 1615.99 (r/w/o: 1615.99/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 540s ] thds: 16 tps: 1720.01 qps: 1720.01 (r/w/o: 1720.01/0.00/0.00) lat (ms,95%): 10.46 err/s: 0.00 reconn/s: 0.00
[ 550s ] thds: 16 tps: 1723.30 qps: 1723.30 (r/w/o: 1723.30/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 560s ] thds: 16 tps: 1716.30 qps: 1716.30 (r/w/o: 1716.30/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 570s ] thds: 16 tps: 1698.70 qps: 1698.70 (r/w/o: 1698.70/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 580s ] thds: 16 tps: 1683.39 qps: 1683.39 (r/w/o: 1683.39/0.00/0.00) lat (ms,95%): 10.65 err/s: 0.00 reconn/s: 0.00
[ 590s ] thds: 16 tps: 1680.91 qps: 1680.91 (r/w/o: 1680.91/0.00/0.00) lat (ms,95%): 10.84 err/s: 0.00 reconn/s: 0.00
[ 600s ] thds: 16 tps: 1677.50 qps: 1677.50 (r/w/o: 1677.50/0.00/0.00) lat (ms,95%): 10.84 err/s: 0.00 reconn/s: 0.00
SQL statistics:
    queries performed:
        read:                            1000776
        write:                           0
        other:                           0
        total:                           1000776
    transactions:                        1000776 (1667.92 per sec.)
    queries:                             1000776 (1667.92 per sec.)
    ignored errors:                      0      (0.00 per sec.)
    reconnects:                          0      (0.00 per sec.)

Throughput:
    events/s (eps):                      1667.9222
    time elapsed:                        600.0136s
    total number of events:              1000776

Latency (ms):
         min:                                    5.18
         avg:                                    9.59
         max:                                  222.04
         95th percentile:                       11.04
         sum:                              9599602.12

Threads fairness:
    events (avg/stddev):           62548.5000/5915.59
    execution time (avg/stddev):   599.9751/0.02
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

[ 10s ] thds: 16 tps: 1513.63 qps: 1513.63 (r/w/o: 0.00/1491.94/21.70) lat (ms,95%): 12.75 err/s: 0.00 reconn/s: 0.00
[ 20s ] thds: 16 tps: 1493.10 qps: 1493.10 (r/w/o: 0.00/1471.10/22.00) lat (ms,95%): 12.98 err/s: 0.00 reconn/s: 0.00
[ 30s ] thds: 16 tps: 1507.51 qps: 1507.51 (r/w/o: 0.00/1485.91/21.60) lat (ms,95%): 13.22 err/s: 0.00 reconn/s: 0.00
[ 40s ] thds: 16 tps: 1534.39 qps: 1534.39 (r/w/o: 0.00/1511.79/22.60) lat (ms,95%): 12.75 err/s: 0.00 reconn/s: 0.00
[ 50s ] thds: 16 tps: 1523.60 qps: 1523.60 (r/w/o: 0.00/1499.00/24.60) lat (ms,95%): 12.98 err/s: 0.00 reconn/s: 0.00
[ 60s ] thds: 16 tps: 1545.80 qps: 1545.80 (r/w/o: 0.00/1522.40/23.40) lat (ms,95%): 12.52 err/s: 0.00 reconn/s: 0.00
[ 70s ] thds: 16 tps: 1436.60 qps: 1436.60 (r/w/o: 0.00/1414.40/22.20) lat (ms,95%): 15.00 err/s: 0.00 reconn/s: 0.00
[ 80s ] thds: 16 tps: 1433.10 qps: 1433.10 (r/w/o: 0.00/1412.20/20.90) lat (ms,95%): 15.27 err/s: 0.00 reconn/s: 0.00
[ 90s ] thds: 16 tps: 1285.10 qps: 1285.10 (r/w/o: 0.00/1266.20/18.90) lat (ms,95%): 20.37 err/s: 0.00 reconn/s: 0.00
[ 100s ] thds: 16 tps: 1134.50 qps: 1134.50 (r/w/o: 0.00/1117.00/17.50) lat (ms,95%): 21.89 err/s: 0.00 reconn/s: 0.00
[ 110s ] thds: 16 tps: 1353.69 qps: 1353.69 (r/w/o: 0.00/1333.49/20.20) lat (ms,95%): 17.32 err/s: 0.00 reconn/s: 0.00
[ 120s ] thds: 16 tps: 1300.91 qps: 1300.91 (r/w/o: 0.00/1283.11/17.80) lat (ms,95%): 20.00 err/s: 0.00 reconn/s: 0.00
[ 130s ] thds: 16 tps: 1296.50 qps: 1296.50 (r/w/o: 0.00/1277.00/19.50) lat (ms,95%): 19.65 err/s: 0.00 reconn/s: 0.00
[ 140s ] thds: 16 tps: 1222.90 qps: 1222.90 (r/w/o: 0.00/1204.80/18.10) lat (ms,95%): 21.50 err/s: 0.00 reconn/s: 0.00
[ 150s ] thds: 16 tps: 1304.29 qps: 1304.29 (r/w/o: 0.00/1284.79/19.50) lat (ms,95%): 21.50 err/s: 0.00 reconn/s: 0.00
[ 160s ] thds: 16 tps: 1213.91 qps: 1213.91 (r/w/o: 0.00/1194.81/19.10) lat (ms,95%): 25.28 err/s: 0.00 reconn/s: 0.00
[ 170s ] thds: 16 tps: 629.70 qps: 629.70 (r/w/o: 0.00/619.80/9.90) lat (ms,95%): 57.87 err/s: 0.00 reconn/s: 0.00
[ 180s ] thds: 16 tps: 781.60 qps: 781.60 (r/w/o: 0.00/770.70/10.90) lat (ms,95%): 35.59 err/s: 0.00 reconn/s: 0.00
[ 190s ] thds: 16 tps: 908.90 qps: 908.90 (r/w/o: 0.00/898.60/10.30) lat (ms,95%): 28.67 err/s: 0.00 reconn/s: 0.00
[ 200s ] thds: 16 tps: 1045.00 qps: 1045.00 (r/w/o: 0.00/1028.50/16.50) lat (ms,95%): 22.69 err/s: 0.00 reconn/s: 0.00
[ 210s ] thds: 16 tps: 1123.10 qps: 1123.10 (r/w/o: 0.00/1105.40/17.70) lat (ms,95%): 20.74 err/s: 0.00 reconn/s: 0.00
[ 220s ] thds: 16 tps: 1001.80 qps: 1001.80 (r/w/o: 0.00/988.20/13.60) lat (ms,95%): 41.10 err/s: 0.00 reconn/s: 0.00
[ 230s ] thds: 16 tps: 420.50 qps: 420.50 (r/w/o: 0.00/415.40/5.10) lat (ms,95%): 75.82 err/s: 0.00 reconn/s: 0.00
[ 240s ] thds: 16 tps: 613.60 qps: 613.60 (r/w/o: 0.00/603.50/10.10) lat (ms,95%): 44.17 err/s: 0.00 reconn/s: 0.00
[ 250s ] thds: 16 tps: 732.90 qps: 732.90 (r/w/o: 0.00/722.50/10.40) lat (ms,95%): 50.11 err/s: 0.00 reconn/s: 0.00
[ 260s ] thds: 16 tps: 1072.20 qps: 1072.20 (r/w/o: 0.00/1055.50/16.70) lat (ms,95%): 23.95 err/s: 0.00 reconn/s: 0.00
[ 270s ] thds: 16 tps: 852.20 qps: 852.20 (r/w/o: 0.00/840.60/11.60) lat (ms,95%): 47.47 err/s: 0.00 reconn/s: 0.00
[ 280s ] thds: 16 tps: 428.00 qps: 428.00 (r/w/o: 0.00/421.60/6.40) lat (ms,95%): 65.65 err/s: 0.00 reconn/s: 0.00
[ 290s ] thds: 16 tps: 977.20 qps: 977.20 (r/w/o: 0.00/962.10/15.10) lat (ms,95%): 48.34 err/s: 0.00 reconn/s: 0.00
[ 300s ] thds: 16 tps: 1220.20 qps: 1220.20 (r/w/o: 0.00/1204.20/16.00) lat (ms,95%): 20.74 err/s: 0.00 reconn/s: 0.00
[ 310s ] thds: 16 tps: 1046.10 qps: 1046.10 (r/w/o: 0.00/1029.10/17.00) lat (ms,95%): 33.72 err/s: 0.00 reconn/s: 0.00
[ 320s ] thds: 16 tps: 1142.10 qps: 1142.10 (r/w/o: 0.00/1125.80/16.30) lat (ms,95%): 23.52 err/s: 0.00 reconn/s: 0.00
[ 330s ] thds: 16 tps: 1060.20 qps: 1060.20 (r/w/o: 0.00/1043.00/17.20) lat (ms,95%): 28.67 err/s: 0.00 reconn/s: 0.00
[ 340s ] thds: 16 tps: 978.80 qps: 978.80 (r/w/o: 0.00/964.00/14.80) lat (ms,95%): 28.16 err/s: 0.00 reconn/s: 0.00
[ 350s ] thds: 16 tps: 431.20 qps: 431.20 (r/w/o: 0.00/425.70/5.50) lat (ms,95%): 66.84 err/s: 0.00 reconn/s: 0.00
[ 360s ] thds: 16 tps: 463.00 qps: 463.00 (r/w/o: 0.00/456.10/6.90) lat (ms,95%): 59.99 err/s: 0.00 reconn/s: 0.00
[ 370s ] thds: 16 tps: 626.80 qps: 626.80 (r/w/o: 0.00/617.30/9.50) lat (ms,95%): 62.19 err/s: 0.00 reconn/s: 0.00
[ 380s ] thds: 16 tps: 537.60 qps: 537.60 (r/w/o: 0.00/530.50/7.10) lat (ms,95%): 52.89 err/s: 0.00 reconn/s: 0.00
[ 390s ] thds: 16 tps: 321.30 qps: 321.30 (r/w/o: 0.00/317.00/4.30) lat (ms,95%): 87.56 err/s: 0.00 reconn/s: 0.00
[ 400s ] thds: 16 tps: 392.70 qps: 392.70 (r/w/o: 0.00/387.20/5.50) lat (ms,95%): 77.19 err/s: 0.00 reconn/s: 0.00
[ 410s ] thds: 16 tps: 541.70 qps: 541.70 (r/w/o: 0.00/532.10/9.60) lat (ms,95%): 75.82 err/s: 0.00 reconn/s: 0.00
[ 420s ] thds: 16 tps: 1165.00 qps: 1165.00 (r/w/o: 0.00/1151.70/13.30) lat (ms,95%): 22.28 err/s: 0.00 reconn/s: 0.00
[ 430s ] thds: 16 tps: 982.70 qps: 982.70 (r/w/o: 0.00/969.50/13.20) lat (ms,95%): 27.17 err/s: 0.00 reconn/s: 0.00
[ 440s ] thds: 16 tps: 418.60 qps: 418.60 (r/w/o: 0.00/412.90/5.70) lat (ms,95%): 66.84 err/s: 0.00 reconn/s: 0.00
[ 450s ] thds: 16 tps: 535.70 qps: 535.70 (r/w/o: 0.00/528.40/7.30) lat (ms,95%): 66.84 err/s: 0.00 reconn/s: 0.00
[ 460s ] thds: 16 tps: 1196.90 qps: 1196.90 (r/w/o: 0.00/1181.80/15.10) lat (ms,95%): 24.38 err/s: 0.00 reconn/s: 0.00
[ 470s ] thds: 16 tps: 1466.39 qps: 1466.39 (r/w/o: 0.00/1446.79/19.60) lat (ms,95%): 14.46 err/s: 0.00 reconn/s: 0.00
[ 480s ] thds: 16 tps: 1474.70 qps: 1474.70 (r/w/o: 0.00/1451.10/23.60) lat (ms,95%): 13.95 err/s: 0.00 reconn/s: 0.00
[ 490s ] thds: 16 tps: 1471.00 qps: 1471.00 (r/w/o: 0.00/1449.30/21.70) lat (ms,95%): 13.95 err/s: 0.00 reconn/s: 0.00
[ 500s ] thds: 16 tps: 1162.40 qps: 1162.40 (r/w/o: 0.00/1145.90/16.50) lat (ms,95%): 21.50 err/s: 0.00 reconn/s: 0.00
[ 510s ] thds: 16 tps: 1298.89 qps: 1298.89 (r/w/o: 0.00/1280.49/18.40) lat (ms,95%): 19.29 err/s: 0.00 reconn/s: 0.00
[ 520s ] thds: 16 tps: 1405.10 qps: 1405.10 (r/w/o: 0.00/1386.10/19.00) lat (ms,95%): 16.12 err/s: 0.00 reconn/s: 0.00
[ 530s ] thds: 16 tps: 1500.71 qps: 1500.71 (r/w/o: 0.00/1478.01/22.70) lat (ms,95%): 12.75 err/s: 0.00 reconn/s: 0.00
[ 540s ] thds: 16 tps: 1531.10 qps: 1531.10 (r/w/o: 0.00/1508.70/22.40) lat (ms,95%): 12.52 err/s: 0.00 reconn/s: 0.00
[ 550s ] thds: 16 tps: 1433.40 qps: 1433.40 (r/w/o: 0.00/1414.50/18.90) lat (ms,95%): 15.55 err/s: 0.00 reconn/s: 0.00
[ 560s ] thds: 16 tps: 1421.70 qps: 1421.70 (r/w/o: 0.00/1400.50/21.20) lat (ms,95%): 15.83 err/s: 0.00 reconn/s: 0.00
[ 570s ] thds: 16 tps: 1441.80 qps: 1441.80 (r/w/o: 0.00/1419.50/22.30) lat (ms,95%): 13.95 err/s: 0.00 reconn/s: 0.00
[ 580s ] thds: 16 tps: 1381.40 qps: 1381.40 (r/w/o: 0.00/1361.70/19.70) lat (ms,95%): 17.63 err/s: 0.00 reconn/s: 0.00
[ 590s ] thds: 16 tps: 1482.90 qps: 1482.90 (r/w/o: 0.00/1463.20/19.70) lat (ms,95%): 13.46 err/s: 0.00 reconn/s: 0.00
[ 600s ] thds: 16 tps: 1431.09 qps: 1431.09 (r/w/o: 0.00/1408.29/22.80) lat (ms,95%): 14.73 err/s: 0.00 reconn/s: 0.00
SQL statistics:
    queries performed:
        read:                            0
        write:                           646946
        other:                           9567
        total:                           656513
    transactions:                        656513 (1094.17 per sec.)
    queries:                             656513 (1094.17 per sec.)
    ignored errors:                      0      (0.00 per sec.)
    reconnects:                          0      (0.00 per sec.)

Throughput:
    events/s (eps):                      1094.1653
    time elapsed:                        600.0126s
    total number of events:              656513

Latency (ms):
         min:                                    5.53
         avg:                                   14.62
         max:                                  187.25
         95th percentile:                       31.94
         sum:                              9599726.80

Threads fairness:
    events (avg/stddev):           41032.0625/778.74
    execution time (avg/stddev):   599.9829/0.01
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

[ 10s ] thds: 16 tps: 81.68 qps: 1324.33 (r/w/o: 1159.37/0.00/164.97) lat (ms,95%): 292.60 err/s: 0.00 reconn/s: 0.00
[ 20s ] thds: 16 tps: 76.90 qps: 1222.83 (r/w/o: 1069.12/0.00/153.70) lat (ms,95%): 314.45 err/s: 0.00 reconn/s: 0.00
[ 30s ] thds: 16 tps: 78.80 qps: 1262.81 (r/w/o: 1105.21/0.00/157.60) lat (ms,95%): 308.84 err/s: 0.00 reconn/s: 0.00
[ 40s ] thds: 16 tps: 44.90 qps: 717.80 (r/w/o: 627.90/0.00/89.90) lat (ms,95%): 646.19 err/s: 0.00 reconn/s: 0.00
[ 50s ] thds: 16 tps: 64.60 qps: 1033.20 (r/w/o: 904.20/0.00/129.00) lat (ms,95%): 411.96 err/s: 0.00 reconn/s: 0.00
[ 60s ] thds: 16 tps: 88.80 qps: 1419.70 (r/w/o: 1241.90/0.00/177.80) lat (ms,95%): 257.95 err/s: 0.00 reconn/s: 0.00
[ 70s ] thds: 16 tps: 87.30 qps: 1402.20 (r/w/o: 1227.80/0.00/174.40) lat (ms,95%): 262.64 err/s: 0.00 reconn/s: 0.00
[ 80s ] thds: 16 tps: 73.10 qps: 1164.90 (r/w/o: 1018.50/0.00/146.40) lat (ms,95%): 344.08 err/s: 0.00 reconn/s: 0.00
[ 90s ] thds: 16 tps: 83.20 qps: 1335.89 (r/w/o: 1169.49/0.00/166.40) lat (ms,95%): 240.02 err/s: 0.00 reconn/s: 0.00
[ 100s ] thds: 16 tps: 69.10 qps: 1104.71 (r/w/o: 966.61/0.00/138.10) lat (ms,95%): 458.96 err/s: 0.00 reconn/s: 0.00
[ 110s ] thds: 16 tps: 90.30 qps: 1446.20 (r/w/o: 1265.60/0.00/180.60) lat (ms,95%): 223.34 err/s: 0.00 reconn/s: 0.00
[ 120s ] thds: 16 tps: 72.00 qps: 1149.90 (r/w/o: 1005.80/0.00/144.10) lat (ms,95%): 314.45 err/s: 0.00 reconn/s: 0.00
[ 130s ] thds: 16 tps: 24.00 qps: 378.40 (r/w/o: 330.50/0.00/47.90) lat (ms,95%): 1032.01 err/s: 0.00 reconn/s: 0.00
[ 140s ] thds: 16 tps: 14.20 qps: 223.00 (r/w/o: 195.30/0.00/27.70) lat (ms,95%): 1561.52 err/s: 0.00 reconn/s: 0.00
[ 150s ] thds: 16 tps: 13.00 qps: 209.90 (r/w/o: 183.10/0.00/26.80) lat (ms,95%): 1739.68 err/s: 0.00 reconn/s: 0.00
[ 160s ] thds: 16 tps: 14.40 qps: 237.50 (r/w/o: 208.70/0.00/28.80) lat (ms,95%): 1506.29 err/s: 0.00 reconn/s: 0.00
[ 170s ] thds: 16 tps: 17.60 qps: 275.10 (r/w/o: 239.90/0.00/35.20) lat (ms,95%): 1771.29 err/s: 0.00 reconn/s: 0.00
[ 180s ] thds: 16 tps: 51.70 qps: 838.10 (r/w/o: 734.70/0.00/103.40) lat (ms,95%): 759.88 err/s: 0.00 reconn/s: 0.00
[ 190s ] thds: 16 tps: 65.80 qps: 1050.90 (r/w/o: 919.30/0.00/131.60) lat (ms,95%): 363.18 err/s: 0.00 reconn/s: 0.00
[ 200s ] thds: 16 tps: 72.90 qps: 1166.40 (r/w/o: 1020.80/0.00/145.60) lat (ms,95%): 350.33 err/s: 0.00 reconn/s: 0.00
[ 210s ] thds: 16 tps: 80.10 qps: 1282.20 (r/w/o: 1121.90/0.00/160.30) lat (ms,95%): 325.98 err/s: 0.00 reconn/s: 0.00
[ 220s ] thds: 16 tps: 66.10 qps: 1057.80 (r/w/o: 925.50/0.00/132.30) lat (ms,95%): 376.49 err/s: 0.00 reconn/s: 0.00
[ 230s ] thds: 16 tps: 44.50 qps: 711.80 (r/w/o: 622.80/0.00/89.00) lat (ms,95%): 733.00 err/s: 0.00 reconn/s: 0.00
[ 240s ] thds: 16 tps: 35.20 qps: 560.00 (r/w/o: 489.60/0.00/70.40) lat (ms,95%): 746.32 err/s: 0.00 reconn/s: 0.00
[ 250s ] thds: 16 tps: 73.60 qps: 1175.90 (r/w/o: 1028.90/0.00/147.00) lat (ms,95%): 363.18 err/s: 0.00 reconn/s: 0.00
[ 260s ] thds: 16 tps: 87.10 qps: 1396.10 (r/w/o: 1221.70/0.00/174.40) lat (ms,95%): 244.38 err/s: 0.00 reconn/s: 0.00
[ 270s ] thds: 16 tps: 49.10 qps: 786.40 (r/w/o: 688.40/0.00/98.00) lat (ms,95%): 816.63 err/s: 0.00 reconn/s: 0.00
[ 280s ] thds: 16 tps: 18.00 qps: 288.60 (r/w/o: 252.40/0.00/36.20) lat (ms,95%): 1258.08 err/s: 0.00 reconn/s: 0.00
[ 290s ] thds: 16 tps: 23.60 qps: 378.40 (r/w/o: 331.20/0.00/47.20) lat (ms,95%): 1069.86 err/s: 0.00 reconn/s: 0.00
[ 300s ] thds: 16 tps: 40.20 qps: 641.89 (r/w/o: 561.60/0.00/80.30) lat (ms,95%): 590.56 err/s: 0.00 reconn/s: 0.00
[ 310s ] thds: 16 tps: 27.30 qps: 433.60 (r/w/o: 379.10/0.00/54.50) lat (ms,95%): 1170.65 err/s: 0.00 reconn/s: 0.00
[ 320s ] thds: 16 tps: 16.90 qps: 277.50 (r/w/o: 243.50/0.00/34.00) lat (ms,95%): 1427.08 err/s: 0.00 reconn/s: 0.00
[ 330s ] thds: 16 tps: 37.70 qps: 599.70 (r/w/o: 524.30/0.00/75.40) lat (ms,95%): 1129.24 err/s: 0.00 reconn/s: 0.00
[ 340s ] thds: 16 tps: 71.10 qps: 1136.00 (r/w/o: 993.80/0.00/142.20) lat (ms,95%): 434.83 err/s: 0.00 reconn/s: 0.00
[ 350s ] thds: 16 tps: 95.70 qps: 1529.20 (r/w/o: 1337.90/0.00/191.30) lat (ms,95%): 189.93 err/s: 0.00 reconn/s: 0.00
[ 360s ] thds: 16 tps: 80.90 qps: 1295.90 (r/w/o: 1134.00/0.00/161.90) lat (ms,95%): 539.71 err/s: 0.00 reconn/s: 0.00
[ 370s ] thds: 16 tps: 98.60 qps: 1579.39 (r/w/o: 1382.19/0.00/197.20) lat (ms,95%): 173.58 err/s: 0.00 reconn/s: 0.00
[ 380s ] thds: 16 tps: 96.70 qps: 1547.61 (r/w/o: 1354.41/0.00/193.20) lat (ms,95%): 183.21 err/s: 0.00 reconn/s: 0.00
[ 390s ] thds: 16 tps: 75.40 qps: 1204.30 (r/w/o: 1053.40/0.00/150.90) lat (ms,95%): 475.79 err/s: 0.00 reconn/s: 0.00
[ 400s ] thds: 16 tps: 93.20 qps: 1492.10 (r/w/o: 1305.60/0.00/186.50) lat (ms,95%): 189.93 err/s: 0.00 reconn/s: 0.00
[ 410s ] thds: 16 tps: 90.40 qps: 1444.60 (r/w/o: 1263.80/0.00/180.80) lat (ms,95%): 215.44 err/s: 0.00 reconn/s: 0.00
[ 420s ] thds: 16 tps: 95.00 qps: 1516.91 (r/w/o: 1327.10/0.00/189.80) lat (ms,95%): 196.89 err/s: 0.00 reconn/s: 0.00
[ 430s ] thds: 16 tps: 93.20 qps: 1492.80 (r/w/o: 1306.40/0.00/186.40) lat (ms,95%): 189.93 err/s: 0.00 reconn/s: 0.00
[ 440s ] thds: 16 tps: 97.30 qps: 1557.10 (r/w/o: 1362.40/0.00/194.70) lat (ms,95%): 179.94 err/s: 0.00 reconn/s: 0.00
[ 450s ] thds: 16 tps: 96.60 qps: 1546.70 (r/w/o: 1353.50/0.00/193.20) lat (ms,95%): 179.94 err/s: 0.00 reconn/s: 0.00
[ 460s ] thds: 16 tps: 98.50 qps: 1577.50 (r/w/o: 1380.40/0.00/197.10) lat (ms,95%): 176.73 err/s: 0.00 reconn/s: 0.00
[ 470s ] thds: 16 tps: 99.50 qps: 1592.79 (r/w/o: 1393.89/0.00/198.90) lat (ms,95%): 170.48 err/s: 0.00 reconn/s: 0.00
[ 480s ] thds: 16 tps: 99.60 qps: 1594.20 (r/w/o: 1394.90/0.00/199.30) lat (ms,95%): 173.58 err/s: 0.00 reconn/s: 0.00
[ 490s ] thds: 16 tps: 99.90 qps: 1599.09 (r/w/o: 1399.39/0.00/199.70) lat (ms,95%): 170.48 err/s: 0.00 reconn/s: 0.00
[ 500s ] thds: 16 tps: 98.80 qps: 1580.92 (r/w/o: 1383.21/0.00/197.70) lat (ms,95%): 179.94 err/s: 0.00 reconn/s: 0.00
[ 510s ] thds: 16 tps: 98.90 qps: 1580.89 (r/w/o: 1383.09/0.00/197.80) lat (ms,95%): 176.73 err/s: 0.00 reconn/s: 0.00
[ 520s ] thds: 16 tps: 94.90 qps: 1516.21 (r/w/o: 1326.51/0.00/189.70) lat (ms,95%): 240.02 err/s: 0.00 reconn/s: 0.00
[ 530s ] thds: 16 tps: 97.90 qps: 1566.30 (r/w/o: 1370.50/0.00/195.80) lat (ms,95%): 179.94 err/s: 0.00 reconn/s: 0.00
[ 540s ] thds: 16 tps: 94.50 qps: 1515.41 (r/w/o: 1326.31/0.00/189.10) lat (ms,95%): 183.21 err/s: 0.00 reconn/s: 0.00
[ 550s ] thds: 16 tps: 98.00 qps: 1567.79 (r/w/o: 1371.79/0.00/196.00) lat (ms,95%): 183.21 err/s: 0.00 reconn/s: 0.00
[ 560s ] thds: 16 tps: 99.20 qps: 1583.60 (r/w/o: 1385.20/0.00/198.40) lat (ms,95%): 170.48 err/s: 0.00 reconn/s: 0.00
[ 570s ] thds: 16 tps: 96.90 qps: 1550.10 (r/w/o: 1356.40/0.00/193.70) lat (ms,95%): 179.94 err/s: 0.00 reconn/s: 0.00
[ 580s ] thds: 16 tps: 95.90 qps: 1536.00 (r/w/o: 1344.20/0.00/191.80) lat (ms,95%): 189.93 err/s: 0.00 reconn/s: 0.00
[ 590s ] thds: 16 tps: 95.30 qps: 1524.80 (r/w/o: 1334.30/0.00/190.50) lat (ms,95%): 193.38 err/s: 0.00 reconn/s: 0.00
[ 600s ] thds: 16 tps: 96.10 qps: 1537.70 (r/w/o: 1345.30/0.00/192.40) lat (ms,95%): 183.21 err/s: 0.00 reconn/s: 0.00
SQL statistics:
    queries performed:
        read:                            606662
        write:                           0
        other:                           86666
        total:                           693328
    transactions:                        43333  (72.20 per sec.)
    queries:                             693328 (1155.27 per sec.)
    ignored errors:                      0      (0.00 per sec.)
    reconnects:                          0      (0.00 per sec.)

Throughput:
    events/s (eps):                      72.2042
    time elapsed:                        600.1454s
    total number of events:              43333

Latency (ms):
         min:                                  141.79
         avg:                                  221.57
         max:                                 2018.17
         95th percentile:                      511.33
         sum:                              9601205.04

Threads fairness:
    events (avg/stddev):           2708.3125/26.93
    execution time (avg/stddev):   600.0753/0.05
```