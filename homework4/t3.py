"""import different modules"""
import configparser
import json
import psutil
import datetime
import time

CONFIG = configparser.ConfigParser()
CONFIG.read('conf.ini')
OUTPUT_TYPE = CONFIG['COMMON']['output']
INTERVAL = int(CONFIG['COMMON']['interval'])

GET_DATE = datetime.datetime.now()


class Monitoring:
    """Class to collect init information"""

    def __init__(self, cpu_load, mem_usage, vir_mem_usage, io_info_disk_usage, io_info_read_count,
                 io_info_write_count, net_info_byte_rec, net_info_byte_sent, snap_number):
        self.cpu_load = cpu_load
        self.mem_usage = mem_usage
        self.vir_mem_usage = vir_mem_usage
        self.io_info_disk_usage = io_info_disk_usage
        self.io_info_read_count = io_info_read_count
        self.io_info_write_count = io_info_write_count
        self.net_info_byte_rec = net_info_byte_rec
        self.net_info_byte_sent = net_info_byte_sent
        self.snap_number = snap_number

    def output_parameters(self, date, out_type):
        """save system snapshot to file"""
        if out_type == "json":
            output = {"SNAPSHOT {0} : TIMESTAMP: {2}:{1} {3}.{4}.{5} ".format(getattr(self, 'snap_number'), date.minute,
                                                                              date.hour, date.day,
                                                                              date.month, date.year): {
                'Overall CPU load': getattr(self, 'cpu_load'),
                'Overall memory usage': getattr(self, 'mem_usage'),
                'Overall virtual memory usage': getattr(self, 'vir_mem_usage'),
                'IO information': [{'Disk usage': getattr(self, 'io_info_disk_usage'),
                                   'Read count': getattr(self, 'io_info_read_count'),
                                   'Write count': getattr(self, 'io_info_write_count')}],
                'Network information': [{'Bytes receive': getattr(self, 'net_info_byte_rec'),
                                        'Bytes sent': getattr(self, 'net_info_byte_sent')}],

            }}
            CONFIG['COMMON']['snapshot'] = str(getattr(self, 'snap_number')+1)
            with open('conf.ini', 'w') as configfile:
                CONFIG.write(configfile)
            with open("result.json", "a") as data:
                data.write(json.dumps(output))
                data.write('\n')
                data.close()


while True:
    monitor = Monitoring(
        psutil.cpu_percent(interval=1),
        psutil.virtual_memory().percent,
        psutil.swap_memory().percent,
        psutil.disk_usage('/').percent,
        psutil.disk_io_counters(perdisk=False).read_count,
        psutil.disk_io_counters(perdisk=False).write_count,
        psutil.net_io_counters(pernic=False).bytes_recv,
        psutil.net_io_counters(pernic=False).bytes_sent,
        int(CONFIG['COMMON']['snapshot'])
    )
    Monitoring.output_parameters(monitor, GET_DATE, OUTPUT_TYPE)
    print(int(CONFIG['COMMON']['snapshot']))
    time.sleep(INTERVAL * 2)



