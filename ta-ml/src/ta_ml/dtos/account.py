from datetime import datetime

from pydantic import BaseModel

from ta_ml.features.account import Gender


class UserAccount(BaseModel):
    id: str
    user_id: int
    birth_date: datetime
    gender: Gender
