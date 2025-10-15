import logging
import sys
import uuid
from pathlib import Path
from loguru import logger
import json

class InterceptHandler(logging.Handler):
    loglevel_mapping = {
        50: 'CRITICAL',
        40: 'ERROR',
        30: 'WARNING',
        20: 'INFO',
        10: 'DEBUG',
        0: 'NOTSET',
    }
    def emit(self, record):
        try:
            level = logger.level(record.levelname).name
        except AttributeError:
            level = self.loglevel_mapping[record.levelno]

        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        log = logger.bind(request_id=str(uuid.uuid4()))
        log.opt(
            depth=depth,
            exception=record.exc_info
        ).log(level,record.getMessage())


class CustomizeLogger:
    @classmethod
    def make_logger(cls, config_path: Path = None):
        logging_config = None
        if config_path:
            config = cls.load_logging_config(config_path)
            if config:
                logging_config = config.get('logger')

        logger = cls.customize_logging(
            logging_config.get('path') if logging_config else '',
            level=logging_config.get('level') if logging_config else 'info',
            retention=logging_config.get('retention') if logging_config else '1 months',
            rotation=logging_config.get('rotation') if logging_config else '20 days',
            format=logging_config.get('format') if logging_config else '<level>{level: <8}</level> <green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> request id: {extra[request_id]} - <cyan>{name}</cyan>:<cyan>{function}</cyan> - <level>{message}</level>',
        )
        return logger

    @classmethod
    def customize_logging(cls,
            filepath: Path,
            level: str,
            rotation: str,
            retention: str,
            format: str
    ):

        logger.remove()
        logger.add(
            sys.stdout,
            enqueue=True,
            backtrace=True,
            level=level.upper(),
            format=format
        )
        # logger.add(
        #     str(filepath),
        #     rotation=rotation,
        #     retention=retention,
        #     enqueue=True,
        #     backtrace=True,
        #     level=level.upper(),
        #     format=format
        # )
        logging.basicConfig(handlers=[InterceptHandler()], level=0)
        logging.getLogger("uvicorn.access").handlers = [InterceptHandler()]
        for _log in ['uvicorn',
                     'uvicorn.error',
                     'fastapi',
                     'httpx'
                     ]:
            _logger = logging.getLogger(_log)
            _logger.handlers = [InterceptHandler()]

        return logger.bind(request_id=str(uuid.uuid4()), method=None)


    @classmethod
    def load_logging_config(cls, config_path):
        config = None
        with open(config_path) as config_file:
            config = json.load(config_file)
        return config