#!/bin/python3
import os
import subprocess
import time
import csv
import re
import sys

sysbench_path = os.getenv('SYSBENCH_PATH', "sysbench")
min_pow = int(os.getenv("MIN_POW", "2"))
target_pow = int(os.getenv("TARGET_POW", "8"))

benches = sys.argv
benches.pop(0)

config = {
    "mysql-host": os.getenv("MYSQL_HOST", "127.0.0.1"),
    "mysql-port": os.getenv("MYSQL_PORT", "3306"),
    "mysql-user": os.getenv("MYSQL_USER", "root"),
    "mysql-password": os.getenv("MYSQL_PASSWORD", ""),
    "mysql-db": os.getenv("MYSQL_DB", "sbtest"),
    "time": os.getenv("BENCHMARK_TIME", "600"),
    "report-interval": os.getenv("REPORT_INTERVAL", "10"),
    "db-driver": "mysql",
}

def run_bench(config, test):
    with open('config', 'w', newline='') as file: 
        config_str = ""
        for key in config.keys():
            config_str += "%s=%s\n" % (key, config[key])
        file.write(config_str)
        
    process = subprocess.Popen([sysbench_path, "--config-file=config", test,"--tables=32","--table-size=1000000","--db-ps-mode=auto","--rand-type=uniform", "run"],
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    final_data = None
    error = False
    while True:
        out = process.stdout.readline()
        if not out: break
        string = out.decode('utf-8').strip()
        if string.startswith('['): print(string)
        if string.startswith('FATAL'): 
            print("\033[91m%s\033[0m" % string) 
            error = True
        if string == "SQL statistics:": break
        
        
    if error: raise Exception("\033[91mSysbench exit with error.\033[0m")
        
    string = "".join(iter(lambda: process.stdout.readline().decode('utf-8'), ""))
    non_spaced = string.replace(' ','')
    
    total_time = float(re.findall("(?<=totaltime:)[0-9.]*",non_spaced)[0])
    
    parsed_data = {
        "tps": round(float(re.findall(r"(?<=transactions:)[0-9.]*", non_spaced)[0]) / total_time, 2),
        "qps": round(float(re.findall(r"(?<=queries:)[0-9.]*", non_spaced)[0]) / total_time, 2), 
        "qpf": {
            "read": int(re.findall(r"(?<=read:)[0-9.]*", non_spaced)[0]), 
            "write": int(re.findall(r"(?<=write:)[0-9.]*", non_spaced)[0]) ,
            "other": int(re.findall(r"(?<=other:)[0-9.]*", non_spaced)[0]), 
            "total": int(re.findall(r"(?<=total:)[0-9.]*", non_spaced)[0]),
        }, 
        "lat": float(re.findall(r"(?<=95thpercentile:)[0-9.]*", non_spaced)[0]), 
        "err": int(re.findall(r"(?<=ignorederrors:)[0-9]*", non_spaced)[0]), 
        "reconn": int(re.findall(r"(?<=reconnects:)[0-9]*", non_spaced)[0]),
        "events": float(re.findall(r"(?<=events\(avg/stddev\):)[0-9.]*", non_spaced)[0]), 
        "exectime": float(re.findall(r"(?<=executiontime\(avg/stddev\):)[0-9.]*", non_spaced)[0])
    }

    return parsed_data


if __name__ == "__main__":
    for bench in benches:
        results = []
        
        for i in range(min_pow, target_pow + 1):
            print("Benchmarking %s with %d threads..." % (bench,pow(2,i)))
            config["threads"] = str(pow(2,i))
            results.append((pow(2,i), run_bench(config, bench)))

        
        with open('results-%s.csv' % bench, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['threads','Transactions per second', 'Queries per second', 'Queries performed', 'Read queries performed','Write queries performed','Other queries performed', 'Latency(95%)', 'Ignored errors/s', 'Reconnects/s','Events(Threads fairness)', 'Execution time(Threads fairness)'])
            
            for (threads, res) in results:
                writer.writerow([threads,res["tps"], res["qps"], 
                                 res["qpf"]["total"], 
                                 res["qpf"]["read"], 
                                 res["qpf"]["write"], 
                                 res["qpf"]["other"], 
                                 res["lat"], 
                                 res["err"], 
                                 res["reconn"],
                                 res["events"],
                                 res["exectime"]])
