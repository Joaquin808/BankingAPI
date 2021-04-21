import logging


def log_info(statement_to_log):
    logging.basicConfig(level=logging.INFO, filename='app.log', filemode='w')

    logger = logging.getLogger(__name__)

    logger.info(statement_to_log)


def log_warning(statement_to_log):
    logging.basicConfig(level=logging.INFO, filename='app.log', filemode='w')

    logger = logging.getLogger(__name__)

    logger.warning(statement_to_log)


def log_error(statement_to_log):
    logging.basicConfig(level=logging.INFO, filename='app.log', filemode='w')

    logger = logging.getLogger(__name__)

    logger.error(statement_to_log)


def _test():
    log_info("test statement")


if __name__ == '__main__':
    _test()

