def calc(values: list[dict]) -> tuple[float, Exception]:
    result = 0
    if not is_valid(values=values):
        return (result, ValueError)
    for val in values:
        result += val['value']
    return (result, None)


def is_valid(values: list[dict]) -> bool:
    for val in values:
        if val['type'] != 'int' and val['type'] != 'float':
            return False
    return True


def get_values() -> str:
    return 'Please enter integer or float values divided by space: '
