import os
import datetime
import logging

import psutil


def get_temperature() -> float | str:
    try:
        with open("/sys/class/thermal/thermal_zone0/temp") as f:
            temp = int(f.read().strip()) / 1000.0  # 単位を℃へ変換
        return temp
    except FileNotFoundError:
        return "Temperature sensor not found"


def write_log_info(LOG_FILE_PATH: str):
    cpu_percent = psutil.cpu_percent(interval=1)
    mem_percent = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage("/").percent
    net_io = psutil.net_io_counters()
    temperature = get_temperature()

    log_message = f"{datetime.datetime.now()} - CPU: {cpu_percent}%,  Memory: {mem_percent}%, Disk: {disk_usage}%, Network (sent): {net_io.bytes_sent}, Network (recv): {net_io.bytes_recv}, Temperature: {temperature}\n"

    with open(LOG_FILE_PATH, "a") as f:
        f.write(log_message)


def get_env_files() -> str:
    log_file = os.getenv("LOG_FILE")
    try:
        log_file_path = os.path.join(os.getcwd(), log_file)
        return log_file_path
    except TypeError:
        return {"error": ".env file not found"}


def init_logger(name: str) -> logging.Logger:
    """initialize logger

    Args:
        name (str): _description_
    """
    # create logger handler
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # create logger handler
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)

    # create formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)

    # add handler to logger
    logger.addHandler(handler)

    logger.info("Complete logger initialization")
    return logger
