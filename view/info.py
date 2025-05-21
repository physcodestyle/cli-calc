from typing import Callable


def show_greeting(mode: str, options: list[dict], values: list[dict]) -> tuple[str, list[dict], list[dict], Exception]:
    print('Info mode')
    return ('info', options, values, None)
