from typing import Callable


GREETING_MESSAGE = 'Interactive mode'
STATE_MESSAGES = {
    '0': 'Good bye!',
    '1': '''
To exit from interactive mode please type 'exit' or 'quit' when it will be possible.

Please press Enter to choose the model for calculation...
''',
    '2': '''
Please choose from following models by input according number...

''',
    '4': '''
Please input a list of values divided by space to get a result of calculation...

''',
    '8': '''
Please input a list of following options for chosen model divided by space...

''',
    '16': '''
Result of calculation:
''',
    '32': '''
Press Enter to continue...''',
}


def show_greeting(mode: str, options: list[dict], values: list[dict]) -> tuple[str, list[dict], list[dict], Exception]:
    print(GREETING_MESSAGE)
    return ('interactive', options, values, None)


def request_values(message: str, callback: Callable) -> list[dict]:
    str = input(message)
    return callback(str.split(' '))


def request_options(message: str, callback: Callable) -> list[dict]:
    str = input(message)
    return callback(str.split(' '))


def request_raw_input(message: str) -> list[dict]:
    return input(message)


def get_request_message(state: str) -> str:
    return STATE_MESSAGES[str(state)]
