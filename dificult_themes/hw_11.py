from functools import wraps
from typing import Callable


def round_result(ndigits: int):
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if type(result) == float or type(result) == int:
                return round(result, ndigits)
            return result

        return wrapper

    return decorator


@round_result(2)
def foo():
    return 12345.5565468


print(foo())
