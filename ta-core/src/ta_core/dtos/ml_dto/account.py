from datetime import datetime

from pydantic import BaseModel, field_serializer

from ta_core.features.account import Gender


class UserAccount(BaseModel):
    id: str
    user_id: int
    birth_date: datetime
    gender: Gender

    @field_serializer("birth_date")
    def serialize_birth_date(self, birth_date: datetime) -> str:
        return birth_date.isoformat()
