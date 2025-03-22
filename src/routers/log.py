from datetime import datetime

from fastapi import APIRouter

from src.lib.models import LogResponse
from src.lib.utils import get_env_files, init_logger

router = APIRouter()


@router.get("/log", response_model=LogResponse | None)
def read_logs():
    logger = init_logger(__name__)

    try:
        log_file_path = get_env_files()
        with open(log_file_path) as f:
            lines = f.readlines()
            if not lines:
                logger.info(f"log_file is not found {log_file_path}")
                return None

            latest_log = lines[-1].strip()
            parts = latest_log.split(" - ")
            timestamp = datetime.strptime(parts[0], "%Y-%m-%d %H:%M:%S.%f")
            stats = parts[1].split(", ")
            cpu_percent = float(stats[0].split(": ")[1].replace("%", ""))
            mem_percent = float(stats[1].split(": ")[1].replace("%", ""))
            disk_usage = float(stats[2].split(": ")[1].replace("%", ""))
            net_io_sent = int(stats[3].split(": ")[1])
            net_io_recv = int(stats[4].split(": ")[1])
            temperature = float(stats[5].split(": ")[1])

            res = LogResponse(
                timestamp=timestamp,
                cpu_percent=cpu_percent,
                mem_percent=mem_percent,
                disk_usage=disk_usage,
                net_io_sent=net_io_sent,
                net_io_recv=net_io_recv,
                temperature=temperature,
            )
            logger.info(f"Response: {res}")
            return res

    except FileNotFoundError:
        logger.error("Log file not found")
        return {"error": "Log file not found"}

    except (ValueError, IndexError):
        logger.error("Invalid log format")
        return {"error": "Invalid log format"}
