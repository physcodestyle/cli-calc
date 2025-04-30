from typing import Any
from models.add import calc as add_calc, get_values as add_get_values


def calc(model: str, values: list[dict]) -> tuple[float, Exception]:
    if model == 'add':
        return add_calc(values=values)


def get_values(model: str) -> str:
    if model == 'add':
        return add_get_values()
