# coding=utf-8
from __future__ import print_function, unicode_literals
import platform
import functools
from dota2crawler.config import IS_PYTHON3

if platform.system() == 'Windows':
    GREEN = ''
    YELLOW = ''
    RED = ''
    COLOR_END = ''
else:
    GREEN = '\033[1;32m'
    YELLOW = '\033[1;33m'
    RED = '\033[1;31m'
    COLOR_END = '\033[0m'

color_map = {
    'print_info': '',
    'print_success': GREEN,
    'print_warning': YELLOW,
    'print_error': RED,
}

indicator_map = {
    'print_info': '[*] ',
    'print_success': '[+] ',
    'print_warning': '[-] ',
    'print_error': '[x] ',
}


def indicator(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        if kwargs.get('indicator', True):
            if IS_PYTHON3:
                func_name = f.__qualname__
            else:
                func_name = f.func_name
            args = (indicator_map.get(func_name, '') + args[0], )
        return f(*args, **kwargs)

    return wrapper


def colorize(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        if IS_PYTHON3:
            func_name = f.__qualname__
        else:
            func_name = f.func_name
        b, e = color_map.get(func_name,
                             ''), COLOR_END if color_map.get(func_name) else ''
        args = tuple(map(lambda s: b + s + e, args))
        return f(*args, **kwargs)

    return wrapper


@indicator
@colorize
def print_info(message, indicator=True):
    print(message)


@indicator
@colorize
def print_success(message, indicator=True):
    print(message)


@indicator
@colorize
def print_warning(message, indicator=True):
    print(message)


@indicator
@colorize
def print_error(message, exit_=True, indicator=True):
    print(message)
    if exit_:
        exit(1)


def unicodeize(data):
    import dota2crawler.config
    if dota2crawler.config.IS_PYTHON3:
        if isinstance(data, bytes):
            return data.decode('utf-8')
        else:
            return data
            # return bytes(str(data), 'latin-1').decode('utf-8')
    try:
        return unicode(data.decode('utf-8'))
    except (UnicodeEncodeError, UnicodeDecodeError):
        return unicode(data.decode('gbk'))
    except (UnicodeEncodeError, UnicodeDecodeError):
        return data
