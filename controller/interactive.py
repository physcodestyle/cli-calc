import re
from models.main import MODEL_LIST, print_help, print_list as model_list, calc as model_calc, get_values as model_get_values_message


EXIT_STATE = 0
START_STATE = 1
MODEL_STATE = 2
INPUT_STATE = 4
OPTION_STATE = 8
OUTPUT_STATE = 16
HELP_STATE = 32


def init_state():
    return START_STATE


def change_state(state: int, data: dict, user_input: tuple[str, list[dict]]) -> tuple[int, dict, bool]:
    if is_ready_to_exit(user_input=user_input):
        return (EXIT_STATE, data, False)
    elif state == START_STATE:
        print(model_list())
        return (MODEL_STATE, data, True)
    elif state == MODEL_STATE and user_input != '' and is_number(user_input=user_input):
        model_keys = list(dict.keys(MODEL_LIST))
        model = model_keys[int(user_input) - 1]
        data['model'] = model
        print_help(model=model)
        return (OPTION_STATE, data, True)
    elif state == OPTION_STATE:
        data['params'] = user_input
        print(model_get_values_message(model=data['model']))
        return (INPUT_STATE, data, True)
    elif state == INPUT_STATE and user_input != '':
        data['values'] = user_input
        result, err = model_calc(model=data['model'], values=data['values'], params=data['params'])
        if err != None:
            data['error'] = err
            return (MODEL_STATE, data, True)
        data['result'] = result
        return (OUTPUT_STATE, data, True)
    elif state == OUTPUT_STATE:
        print(data['result'])
        return (START_STATE, data, True)
    else:
        return (state, True)


def is_option_state(state: int) -> bool:
    return state == OPTION_STATE


def is_input_state(state: int) -> bool:
    return state == INPUT_STATE


def is_output_state(state: int) -> bool:
    return state == OUTPUT_STATE


def is_ready_to_exit(user_input: str) -> bool:
    return user_input == 'exit' or user_input == 'quit'


def is_number(user_input: str) -> bool:
    return re.match(r'^\d+$', user_input) or re.match(r'^-?\d+(?:\.\d+)$', user_input)
