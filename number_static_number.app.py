# -*- coding: utf-8 -*-

import numpy as np
import time
import sys

TYPE_INT8_NAME = 'int8'
TYPE_INT16_NAME = 'int16'
TYPE_INT32_NAME = 'int32'
TYPE_INT64_NAME = 'int64'
TYPE_FLOAT16_NAME = 'float16'
TYPE_FLOAT32_NAME = 'float32'

TYPE_NAME_TO_NUM = {
    TYPE_INT8_NAME: np.int8,
    TYPE_INT16_NAME: np.int16,
    TYPE_INT32_NAME: np.int32,
    TYPE_INT64_NAME: np.int64,
    TYPE_FLOAT16_NAME: np.float16,
    TYPE_FLOAT32_NAME: np.float32
}
TYPE_NUM_TO_NAME = {v: k for k, v in TYPE_NAME_TO_NUM.items()}


value = '0'
numpy_type = np.int32



def on_set(key, val):
    if key == "value":
        global value
        value = val
    elif key == "type":
        global numpy_type
        numpy_type = TYPE_NAME_TO_NUM[val]


def on_get(key):
    if key == "type":
        return TYPE_NUM_TO_NAME[numpy_type]


def on_init():
    return True


def on_valid():
    return True


def on_run():
    v = 0
    if numpy_type == np.int8:
        v = int(float(value))
    elif numpy_type == np.int16:
        v = int(float(value))
    elif numpy_type == np.int32:
        v = int(float(value))
    elif numpy_type == np.int64:
        v = long(float(value))
    elif numpy_type == np.float16:
        v = float(value)
    elif numpy_type == np.float32:
        v = float(value)
    else:
        v = float(value)

    
    return {'number': np.array([v], numpy_type)}


def on_destroy():
    return True


if __name__ == '__main__':
    pass
