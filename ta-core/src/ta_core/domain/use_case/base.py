from dataclasses import dataclass

from ta_core.domain.unit_of_work.base import IUnitOfWork


@dataclass(frozen=True)
class IUseCase:
    uow: IUnitOfWork
