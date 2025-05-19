from datetime import datetime

from pydantic import BaseModel

from ta_ml.features.event import AttendanceAction, Frequency


class RecurrenceRule(BaseModel):
    id: str
    freq: Frequency


class Recurrence(BaseModel):
    id: str
    rrule: RecurrenceRule


class Event(BaseModel):
    id: str
    user_id: int
    start: datetime
    end: datetime
    timezone: str
    recurrence: Recurrence


class EventAttendanceActionLog(BaseModel):
    id: str
    user_id: int
    event_id: str
    start: datetime
    action: AttendanceAction
    acted_at: datetime
