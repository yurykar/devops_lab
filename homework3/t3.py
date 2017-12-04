"""import different modules"""
import datetime
import time
import json
import configparser
import psutil

CONFIG = configparser.ConfigParser()

CONFIG.read('conf.ini')
OUTPUT_TYPE = CONFIG['COMMON']['output']
INTERVAL = int(CONFIG['COMMON']['interval'])
SNAPSHOT = int(CONFIG['COMMON']['snapshot'])

GET_DATE = datetime.datetime.now()


def output_parameters(date, out_type):
    """save system snapshot to file"""
    print(out_type)
    if out_type == "json" :
        global SNAPSHOT
        output = {"SNAPSHOT {0} : TIMESTAMP: {2}:{1} {3}.{4}.{5} ".format(SNAPSHOT, date.minute, date.hour, date.day,
                                                                          date.month, date.year): {
            'Overall CPU load': psutil.cpu_percent(interval=1),
            'Overall memory usage': psutil.virtual_memory().percent,
            'Overall virtual memory usage': psutil.swap_memory().percent,
            'IO information': [{'Disk usage': psutil.disk_usage('/').percent,
                                'Read count': psutil.disk_io_counters(perdisk=False).read_count,
                                'Write count': psutil.disk_io_counters(perdisk=False).write_count}],
            'Network information': [{'Bytes receives': psutil.net_io_counters(pernic=False).bytes_recv,
                                     'Bytes sent': psutil.net_io_counters(pernic=False).bytes_sent}],

        }}
        SNAPSHOT += 1
        CONFIG['COMMON']['snapshot'] = str(SNAPSHOT)
        with open('conf.ini', 'w') as configfile:
            CONFIG.write(configfile)
        with open("result.json", "w") as data:
            data.write(json.dumps(output))
            data.close()


while True:
    output_parameters(GET_DATE, OUTPUT_TYPE)
    time.sleep(INTERVAL * 60)
