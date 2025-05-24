from fastapi import FastAPI

from ta_ml.domain.entities.account import UserAccount as UserAccountEntity
from ta_ml.domain.entities.event import Event as EventEntity
from ta_ml.domain.entities.event import (
    EventAttendanceActionLog as EventAttendanceActionLogEntity,
)
from ta_ml.dtos.forecast import (
    ForecastAttendanceTimeRequest,
    ForecastAttendanceTimeResponse,
)
from ta_ml.forecast.attendance import forecast_attendance_time as forecast

app = FastAPI()


@app.post(
    path="/forecast/attendance",
    name="Forecast Attendance Time",
    response_model=ForecastAttendanceTimeResponse,
)
async def forecast_attendance_time(
    req: ForecastAttendanceTimeRequest,
) -> ForecastAttendanceTimeResponse:
    return forecast(
        earliest_attend_data={
            EventAttendanceActionLogEntity(**log.model_dump())
            for log in req.earliest_attend_data
        },
        latest_leave_data={
            EventAttendanceActionLogEntity(**log.model_dump())
            for log in req.latest_leave_data
        },
        event_data={EventEntity(**event.model_dump()) for event in req.event_data},
        user_data={UserAccountEntity(**user.model_dump()) for user in req.user_data},
    )
