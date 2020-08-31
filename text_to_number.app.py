import numpy as np
import sys
import re

TRUE_STR_LIST = ['true']


enable_default = False
default_value = 0.0
filter_only_number = False


def println(func_name, text, std=sys.stdout):
    std.write(f'[text_to_number{func_name}] {text}')
    std.flush()


def on_set(k, v):
    if k == 'default_value':
        global default_value
        default_value = float(v)
    elif k == 'enable_default':
        global enable_default
        enable_default = True if v.lower() in TRUE_STR_LIST else False
    elif k == 'filter_only_number':
        global filter_only_number
        filter_only_number = True if v.lower() in TRUE_STR_LIST else False


def on_get(k):
    if k == 'default_value':
        return str(default_value)
    elif k == 'enable_default':
        return str(enable_default)
    elif k == 'filter_only_number':
        return str(filter_only_number)


def on_run(text):

    if not text.shape or len(text.shape) != 1:
        return return_negative()

    string_data = ''.join([ chr(x) for x in text ])

    # string_data = '123??' -> '123'
    # string_data = '12a3'  -> '123'
    # string_data = '12.3'  -> '123'
    if filter_only_number:
        string_data = re.sub('[^0-9]', '', string_data)

    try:
        number = float(string_data)
    except:
        return return_negative()

    println('on_run', f'number - {number}')
    
    return {'number' : np.array([number])}


def return_negative():
    if enable_default:
        return {'number': np.array([default_value])}
    else:
        return {'number': None}

