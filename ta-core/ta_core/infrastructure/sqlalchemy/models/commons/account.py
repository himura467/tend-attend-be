from typing import List

from pydantic.networks import EmailStr
from sqlalchemy.dialects.mysql import BIGINT, VARCHAR
from sqlalchemy.exc import StatementError
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy.orm.base import Mapped
from sqlalchemy.sql.schema import ForeignKey, UniqueConstraint

from ta_core.domain.entities.account import GuestAccount as GuestAccountEntity
from ta_core.domain.entities.account import HostAccount as HostAccountEntity
from ta_core.infrastructure.sqlalchemy.models.commons.base import (
    AbstractCommonDynamicBase,
)


class HostAccount(AbstractCommonDynamicBase):
    host_name: Mapped[str] = mapped_column(
        VARCHAR(64), unique=True, nullable=False, comment="Host Name"
    )
    hashed_password: Mapped[str] = mapped_column(
        VARCHAR(512), nullable=False, comment="Hashed Password"
    )
    refresh_token: Mapped[str | None] = mapped_column(
        VARCHAR(512), nullable=True, comment="Refresh Token"
    )
    email: Mapped[EmailStr] = mapped_column(
        VARCHAR(64), unique=True, nullable=False, comment="Email Address"
    )
    user_id: Mapped[int | None] = mapped_column(
        BIGINT(unsigned=True), unique=True, nullable=True, comment="User ID"
    )
    guests: Mapped[List["GuestAccount"]] = relationship(back_populates="host", uselist=True)

    def to_entity(self) -> HostAccountEntity:
        try:
            guests = [guest.to_entity() for guest in self.guests]
        except StatementError:
            guests = None

        return HostAccountEntity(
            entity_id=self.id,
            host_name=self.host_name,
            hashed_password=self.hashed_password,
            refresh_token=self.refresh_token,
            email=self.email,
            user_id=self.user_id,
            guests=guests,
        )

    @classmethod
    def from_entity(cls, entity: HostAccountEntity) -> "HostAccount":
        return cls(
            id=entity.id,
            host_name=entity.host_name,
            hashed_password=entity.hashed_password,
            refresh_token=entity.refresh_token,
            email=entity.email,
            user_id=entity.user_id,
        )


class GuestAccount(AbstractCommonDynamicBase):
    guest_first_name: Mapped[str] = mapped_column(
        VARCHAR(64), nullable=False, comment="Guest First Name"
    )
    guest_last_name: Mapped[str] = mapped_column(
        VARCHAR(64), nullable=False, comment="Guest Last Name"
    )
    guest_nickname: Mapped[str | None] = mapped_column(
        VARCHAR(64), nullable=True, comment="Guest Nickname"
    )
    hashed_password: Mapped[str] = mapped_column(
        VARCHAR(512), nullable=False, comment="Hashed Password"
    )
    refresh_token: Mapped[str | None] = mapped_column(
        VARCHAR(512), nullable=True, comment="Refresh Token"
    )
    user_id: Mapped[int] = mapped_column(
        BIGINT(unsigned=True), unique=True, nullable=False, comment="User ID"
    )
    host_id: Mapped[str] = mapped_column(
        VARCHAR(36), ForeignKey("host_account.id", ondelete="CASCADE"), nullable=False
    )
    host: Mapped["HostAccount"] = relationship(back_populates="guests", uselist=False)
    UniqueConstraint("guest_first_name", "guest_last_name", "guest_nickname", "host_id")

    def to_entity(self) -> GuestAccountEntity:
        return GuestAccountEntity(
            entity_id=self.id,
            guest_first_name=self.guest_first_name,
            guest_last_name=self.guest_last_name,
            guest_nickname=self.guest_nickname,
            hashed_password=self.hashed_password,
            refresh_token=self.refresh_token,
            user_id=self.user_id,
            host_id=self.host_id,
        )

    @classmethod
    def from_entity(cls, entity: GuestAccountEntity) -> "GuestAccount":
        return cls(
            id=entity.id,
            guest_first_name=entity.guest_first_name,
            guest_last_name=entity.guest_last_name,
            guest_nickname=entity.guest_nickname,
            hashed_password=entity.hashed_password,
            refresh_token=entity.refresh_token,
            user_id=entity.user_id,
            host_id=entity.host_id,
        )
