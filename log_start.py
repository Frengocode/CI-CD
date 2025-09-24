import logging
from datetime import datetime, UTC
import uuid


logging.basicConfig(level=logging.DEBUG)
log: logging.Logger = logging.getLogger(__name__)


""" Log Application when application was started """


def log_app_started() -> None:

    app_id: str = str(uuid.uuid1(node=1000, clock_seq=1))
    today_datetime = datetime.now(UTC)
    log.info("Starting application [INFO %s] [DATE %s]", app_id, today_datetime)


if __name__ == "__main__":
    log_app_started()
