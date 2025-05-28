import asyncio
from functools import wraps
from typing import Any, Callable, Coroutine, Never, cast


def coro[**P, T: Coroutine[Any, Any, Never]](
    f: Callable[P, T],
) -> Callable[[Any, Any], Any]:
    @wraps(f)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> Any:
        return asyncio.run(f(*args, **kwargs))

    return cast(Callable[[Any, Any], Any], wrapper)
