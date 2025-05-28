from datetime import datetime

from pydantic import BaseModel, Field

from ta_ml.features.event import AttendanceAction, Frequency


class RecurrenceRule(BaseModel):
    id: str = Field(serialization_alias="entity_id")
    freq: Frequency


class Recurrence(BaseModel):
    id: str = Field(serialization_alias="entity_id")
    rrule: RecurrenceRule


class Event(BaseModel):
    id: str = Field(serialization_alias="entity_id")
    user_id: int
    start: datetime
    end: datetime
    timezone: str
    recurrence: Recurrence


class EventAttendanceActionLog(BaseModel):
    id: str = Field(serialization_alias="entity_id")
    user_id: int
    event_id: str
    start: datetime
    action: AttendanceAction
    acted_at: datetime
