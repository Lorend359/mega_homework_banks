from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    Декоратор который автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки.
    """

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            log_message = f"Executing {func.__name__} with inputs: {args}, {kwargs}"

            if filename:
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(log_message + "\n")
            else:
                print(log_message)

            try:
                result = func(*args, **kwargs)
                log_success = f"{func.__name__} ok: {result}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(log_success + "\n")
                else:
                    print(log_success)
                return result
            except Exception as e:
                log_error = f"{func.__name__} error: {type(e).__name__}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(log_error + "\n")
                else:
                    print(log_error)
                raise

        return inner

    return decorator
