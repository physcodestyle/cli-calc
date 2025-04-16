from typing import Any
from alert import give as alert_give


def give(data: Any, type: str, options: dict = {}):
    if type(data) == 'str':
        if type == 'alert':
            alert_give(data=data, options=options)
