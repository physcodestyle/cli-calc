def calc(*args: float) -> tuple[float, Exception]:
    result = 0
    for num in args:
        result += num
    return (result, None)


def settings() -> dict:
    return {
        "input": {
            "type": [ "prompt" ],
            "options": [
                { "separated_float": " " }
            ],
        },
        "output": {
            "type": [ "alert" ],
            "options": [ {} ]
        }
    }
