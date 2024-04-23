from pathlib import Path
import logging

def get_logger(name, level=logging.INFO):
    # create a custom logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # create handlers
    c_handler = logging.StreamHandler()
    logs_file = Path(__file__).absolute().parents[2] / "logs"
    if not logs_file.exists():
        logs_file.mkdir(parents=True, exist_ok=True)
    f_handler = logging.FileHandler(logs_file / "example.logs", encoding='utf-8')
    c_handler.setLevel(logging.INFO)
    f_handler.setLevel(logging.DEBUG)

    # create formatters and add it to handlers
    c_format = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
    f_format = logging.Formatter(
        "%(asctime)s.%(msecs)03d - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    c_handler.setFormatter(c_format)
    f_handler.setFormatter(f_format)

    # add handlers to the logger
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)

    return logger