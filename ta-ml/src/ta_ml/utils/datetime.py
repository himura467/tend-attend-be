from datetime import datetime
from zoneinfo import ZoneInfo


def apply_timezone(date_value: datetime, timezone: str) -> datetime:
    return date_value.astimezone(ZoneInfo(timezone))
