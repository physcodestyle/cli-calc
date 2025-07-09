from controller.interactive import change_state, init_state, is_option_state, is_input_state, is_output_state
from view.interactive import get_request_message
from view.main import choose_mode as select_view_mode, request_values as get_values_from_user, request_options as get_options_from_user, request_raw_input as get_raw_input_from_user
from models.main import print_help as model_help, print_list as model_list, calc as model_calc, get_values as model_get_values_message


def is_help_mode(options: list[dict]) -> bool:
    for opt in options:
        if opt['key'] == 'help':
            return True
    return False


def is_list_mode(options: list[dict]) -> bool:
    for opt in options:
        if opt['key'] == 'list':
            return True
    return False


def is_interactive_mode(mode: str) -> bool:
    return mode == 'interactive'


def chose_model(options: list[dict]) -> str:
    for opt in options:
        if opt['key'] == 'model':
            return opt['value']
    return ''


def get_params(options: list[dict]) -> str:
    for opt in options:
        if opt['key'] == 'params':
            return opt['value']
    return ''


def run(row_args: list[str]):
    mode, options, values, err = select_view_mode(row_args=row_args)
    if err != None:
        print(err)
    if is_help_mode(options=options):
        model = chose_model(options=options)
        model_help(model=model)
    elif is_list_mode(options=options):
        model_list()
    elif is_interactive_mode(mode=mode):
        is_live = True
        current_state = init_state()
        state_data = {}
        user_input = ''
        while is_live:
            if not is_output_state(state=current_state):
                if is_option_state(state=current_state):
                    user_input = get_options_from_user(mode=mode, message=get_request_message(state=current_state))
                elif is_input_state(state=current_state):
                    user_input = get_values_from_user(mode=mode, message=get_request_message(state=current_state))
                else:
                    user_input = get_raw_input_from_user(mode=mode, message=get_request_message(state=current_state))
            else:
                print(get_request_message(state=current_state))
            current_state, state_data, is_live = change_state(state=current_state, data=state_data, user_input=user_input)
    else:
        model = chose_model(options=options)
        result, err = model_calc(model=model, values=values, params=get_params(options=options))
        if err != None:
            values, err = get_values_from_user(mode=mode, message=model_get_values_message(model=model))
            if err != None:
                print(err)
            result, err = model_calc(model=model, values=values, params=get_params(options=options))
            if err != None:
                print(err)
        print(result)
