from abc import ABCMeta
from datetime import datetime, timedelta
from enum import Enum
from typing import Any, TypedDict

from pydantic import BaseModel, Field
from typing_extensions import NotRequired


class EventDict(TypedDict):
    start: datetime
    end: datetime
    duration: timedelta
    freq: "Frequency"
    stl_period: NotRequired[int]


class IEntity(metaclass=ABCMeta):
    def __init__(self, entity_id: str) -> None:
        self.id = entity_id

    def __hash__(self) -> int:
        return hash(self.id)

    def __eq__(self, obj: object) -> bool:
        if isinstance(obj, IEntity):
            return self.id == obj.id
        return False


class Gender(str, Enum):
    MALE = "male"
    FEMALE = "female"


class UserAccount(IEntity):
    def __init__(
        self,
        entity_id: str,
        user_id: int,
        birth_date: datetime,
        gender: Gender,
        **kwargs: Any  # We only include fields we actually use
    ) -> None:
        super().__init__(entity_id)
        self.user_id = user_id
        self.birth_date = birth_date
        self.gender = gender


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


class RecurrenceRule(IEntity):
    def __init__(
        self,
        entity_id: str,
        freq: Frequency,
        **kwargs: Any  # We only include fields we actually use
    ) -> None:
        super().__init__(entity_id)
        self.freq = freq


class Recurrence(IEntity):
    def __init__(
        self,
        entity_id: str,
        rrule: RecurrenceRule,
        **kwargs: Any  # We only include fields we actually use
    ) -> None:
        super().__init__(entity_id)
        self.rrule = rrule


class Event(IEntity):
    def __init__(
        self,
        entity_id: str,
        user_id: int,
        start: datetime,
        end: datetime,
        timezone: str,
        recurrence: Recurrence | None,
        **kwargs: Any  # We only include fields we actually use
    ) -> None:
        super().__init__(entity_id)
        self.user_id = user_id
        self.start = start
        self.end = end
        self.timezone = timezone
        assert recurrence is not None
        self.recurrence = recurrence


class EventAttendanceActionLog(IEntity):
    def __init__(
        self,
        entity_id: str,
        user_id: int,
        event_id: str,
        start: datetime,
        action: AttendanceAction,
        acted_at: datetime,
        **kwargs: Any  # We only include fields we actually use
    ) -> None:
        super().__init__(entity_id)
        self.user_id = user_id
        self.event_id = event_id
        self.start = start
        self.action = action
        self.acted_at = acted_at


class AttendanceTimeForecast(BaseModel):
    start: datetime = Field(..., title="Event Started At")
    attended_at: datetime = Field(..., title="Attended At")
    duration: float = Field(..., title="Attendance Duration")


class ForecastAttendanceTimeResponse(BaseModel):
    error_codes: list[int] = Field(..., title="Error Codes")
    attendance_time_forecasts: dict[int, dict[str, list[AttendanceTimeForecast]]] = (
        Field(..., title="Attendance Time Forecasts")
    )
