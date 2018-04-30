import logging.config
'''
Logging setup.
'''
logging.config.fileConfig('logging.conf')
logger = logging.getLogger('main')
logger.info('Logging configured')