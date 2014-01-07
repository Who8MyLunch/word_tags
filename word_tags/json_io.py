
from __future__ import division, print_function, unicode_literals

import simplejson as json


def read(fname):
    """Read serialized data from JSON file, decode into Python object(s).

    Parameters
    ----------
    fname : string file name.

    """
    # Read string from JSON file.
    with open(fname, 'r') as fi:
        serial = fi.read()

    # Decode.
    decoder = json.JSONDecoder()
    data = decoder.decode(serial)

    return data


def write(fname, data):
    """Encode Python object(s), write to JSON file.

    Parameters
    ----------
    fname : string file name.
    data : Data to be written to file.

    """
    # Encode to string.
    # encoder = json.JSONEncoder()
    # serial = encoder.encode(data)

    # Write to file.
    s = pretty(data)
    with open(fname, 'w') as fo:
        fo.write(s)


def pretty(data_dict):
    s = json.dumps(data_dict, sort_keys=True, indent=4, separators=(',', ': '))
    return s
