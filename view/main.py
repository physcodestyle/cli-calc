APP_VERSION = '0.1.0'
TAB_SPACES_COUNT = 8
BASIC_OPTIONS = {
    'help': 'Show this help',
    'interactive': 'Use interactive mode',
    'list': 'Show all available models',
    'model': 'Use chosen model for calculation',
    'params': 'Use params for chosen calculation model',
    'values': 'Use input values for chosen models (compatible float numbers)',
    'output': 'Use chosen output type',
}


def print_help():
    output = f'''CLI Calc (v{APP_VERSION})

NAME
\tpython calc.py — CLI Calc for run different calculations

SYNOPSIS
\tpython calc.py [--help] [--interactive] [--model-list] [--model=<model's name>] [--params=<model's params>] [--input=<float numbers>] [--output=<output type>]

\tpython calc.py [<model's name>] [help] [--params=<model's params>] [<float numbers>]

DESCRIPTION
\tCLI Calc is a universal calculator for terminal which could use any models as an extension for math calculating based on input args with chosen output type.

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


def choose_mode(row_args: list[str]):
    args = row_args[1:]
    if len(args) == 0:
        print_help()

