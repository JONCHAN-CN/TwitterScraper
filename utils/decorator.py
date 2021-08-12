from functools import wraps
from time import time

from .logger import *


def try_exception(function):
    """
    A decorator that wraps the passed in function and logs exceptions should one occur
    https://www.blog.pythonlibrary.org/2016/06/09/python-how-to-create-an-exception-logging-decorator/
    """
    exp_logger = init_logger('./log/exception.log', 'a', 'exception')

    @wraps(function)
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except:
            # log the exception
            err = "There was an exception in  "
            err += function.__name__
            exp_logger.exception(err)

            # # re-raise the exception
            # raise

    return wrapper


def time_elapsed(function):
    """
    A decorator that time passed in function
    https://codereview.stackexchange.com/questions/169870/decorator-to-measure-execution-time-of-a-function
    """

    @wraps(function)
    def wrapper(*args, **kw):
        ts = time()
        result = function(*args, **kw)
        te = time()
        # print('func:%r args:[%r, %r] took: %2.4f sec' % (function.__name__, args, kw, te-ts))
        print('%r took %2.2f sec\n' % (function.__name__, te - ts))
        return result

    return wrapper

def time_log(function):
    """
    A decorator that log when it is done
    """

    @wraps(function)
    def wrapper(*args, **kw):
        result = function(*args, **kw)
        now = dt.now().strftime('%Y-%m-%d %H:%M:%S')
        print('%r on %s\n' % (function.__name__, now))
        return result

    return wrapper