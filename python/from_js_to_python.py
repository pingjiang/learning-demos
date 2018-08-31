"""

0. style guides

https://www.python.org/dev/peps/pep-0008/

1. strong types: int, str, list, tuple, map, set, fn, class, regexp
2. stdlib
3. thirdparty libs
4. if else
"""
from pprint import pprint


def data_types():
    int_val = 1
    price = 9.23
    re_num = r'\\d+\\.\\d+'
    bool_val = True
    str_val = 'Lorem'
    items = ['foo', 'bar']
    fruits = { 'apple', 'orange' }
    obj = {
        'key': 'value',
    }

    pprint({
        str_val: str_val,
        'int_val': int_val,
        'price': price,
        're_num': re_num,
        'bool_val': bool_val,
        'str_val': str_val,
        'items': items,
        'fruits': fruits,
        'obj': obj,
    }, indent=4)


if __name__ == '__main__':
    data_types()
