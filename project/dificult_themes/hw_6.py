from typing import Callable


def always_return_dist_result(func: Callable) -> Callable:
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)

        return {'result': result}

    return inner


@always_return_dist_result
def foo():
    return 22


print(foo())
