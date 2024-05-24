import sys
import logging
import ecs_logging


def init_es_log(level):
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(ecs_logging.StdlibFormatter(exclude_fields=(
        "ecs",
        "process",
        "log.original",
    )))

    logging.basicConfig(handlers=[handler], level=level)
