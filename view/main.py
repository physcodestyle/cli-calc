import re
from view.constants import BASIC_OPTIONS
from view.interactive import show_greeting as show_ui, request_values as get_values_from_ui
from view.terminal import show_greeting as show_terminal, request_values as get_values_from_terminal
from view.info import show_greeting as show_info
from view.help import show_greeting as show_help


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
        return show_help('', [{
            'key': 'help',
            'value': ''
        }], [])
    else:
        terminal_mode, options, values, err = process_args(args)
        if err != None:
            return err
        elif detect_mode(options=options, mode_key='list'):
            return show_info(terminal_mode, options, values)
        elif detect_mode(options=options, mode_key='help') and not detect_mode(options=options, mode_key='model'):
            return show_help(terminal_mode, options, values)
        elif detect_mode(options=options, mode_key='interactive'):
            return show_ui(terminal_mode, options, values)
        else:
            return show_terminal(terminal_mode, options, values)


def request_values(mode: str, message: str) -> list[dict]:
    if mode == 'interactive':
        return get_values_from_ui(message=message, callback=extract_values)
    elif mode == 'terminal':
        return get_values_from_terminal(message=message, callback=extract_values)
    else:
        str = input(message)
        return extract_values(str.split(' '))
