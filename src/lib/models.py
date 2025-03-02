from datetime import datetime

from pydantic import BaseModel


class LogResponse(BaseModel):
    timestamp: datetime
    cpu_percent: float
    mem_percent: float
    disk_usage: float
    net_io_sent: int
    net_io_recv: int
    temperature: float
