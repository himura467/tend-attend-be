from datetime import datetime

from pydantic import BaseModel, Field

from ta_ml.dtos.account import UserAccount
from ta_ml.dtos.base import BaseModelWithErrorCodes
from ta_ml.dtos.event import Event, EventAttendanceActionLog


class ForecastAttendanceTimeRequest(BaseModel):
    earliest_attend_data: list[EventAttendanceActionLog]
    latest_leave_data: list[EventAttendanceActionLog]
    event_data: list[Event]
    user_data: list[UserAccount]


class AttendanceTimeForecast(BaseModel):
    start: datetime = Field(..., title="Event Started At")
    attended_at: datetime = Field(..., title="Attended At")
    duration: float = Field(..., title="Attendance Duration")


class ForecastAttendanceTimeResponse(BaseModelWithErrorCodes):
    attendance_time_forecasts: dict[int, dict[str, list[AttendanceTimeForecast]]] = (
        Field(..., title="Attendance Time Forecasts")
    )
