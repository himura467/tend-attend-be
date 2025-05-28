import asyncio

import typer
from ta_core.infrastructure.sqlalchemy.db import get_db_async
from ta_core.infrastructure.sqlalchemy.unit_of_work import SqlalchemyUnitOfWork
from ta_core.usecase.develop import DevelopUsecase

app = typer.Typer()


@app.command("attendance-log")
def mock_attendance_log() -> None:
    async def run_mock_async() -> None:
        session = await get_db_async().__anext__()
        uow = SqlalchemyUnitOfWork(session=session)
        usecase = DevelopUsecase(uow=uow)
        await usecase.mock_user_attendance_sequence_async()

    asyncio.get_event_loop().run_until_complete(run_mock_async())
