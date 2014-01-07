#!/usr/bin/python

from __future__ import division, print_function, unicode_literals

import json_io
import word_set
import tagger

"""
This is an example of using the two classes Word_Set and Tagger to tag specified words
in a sentence.

"""

# Load tag/word maps from file.
fname_config = 'config.json'
mapping = json_io.read(fname_config)

# Build a tag matcher class with loaded tag/word mapping.
tag_matcher = tagger.Tagger(mapping)

# Demonstrate with a sentence.
sentence = 'I like to feed an apple and a carrot to the one horse while the cow eats asparagus.'


a, b, c, d = tag_matcher.process(sentence)

print('Original: {:s}\n'.format(a))
print('tagged:   {:s}\n'.format(b))
print('untagged: {:s}\n'.format(c))
print('Final:    {:s}\n'.format(d))
