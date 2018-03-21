import inspect
import re

from logger.log_config import log_msg


def log(func):
    def wrapper(*args, **kwargs):
        func_name = func.__code__.co_name
        func_args = inspect.getfullargspec(func).args
        module = re.compile('\/([a-zA-Z]+)\.py').findall(func.__code__.co_filename)[0]

        log_msg(module, 'execute func :: `' + func_name + '` with args:: ' + str(func_args))
        return func(*args, **kwargs)

    return wrapper
