import logging

class DebugInfoLogFilter(logging.Filter):

    def filter(self, record: logging.LogRecord) -> bool:
        return record.levelname in ('DEBUG', 'INFO')

class WarningErrorCritical(logging.Filter):

    def filter(self, record: logging.LogRecord) -> bool:
        return record.levelname in ('WARNING', 'ERROR', 'CRITICAL')
