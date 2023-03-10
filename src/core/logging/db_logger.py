import logging
from ..models import Log
from ..db import DbService


class DbHandler(logging.Handler):
    def __init__(self):
        super().__init__()

    def emit(self, record):
        log = Log(timestamp=record.asctime.replace(',', '.'),
                  feature=record.feature,
                  level=record.levelname,
                  message=record.message)
        db = DbService()
        db.save(log)
