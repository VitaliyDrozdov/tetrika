import inspect
from functools import wraps


def strict(func):
    sig = inspect.signature(func)

    @wraps(func)
    def wrapper(*args, **kwargs):
        sig_args = sig.bind(*args, **kwargs)
        for name, value in sig_args.arguments.items():
            expected_type = sig.parameters[name].annotation
            if expected_type is inspect._empty:
                continue
            if not isinstance(value, expected_type):
                raise TypeError(
                    f"Аргумент '{name}' должен быть с типом {expected_type.__name__}, "
                    f"Текущий тип: {type(value).__name__}"
                )
        return func(*args, **kwargs)

    return wrapper


# @strict
# def sum_two(a: int, b: int) -> int:
#     return a + b


# print(sum_two(1, 2))  # 3
# print(sum_two(1, 2.4))  # TypeError
