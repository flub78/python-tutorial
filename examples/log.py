#!/usr/bin/python
# -*- coding:utf8 -*
#
# Logging in Python
# https://docs.python.org/2/howto/logging.html

import logging

print "Experiment on logging"

logger = logging.getLogger("memory access")
logger.info("System has 2Gb of memory")

# configuration of the default logger must be done before to use it.
# If not the configuration is not taken into account
logging.basicConfig(filename='example.log',level=logging.DEBUG)


logging.error('Logging of an error on default logger')

# by default info level is not enabled
# logging.info('Nothing serious')

logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')

print "bye"

