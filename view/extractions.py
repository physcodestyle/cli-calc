import re
from view.constants import BASIC_OPTIONS


def extract_values(args: list[str]) -> tuple[list[dict], Exception]:
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


def extract_options(args: list[str]) -> tuple[list[dict], Exception]:
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
