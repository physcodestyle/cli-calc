from view.extractions import extract_options, extract_values
from view.interactive import show_greeting as show_ui, request_values as get_values_from_ui, request_options as get_options_from_ui, request_raw_input as get_raw_input_from_ui
from view.terminal import show_greeting as show_terminal, request_values as get_values_from_terminal, request_options as get_options_from_terminal, request_raw_input as get_raw_input_from_terminal
from view.info import show_greeting as show_info
from view.help import show_greeting as show_help


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


def request_options(mode: str, message: str) -> list[dict]:
    if mode == 'interactive':
        options, err = get_options_from_ui(message=message, callback=extract_options)
        if err != None:
            print(err)
            return []
        return options
    elif mode == 'terminal':
        options, err = get_options_from_terminal(message=message, callback=extract_options)
        if err != None:
            print(err)
            return []
        return options
    else:
        str = input(message)
        return extract_options(str.split(' '))


def request_values(mode: str, message: str) -> list[dict]:
    if mode == 'interactive':
        values, err = get_values_from_ui(message=message, callback=extract_values)
        if err != None:
            print(err)
            return []
        return values
    elif mode == 'terminal':
        values, err = get_values_from_terminal(message=message, callback=extract_values)
        if err != None:
            print(err)
            return []
        return values
    else:
        str = input(message)
        return extract_values(str.split(' '))


def request_raw_input(mode: str, message: str) -> str:
    if mode == 'interactive':
        return get_raw_input_from_ui(message=message)
    elif mode == 'terminal':
        return get_raw_input_from_terminal(message=message)
    else:
        return input(message)
