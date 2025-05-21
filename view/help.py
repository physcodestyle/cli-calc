from typing import Callable
from view.constants import APP_VERSION, TAB_SPACES_COUNT, BASIC_OPTIONS


def show_greeting(mode: str, options: list[dict], values: list[dict]) -> tuple[str, list[dict], list[dict], Exception]:
    output = f'''CLI Calc (v{APP_VERSION})

NAME
\tpython calc.py — CLI Calc for run different calculations

SYNOPSIS
\tpython calc.py [--help] [--interactive] [--list] [--model=<model's name>] [--params=<model's params>] [--input=<float numbers>] [--output=<output type>]

\tpython calc.py [<model's name>] [help] [--params=<model's params>] [<float/int numbers>]

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
    return ('help', options, values, None)
