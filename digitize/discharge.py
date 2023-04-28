from .language import Language
from .digit_suffixes import DIGIT_SUFFIXES

def discharge(value: int, discharge_text_bool: bool = False, language: str = Language.EN):
    result = ('{0:,}'.format(round(value, 2)).replace(',', ','))
    discharge_text = "None"

    if discharge_text_bool:
        digit = 1
        value = value // 10
        while value > 0:
            value = value // 10
            digit = digit + 1

        digit_suffixes = DIGIT_SUFFIXES.get(language, {})

        discharge_text = digit_suffixes.get((digit - 1) // 3, '')

    return (result + f" {discharge_text}") if discharge_text_bool in [True, "True", 1, "1"] else (result)
