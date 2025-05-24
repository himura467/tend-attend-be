from functools import wraps
from typing import Awaitable, Callable, cast

from ta_core.domain.use_case.base import IUseCase
from ta_core.dtos.base import BaseModelWithErrorCodes


def rollbackable[**P, T: Awaitable[BaseModelWithErrorCodes]](
    f: Callable[P, T],
) -> Callable[P, T]:
    @wraps(f)
    async def wrapper(
        self: IUseCase, *args: P.args, **kwargs: P.kwargs
    ) -> BaseModelWithErrorCodes:
        response: BaseModelWithErrorCodes = await f(self, *args, **kwargs)
        if response.error_codes:
            await self.uow.rollback_async()
        else:
            await self.uow.commit_async()
        return response

    return cast(Callable[P, T], wrapper)
