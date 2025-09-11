from logtail import LogtailHandler
import logging

SOURCE_TOKEN = "7jRV5jWRw7nWSVLxXgfWBKvA"
HOST = "s1516029.eu-nbg-2.betterstackdata.com"


def get_logger():
    handler = LogtailHandler(
        source_token=SOURCE_TOKEN,
        host=f'https://{HOST}',
    )
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.ERROR)
    logger.handlers = []
    logger.addHandler(handler)
    return logger


logger = get_logger()

logger.info("some into log", extra={"user_id": 1354})
logger.error("some error log")
