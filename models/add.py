MODEL_VERSION = '0.1.0'
TAB_SPACES_COUNT = 8
BASIC_OPTIONS = {
    'help': 'Show this help',
    'progression': 'Use arithmetic progression (the first argument is basis, the second argument is step)',
}


def print_help():
    output = f'''Add Model (v{MODEL_VERSION})

NAME
\tpython calc.py -m=add — Using Add Model for CLI Calc

SYNOPSIS
\tpython calc.py -m=add [--help] [--progression=<step count>] [<float/int numbers>]

\tpython calc.py add [help] [--progression=<step count>] [<float/int numbers>]

DESCRIPTION
\tAdd Model for CLI Calc is a model for calculation of summa of numbers (also use for arithmetic progression).

\tThe following options ara available:
'''
    keys = list(dict.keys(BASIC_OPTIONS))
    tabs = []

    for k in keys:
        tabs.append((len(k) + 6) // TAB_SPACES_COUNT)

    for i in range(len(keys)):
        output += '\n\t--' + keys[i]
        output += ', -' + keys[i][0] + '\t'
        output += ''.join(['\t' for _ in range(max(tabs) - tabs[i])])
        output += BASIC_OPTIONS[keys[i]] + '\n'

    print(output)


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
