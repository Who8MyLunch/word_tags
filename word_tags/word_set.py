#!/usr/bin/python

from __future__ import division, print_function, unicode_literals


class Word_Set(object):
    def __init__(self, mapping):
        """Instantiate a new Word_Set object.

        Parameters
        ----------

        mapping : dict, each key in mapping is a class tag.  The item for each tag is a sequence
                        of words that belong to that class.
        """

        self.mapping = {}
        for tag, words in mapping.items():
            tag = tag.upper()

            words = [w.lower() for w in words]
            words = set(words)

            self.mapping[tag] = words

    @property
    def tags(self):
        """Helpful property returning tags managed by this class.
        """
        return self.mapping.keys()

    def word_match(self, word_test):
        """Find tag that maps to a set of words that contains the input word.
        Return found tag, otherwise return None.

        Parameters
        ----------

        word_test : string, a word that might belong to a class.
        """

        # Remove leading/trailing whitespace, convert to lower case.
        word_test = word_test.strip().lower()

        # Look for a match.
        for tag, words in self.mapping.items():
            if word_test in words:
                return tag

        # If we get here, then there were no matches.
        return None
