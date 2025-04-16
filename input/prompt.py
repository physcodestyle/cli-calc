from typing import Any

def get(message: str, options: dict = {}) -> tuple[Any, Exception]:
    user_input = input(message)
    options_keys = [*options]
    if len(options_keys) == 0:
        return (user_input, None)
    elif 'separated_float' in options_keys:
        separated_values = message.split(options['separated_float'])
        return (map(lambda value: float(value), separated_values), None)
    return (user_input, TypeError)
