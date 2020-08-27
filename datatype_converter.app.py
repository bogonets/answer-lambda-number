import numpy as np
import sys

TRUE_STR_LIST = ['true']


enable_default = False
default_value = 0.0


def on_set(k, v):
    if k == 'default_value':
        global default_value
        default_value = float(v)
    elif k == 'enable_default':
        global enable_default
        enable_default = True if v.lower() in TRUE_STR_LIST else False


def on_get(k):
    if k == 'default_value':
        return str(default_value)
    elif k == 'enable_default':
        return str(enable_default)


def on_run(text):

    if not text.shape or len(text.shape) != 1:
        return return_negative()

    string_data = ''.join([ chr(x) for x in text ])

    try:
        number = float(string_data)
    except:
        return return_negative()

    return {'number' : np.array([number])}


def return_negative():
    if enable_default:
        return {'number': np.array([default_value])}
    else:
        return {'number': None}

