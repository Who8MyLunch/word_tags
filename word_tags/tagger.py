#!/usr/bin/python

from __future__ import division, print_function, unicode_literals

import word_set


class Tagger(object):
    def __init__(self, mapping):
        """Instantiate a Tagger object

        Parameters
        ----------
        mapping : dict, each key in mapping is a class tag.  The item for each tag is a sequence
                        of words that belong to that class.
        """

        self.word_set = word_set.Word_Set(mapping)

    def process(self, sentence):
        """Process a sentence.  Replace class words with class tag.
        """

        # Preprocess the sentence.
        punctation = '.,;:!?'
        for p in punctation:
            sentence = sentence.replace(p, ' ')

        words = sentence.split()
        words = [w.lower() for w in words]

        # List to hold intermediate data.
        words_tagged = []
        words_untagged = []
        words_new_sentence = []

        # Loop over words:
        for w in words:
            m = self.word_set.match(w)

            if m:
                # Keep track of word that matched a class.
                words_tagged.append(w)

                # Keep track of the class tag.
                words_new_sentence.append(m)
            else:
                # Keep track of words that did not match.
                words_untagged.append(w)

                # No match, don't store the tag, put the original word back in.
                words_new_sentence.append(w)

        # Build up final sentence strings.
        sentence_tagged = ' '.join(words_tagged)
        sentence_untagged = ' '.join(words_untagged)
        sentence_new = ' '.join(words_new_sentence)

        # Return the four reuired items.
        return sentence, sentence_tagged, sentence_untagged, sentence_new
