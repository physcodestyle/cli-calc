from view.main import choose_mode as select_view_mode, request_values as get_values_from_user
from models.main import print_help as model_help, print_list as model_list, calc as model_calc, get_values as model_get_values_message


def is_help_mode(options: list[dict]) -> str:
    for opt in options:
        if opt['key'] == 'help':
            return True
    return False


def is_list_mode(options: list[dict]) -> str:
    for opt in options:
        if opt['key'] == 'list':
            return True
    return False


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
    model = chose_model(options=options)
    if is_help_mode(options=options):
        model_help(model=model)
    elif is_list_mode(options=options):
        model_list()
    else:
        result, err = model_calc(model=model, values=values, params=get_params(options=options))
        if err != None:
            values, err = get_values_from_user(mode=mode, message=model_get_values_message(model=model))
            if err != None:
                print(err)
            result, err = model_calc(model=model, values=values, params=get_params(options=options))
            if err != None:
                print(err)
        print(result)
