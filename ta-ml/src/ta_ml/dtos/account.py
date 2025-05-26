from datetime import datetime

from pydantic import BaseModel, Field

from ta_ml.features.account import Gender


class UserAccount(BaseModel):
    id: str = Field(serialization_alias="entity_id")
    user_id: int
    birth_date: datetime
    gender: Gender
