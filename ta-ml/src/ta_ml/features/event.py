from datetime import datetime, timedelta
from enum import Enum
from typing import TypedDict

from typing_extensions import NotRequired


class Frequency(str, Enum):
    SECONDLY = "SECONDLY"
    MINUTELY = "MINUTELY"
    HOURLY = "HOURLY"
    DAILY = "DAILY"
    WEEKLY = "WEEKLY"
    MONTHLY = "MONTHLY"
    YEARLY = "YEARLY"


class Weekday(str, Enum):
    MO = "MO"
    TU = "TU"
    WE = "WE"
    TH = "TH"
    FR = "FR"
    SA = "SA"
    SU = "SU"


class AttendanceAction(str, Enum):
    ATTEND = "attend"
    LEAVE = "leave"


class EventDict(TypedDict):
    start: datetime
    end: datetime
    duration: timedelta
    freq: Frequency
    stl_period: NotRequired[int]
