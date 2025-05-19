from datetime import datetime

from ta_ml.domain.entities.base import IEntity
from ta_ml.features.event import AttendanceAction, Frequency


class RecurrenceRule(IEntity):
    def __init__(
        self,
        entity_id: str,
        freq: Frequency,
    ) -> None:
        super().__init__(entity_id)
        self.freq = freq


class Recurrence(IEntity):
    def __init__(
        self,
        entity_id: str,
        rrule: RecurrenceRule,
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
        recurrence: Recurrence,
    ) -> None:
        super().__init__(entity_id)
        self.user_id = user_id
        self.start = start
        self.end = end
        self.timezone = timezone
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
    ) -> None:
        super().__init__(entity_id)
        self.user_id = user_id
        self.event_id = event_id
        self.start = start
        self.action = action
        self.acted_at = acted_at
