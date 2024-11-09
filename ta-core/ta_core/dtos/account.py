from pydantic import BaseModel
from pydantic.fields import Field
from pydantic.networks import EmailStr

from ta_core.dtos.base import BaseModelWithErrorCodes


class CreateHostAccountRequest(BaseModel):
    host_name: str = Field(..., title="Host Name")
    password: str = Field(..., title="Password")
    email: EmailStr = Field(..., title="Email")


class CreateHostAccountResponse(BaseModelWithErrorCodes):
    pass


class CreateGuestAccountRequest(BaseModel):
    guest_first_name: str = Field(..., title="Guest First Name")
    guest_last_name: str = Field(..., title="Guest Last Name")
    guest_nickname: str | None = Field(None, title="Guest Nickname")
    password: str = Field(..., title="Password")
    host_name: str = Field(..., title="Associated Host Name")


class CreateGuestAccountResponse(BaseModelWithErrorCodes):
    pass


class GuestInfo(BaseModel):
    account_id: str = Field(..., title="Account ID")
    first_name: str = Field(..., title="First Name")
    last_name: str = Field(..., title="Last Name")
    nickname: str | None = Field(None, title="Nickname")


class GetGuestsInfoResponse(BaseModelWithErrorCodes):
    guests: tuple[GuestInfo, ...] = Field(..., title="Guests Info")
