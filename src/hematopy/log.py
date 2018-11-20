import os
import logging
import logging.handlers


SEMATEXT_API_TOKEN = os.environ.get('SEMATEXT_API_TOKEN')

logger = logging.getLogger('hematopy-logger')
logger.setLevel(logging.INFO)

if SEMATEXT_API_TOKEN:
    sematext_format = '{}:%(message)s'.format(SEMATEXT_API_TOKEN)
    formater = logging.Formatter(sematext_format)
    handler = logging.handlers.SysLogHandler(address=('logsene-syslog-receiver.eu.sematext.com', 514))
    handler.setFormatter(formater)
    logger.addHandler(handler)
