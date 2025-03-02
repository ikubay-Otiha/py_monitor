from datetime import datetime

from fastapi import APIRouter

from src.lib.models import LogResponse
from src.lib.utils import get_env_files

router = APIRouter()


@router.get("/log", response_model=LogResponse | None)
def read_logs():
    try:
        log_file_path = get_env_files()
        with open(log_file_path) as f:
            lines = f.readlines()
            if not lines:
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
            return res

    except FileNotFoundError:
        return {"error": "Log file not found"}

    except (ValueError, IndexError):
        return {"error": "Invalid log format"}
