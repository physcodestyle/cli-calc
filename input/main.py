from typing import Any
from prompt import get as prompt_get


def get(message: str, type: str, options: dict = {}) -> Any | None:
    if type == 'prompt':
        user_input, err = prompt_get(message=message, options=options)
        if err != None:
            print(err)
        return user_input
    return None
