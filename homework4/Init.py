import configparser

CONFIG = configparser.ConfigParser()
CONFIG.read('conf.ini')


class Initial:
    """class to collect info from conf.ini file"""

    def __init__(self):
        self.output = CONFIG['COMMON']['output']
        self.interval = CONFIG['COMMON']['interval']
        self.snapshot = CONFIG['COMMON']['snapshot']

    def change_conf(self):
        CONFIG['COMMON']['output'] = getattr(self, 'output')
        CONFIG['COMMON']['interval'] = getattr(self, 'interval')
        CONFIG['COMMON']['snapshot'] = getattr(self, 'snapshot')
        with open('conf.ini', 'w') as configfile:
            CONFIG.write(configfile)
