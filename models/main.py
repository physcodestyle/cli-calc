from models.add import get_short_info as add_info, print_help as add_help, calc as add_calc, get_values as add_get_values


MODEL_LIST = {
    'add': add_info()
}


def print_help(model: str) -> str:
    if model == 'add':
        return add_help()
    else:
        return f'A model \'{model}\' doesn\'t exist'


def print_list():
    output = [ 'MODEL LIST:', '' ]
    counter = 1
    for m in dict.keys(MODEL_LIST):
        output.append(f'{counter}. {MODEL_LIST[m]}')
        counter += 1
    return '\n'.join(output)


def calc(model: str, values: list[dict], params: str) -> tuple[float, Exception]:
    if model == 'add':
        return add_calc(values=values, params=params)


def get_values(model: str) -> str:
    if model == 'add':
        return add_get_values()
