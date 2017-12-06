"""import different modules"""
import configparser
import psutil
import datetime
import time
from Monitor import Monitoring
from Init import Initial

CONFIG = configparser.ConfigParser()
CONFIG.read('conf.ini')

GET_DATE = datetime.datetime.now()

while True:
    init = Initial()
    monitor = Monitoring(
        psutil.cpu_percent(interval=1),
        psutil.virtual_memory().percent,
        psutil.swap_memory().percent,
        psutil.disk_usage('/').percent,
        psutil.disk_io_counters(perdisk=False).read_count,
        psutil.disk_io_counters(perdisk=False).write_count,
        psutil.net_io_counters(pernic=False).bytes_recv,
        psutil.net_io_counters(pernic=False).bytes_sent,
        int(getattr(init, 'snapshot'))
    )
    setattr(init, 'snapshot', Monitoring.output_parameters(monitor, GET_DATE, getattr(init, 'output')))
    Initial.change_conf(init)
    print(getattr(init, 'snapshot'))
    time.sleep(int(getattr(init, 'interval')) * 60)



