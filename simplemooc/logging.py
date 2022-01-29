import logging
import logging.config

class Logger:
    def __init__(self):
        logging.config.fileConfig('simplemooc/logging.conf')
        self.logger = logging.getLogger('applog')
    
    def debug(self, msg):
        self.logger.debug(msg)

    def warn(self, msg):
        self.logger.warn(msg)
    
    def info(self, msg):
        self.logger.info(msg)
    
    def error(self, msg):
        self.logger.error(msg)
    
    def critical(self, msg):
        self.logger.critical(msg)