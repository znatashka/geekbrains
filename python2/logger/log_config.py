import logging

logging.basicConfig(
    filename='log.log',
    level=logging.DEBUG,
    format='%(name)-5s %(levelname)-5s %(asctime)-20s %(message)s'
)


def log_msg(module, message):
    logger = logging.getLogger(module)
    logger.debug(message)
