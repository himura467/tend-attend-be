from datetime import datetime

from ta_ml.domain.entities.base import IEntity
from ta_ml.features.account import Gender


class UserAccount(IEntity):
    def __init__(
        self,
        entity_id: str,
        user_id: int,
        birth_date: datetime,
        gender: Gender,
    ) -> None:
        super().__init__(entity_id)
        self.user_id = user_id
        self.birth_date = birth_date
        self.gender = gender
