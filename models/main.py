from models.add import get_short_info as add_info, print_help as add_help, calc as add_calc, get_values as add_get_values


def print_help(model: str):
    if model == 'add':
        return add_help()


def print_list():
    output = f'''
MODEL LIST:
{add_info()}
'''
    print(output)


def calc(model: str, values: list[dict], params: str) -> tuple[float, Exception]:
    if model == 'add':
        return add_calc(values=values, params=params)


def get_values(model: str) -> str:
    if model == 'add':
        return add_get_values()
