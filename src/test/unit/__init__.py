import logging.config
'''
Logging setup.
'''
logging.config.fileConfig('logging.conf')
logger = logging.getLogger('test.unit')
logger.info('Logging configured')