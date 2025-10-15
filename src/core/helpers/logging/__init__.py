import logging

from src.core.helpers.logging.custom_logging import CustomizeLogger

logger = logging.getLogger(__name__)
logger = CustomizeLogger.make_logger()
