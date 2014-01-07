#!/usr/bin/python

from __future__ import division, print_function, unicode_literals

import json_io
import word_set
import tagger

"""
This is an example of using the two classes Word_Set and Tagger to tag specified words
in a sentence.

"""

# Files.

fname_config = 'config.json'

mapping = json_io.read(fname_config)

words = word_set.Word_Set(mapping)
