from models.add import print_help as add_help, calc as add_calc, get_values as add_get_values


def print_help(model: str):
    if model == 'add':
        return add_help()


def calc(model: str, values: list[dict], params: str) -> tuple[float, Exception]:
    if model == 'add':
        return add_calc(values=values, params=params)


def get_values(model: str) -> str:
    if model == 'add':
        return add_get_values()
