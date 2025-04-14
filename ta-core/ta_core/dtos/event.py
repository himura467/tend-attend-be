from datetime import datetime

from pydantic import BaseModel
from pydantic.fields import Field

from ta_core.dtos.base import BaseModelWithErrorCodes
from ta_core.features.event import AttendanceAction


class Event(BaseModel):
    summary: str = Field(..., title="Summary")
    location: str | None = Field(None, title="Location")
    start: datetime = Field(..., title="Start")
    end: datetime = Field(..., title="End")
    is_all_day: bool = Field(True, title="Is All Day")
    recurrence_list: list[str] = Field(..., title="Recurrence List")
    timezone: str = Field(..., title="Timezone")


class EventWithId(Event):
    id: str = Field(..., title="Event ID")


class Attendance(BaseModel):
    action: AttendanceAction = Field(..., title="Attendance Action")
    acted_at: datetime = Field(..., title="Acted At")


class AttendanceTime(BaseModel):
    start: datetime = Field(..., title="Event Started At")
    attended_at: datetime = Field(..., title="Attended At")
    duration: float = Field(..., title="Attendance Duration")


class CreateEventRequest(BaseModel):
    event: Event = Field(..., title="Event")


class CreateEventResponse(BaseModelWithErrorCodes):
    pass


class AttendEventRequest(BaseModel):
    action: AttendanceAction = Field(..., title="Attendance Action")


class AttendEventResponse(BaseModelWithErrorCodes):
    pass


class UpdateAttendancesRequest(BaseModel):
    attendances: list[Attendance] = Field(..., title="Attendances")


class UpdateAttendancesResponse(BaseModelWithErrorCodes):
    pass


class GetAttendancesResponse(BaseModelWithErrorCodes):
    attendances: list[Attendance] = Field(..., title="Attendances")


class GetMyEventsResponse(BaseModelWithErrorCodes):
    events: list[EventWithId] = Field(..., title="My Events")


class GetFollowingEventsResponse(BaseModelWithErrorCodes):
    events: list[EventWithId] = Field(..., title="Following Events")


class GetGuestCurrentAttendanceStatusResponse(BaseModelWithErrorCodes):
    attend: bool = Field(..., title="Attend")


class ForecastAttendanceTimeResponse(BaseModelWithErrorCodes):
    attendance_time_forecasts: dict[int, dict[str, list[AttendanceTime]]] = Field(
        ..., title="Attendance Time Forecasts"
    )
