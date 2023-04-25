import numpy as np


def np_encoder(object):
    if isinstance(object, np.generic):
        return object.item()