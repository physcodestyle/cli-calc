from view.main import choose_mode as select_view_mode, request_values as get_values_from_user
from models.main import calc as model_calc, get_values as model_get_values_message


def chose_model(options: list[dict]) -> str:
    for opt in options:
        if opt['key'] == 'model':
            return opt['value']
    return ''


def run(row_args: list[str]):
    mode, options, values, err = select_view_mode(row_args=row_args)
    if err != None:
        print(err)
    model = chose_model(options=options)
    result, err = model_calc(model=model, values=values)
    if err != None:
        values, err = get_values_from_user(mode=mode, message=model_get_values_message(model=model))
        if err != None:
            print(err)
        result, err = model_calc(model=model, values=values)
        if err != None:
            print(err)
    print(result)
