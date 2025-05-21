import re
from view.interactive import show_greeting as show_ui, request_values as get_values_from_ui
from view.terminal import show_greeting as show_terminal, request_values as get_values_from_terminal


APP_VERSION = '0.1.0'
TAB_SPACES_COUNT = 8
BASIC_OPTIONS = {
    'help': 'Show this help',
    'interactive': 'Use interactive mode',
    'list': 'Show all available models',
    'model': 'Use chosen model for calculation',
    'params': 'Use params for chosen calculation model',
    'output': 'Use chosen output type',
}


def print_help():
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


def extract_values(args: list[str]) -> tuple[tuple[str], Exception]:
    output = []
    for row_arg in args:
        if row_arg.startswith('-'):
            continue
        elif re.match(r'^([Tt]rue|[Ff]alse)$', row_arg):
            output.append({ 'type': 'bool', 'value': bool(re.match(r'[Tt]rue', row_arg)) })
        elif re.match(r'^\d+$', row_arg):
            output.append({ 'type': 'int', 'value': int(row_arg) })
        elif re.match(r'^-?\d+(?:\.\d+)$', row_arg):
            output.append({ 'type': 'float', 'value': float(row_arg) })
        else:
            output.append({ 'type': 'str', 'value': row_arg })
    return output, None


def extract_options(args: list[str]) -> tuple[tuple[str], Exception]:
    output = []
    options = list(map(lambda k: '--' + k, dict.keys(BASIC_OPTIONS)))
    opts = list(map(lambda o: o[1:3], options))
    for row_arg in args:
        arg = row_arg.split('=')
        if arg[0] in options:
            output.append({
                'key': arg[0][2:],
                'value': arg[1] if len(arg) > 1 else None,
            })
        elif arg[0] in opts:
            index = -1
            for i in range(len(options)):
                if options[i].startswith('-' + arg[0]):
                    index = i
                    break
            output.append({
                'key': options[index][2:],
                'value': arg[1] if len(arg) > 1 else None,
            })
        else:
            continue
    return output, None


def process_args(args: list[str]) -> tuple[str, list[dict], list[dict], Exception]:
    options, err = extract_options(args)
    if err != None:
        return ('', options, [], err)
    values, err = extract_values(args)
    if err != None:
        return ('', options, values, err)
    if len(values) > 0:
        if not detect_mode(options=options, mode_key='model') and values[0]['type'] == 'str':
            options.append({
                'key': 'model',
                'value': values[0]['value'],
            })
            values = values[1:]
        return ('values', options, values, None)
    return ('options', options, values, None)


def detect_mode(options: tuple[str], mode_key: str) -> bool:
    is_mode_detected = False
    for opt in options:
        if opt['key'] == mode_key:
            is_mode_detected = True
    return is_mode_detected


def choose_mode(row_args: list[str]) -> tuple[list[dict], list[dict], Exception]:
    args = row_args[1:]
    if len(args) == 0:
        print_help()
    else:
        terminal_mode, options, values, err = process_args(args)
        if err != None:
            return err
        elif detect_mode(options=options, mode_key='help') and not detect_mode(options=options, mode_key='model'):
            print_help()
        elif detect_mode(options=options, mode_key='interactive'):
            return show_ui(terminal_mode, options, values)
        else:
            return show_terminal(terminal_mode, options, values)
    return '', options, values, None


def request_values(mode: str, message: str) -> list[dict]:
    if mode == 'interactive':
        return get_values_from_ui(message=message, callback=extract_values)
    elif mode == 'terminal':
        return get_values_from_terminal(message=message, callback=extract_values)
    else:
        str = input(message)
        return extract_values(str.split(' '))
