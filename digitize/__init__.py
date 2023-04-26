"""
digitize - open source available library for determining the
bit depth of a number with the output of its name.
"""

__title__ = "digitize"
__author__ = "LimeGeeg"
__license__ = "MIT"
__copyright__ = "Copyright 2023-present LimeGeeg"
__version__ = "1.2.0"

from .digit_suffixes import DIGIT_SUFFIXES
from .language import Language

DIGIT_SUFFIXES_EN = {
    0: '',
    1: 'thousand',
    2: 'million',
    3: 'billion',
    4: 'trl.',
    5: 'square',
    6: 'quin.',
    7: 'sex',
    8: 'Sept.',
    9: 'octyl.',
    10: 'nonyl.',
    11: 'dycel.',
    12: 'undecyl.',
    13: 'duodecil.',
    14: 'tredecyl.',
    15: 'quatzel.',
    16: 'quindecl.',
    17: 'sexdicyl.',
    18: 'septindecyl.',
    19: 'octodecyl.',
    20: 'novemdecyl.',
    21: 'vigintil.',
    22: 'unvigint.',
    23: 'duovigintil.',
    24: 'trevintil.',
    25: 'quattuorvigintil.',
    26: 'quinvintil.',
    27: 'sexvigintyl.',
    28: 'septinvintil.',
    29: 'octovagintil.',
    30: 'novemvigintil.',
    31: 'trigintil.',
    32: 'untrigintil.',
    33: 'duotrigintyl.',
    34: 'googol.',
    35: 'tretrigintil.',
    36: 'quattuortrigintil.',
    37: 'quintrigil.',
    38: 'sextrigintil.',
    39: 'septintrigintil.',
    40: 'octotrigintil.',
    41: 'novemtrigintil.',
    42: 'quadragintyl.',
    43: 'unquadragyntel.',
    44: 'duoquadragynthyl.',
    45: 'trewkadragintil.',
    46: 'quattuorquadragintyl.',
    47: 'quinquadragintyl.',
    48: 'sexquadragyntel.',
    49: 'septinquadragintyl.',
    50: 'octovquadragint.',
    51: 'novemquadragintyl.',
}

DIGIT_SUFFIXES_RU = {
    0: '',
    1: 'тыс.',
    2: 'млн.',
    3: 'млрд.',
    4: 'трл.',
    5: 'квдр.',
    6: 'квин.',
    7: 'секст.',
    8: 'септ.',
    9: 'октил.',
    10: 'нонил.',
    11: 'дицел.',
    12: 'ундецил.',
    13: 'дуодецил.',
    14: 'тредецил.',
    15: 'кватцел.',
    16: 'квиндецл.',
    17: 'сексдицил.',
    18: 'септиндецил.',
    19: 'октодецил.',
    20: 'новемдецил.',
    21: 'вигинтил.',
    22: 'унвигинтил.',
    23: 'дуовигинтил.',
    24: 'тревинтил.',
    25: 'кваттуорвигинтил.',
    26: 'квинвигинтил.',
    27: 'сексвигинтил.',
    28: 'септинвигинтил.',
    29: 'октовигинтил.',
    30: 'новэмвигинтил.',
    31: 'тригинтил.',
    32: 'унтригинтил.',
    33: 'дуотригинтил.',
    34: 'гугол.',
    35: 'третригинтил.',
    36: 'кваттуортригинтил.',
    37: 'квинтригил.',
    38: 'секстригинтил.',
    39: 'септинтригинтил.',
    40: 'октотригинтил.',
    41: 'новемтригинтил.',
    42: 'квадрагинтил.',
    43: 'унквадрагинтел.',
    44: 'дуоквадрагинтил.',
    45: 'тревкадрагинтил.',
    46: 'кваттуорквадрагинтил.',
    47: 'квинквадрагинтил.',
    48: 'сексквадрагинтел.',
    49: 'септинквадрагинтил.',
    50: 'октовквадрагинтал.',
    51: 'новемквадрагинтил.',
}

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
