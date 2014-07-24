from __future__ import absolute_import
from random import shuffle
from importlib import import_module
from algorithms.conf import ALGORITHM_MAPPER

SEQ = range(100)
shuffle(SEQ)

def run(algorithm_name, **kwargs):
    seq = kwargs.get('seq', SEQ)
    try:
        mapper = ALGORITHM_MAPPER[algorithm_name]
        module = import_module(mapper['module'])
        method = getattr(module, mapper['method'])
    except KeyError as ex:
        raise ex
    return method(seq)
