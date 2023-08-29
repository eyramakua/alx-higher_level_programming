#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        mus = fct(*args)
    except BaseException as e:
        mus = None
        print("Exception: {}".format(e), file=sys.stderr)
    finally:
        return mus
