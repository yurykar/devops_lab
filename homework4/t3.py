"""import different modules"""
import configparser
import psutil
import datetime
import time
from Monitor import Monitoring

CONFIG = configparser.ConfigParser()
CONFIG.read('conf.ini')
OUTPUT_TYPE = CONFIG['COMMON']['output']
INTERVAL = int(CONFIG['COMMON']['interval'])
GET_DATE = datetime.datetime.now()

while True:
    SNAPSHOT = int(CONFIG['COMMON']['snapshot'])
    monitor = Monitoring(
        psutil.cpu_percent(interval=1),
        psutil.virtual_memory().percent,
        psutil.swap_memory().percent,
        psutil.disk_usage('/').percent,
        psutil.disk_io_counters(perdisk=False).read_count,
        psutil.disk_io_counters(perdisk=False).write_count,
        psutil.net_io_counters(pernic=False).bytes_recv,
        psutil.net_io_counters(pernic=False).bytes_sent,
        SNAPSHOT
    )
    CONFIG['COMMON']['snapshot'] = Monitoring.output_parameters(monitor, GET_DATE, OUTPUT_TYPE)
    with open('conf.ini', 'w') as configfile:
        CONFIG.write(configfile)
    time.sleep(INTERVAL * 60)



