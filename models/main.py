from typing import Any
from add import calc as add_calc
from add import settings as add_settings


def calc(*args: Any, operation: str) -> Any:
    if operation == 'add':
        preprocessed_args = map(lambda arg: float(arg), args)
        result, err = add_calc(preprocessed_args)
        if err != None:
            print(err)
        return result


def settings(operation: str) -> dict:
    if operation == 'add':
        return add_settings()
