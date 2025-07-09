from typing import Callable


def show_greeting(mode: str, options: list[dict], values: list[dict]) -> tuple[str, list[dict], list[dict], Exception]:
    print('Terminal mode')
    return ('terminal', options, values, None)


def request_options(message: str, callback: Callable) -> list[dict]:
    str = input(message)
    return callback(str.split(' '))


def request_values(message: str, callback: Callable) -> list[dict]:
    str = input(message)
    return callback(str.split(' '))


def request_raw_input(message: str) -> list[dict]:
    return input(message)
