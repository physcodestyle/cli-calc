MODEL_VERSION = '0.1.0'
TAB_SPACES_COUNT = 8
BASIC_OPTIONS = {
    'help': 'Show this help',
    'progression': 'Use geometric progression (the first argument is basis, the second argument is step)',
}


def get_short_info():
    return f'\tmult:\tMultiplication Model (v{MODEL_VERSION}) — is for calculation of multiplication of numbers (also use for geometric progression).'


def print_help():
    output = f'''Multiplication Model (v{MODEL_VERSION})

NAME
\tpython calc.py -m=mult — Using Multiplication Model for CLI Calc

SYNOPSIS
\tpython calc.py -m=mult [--help] [--params=progression] [<float/int numbers>] (3 values for geometric progression: basis, step, step_count)

\tpython calc.py mult [help] [--params=progression] [<float/int numbers>] (3 values for geometric progression: basis, step, step_count)

DESCRIPTION
\Multiplication Model for CLI Calc is a model for calculation of multiplication of numbers (also use for geometric progression).

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


def calc(values: list[dict], params: str) -> tuple[float, Exception]:
    result = 0
    if not is_valid(values=values):
        return (result, ValueError)
    if is_progression_mode(params=params):
        result = values[0]['value']
        for _ in range(values[2]['value']):
            result *= values[1]['value']
    else:
        if len(values) > 0:
            result = 1
        for val in values:
            result *= val['value']
    return (result, None)


def get_values() -> str:
    return 'Please enter integer or float values divided by space: '


def is_valid(values: list[dict]) -> bool:
    for val in values:
        if val['type'] != 'int' and val['type'] != 'float':
            return False
    return True


def is_progression_mode(params: str) -> bool:
    return params == 'progression'
