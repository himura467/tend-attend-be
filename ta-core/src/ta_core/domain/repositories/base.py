from abc import ABCMeta, abstractmethod
from typing import Any, Generic, Protocol, Type, TypeVar

from sqlalchemy.orm.base import Mapped

from ta_core.domain.entities.base import IEntity
from ta_core.utils.uuid import UUID

TEntity = TypeVar("TEntity", bound=IEntity)
TModel = TypeVar("TModel", bound="ModelProtocol[Any]")


class ModelProtocol(Protocol[TEntity]):
    id: Mapped[bytes]

    def to_entity(self) -> TEntity: ...

    @classmethod
    def from_entity(cls: Type[TModel], entity: TEntity) -> TModel: ...


class IRepository(Generic[TEntity, TModel], metaclass=ABCMeta):
    @abstractmethod
    async def create_async(self, entity: TEntity) -> TEntity | None:
        raise NotImplementedError()

    @abstractmethod
    async def bulk_create_async(self, entities: set[TEntity]) -> set[TEntity] | None:
        raise NotImplementedError()

    @abstractmethod
    async def read_by_id_async(self, record_id: UUID) -> TEntity:
        raise NotImplementedError()

    @abstractmethod
    async def read_by_id_or_none_async(self, record_id: UUID) -> TEntity | None:
        raise NotImplementedError()

    @abstractmethod
    async def read_by_ids_async(self, record_ids: set[UUID]) -> set[TEntity]:
        raise NotImplementedError()

    @abstractmethod
    async def read_all_async(self, where: list[Any]) -> set[TEntity]:
        raise NotImplementedError()

    @abstractmethod
    async def update_async(self, entity: TEntity) -> TEntity:
        raise NotImplementedError()

    @abstractmethod
    async def delete_by_id_async(self, record_id: UUID) -> None:
        raise NotImplementedError()

    @abstractmethod
    async def delete_all_async(self, where: list[Any]) -> None:
        raise NotImplementedError()
