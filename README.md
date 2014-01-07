
# Word_Tags

Text processing example

## Word_Set List object

Holds one or more sets of words and maps each set to a string

set of words: {apple, pear, cherry} mapped to the string FRUIT

## Class-Tagged Sentence Object

Accept as input a string of words.

String must be converted to lowercase.

Data processing search through inut string for occurances of words from each Word_Set.  That
word in the sentence is replaced by the corresponding class name.

Output from processing function is to be four items:

 - The original sentence
 - The subset of input words that **matched** to any of the Word_Sets
 - The subset of input words that did **not match** to any element of a Word_Set
 - The fully-processed input string, where each matched word is replaced with its
   corresponding tag.


# Brainstorming

## Recap

I understand the problem.  Breaking up a string into individual words.  Matching input words
with special predefined sets of words.  Each set represents a grouping of some type.  A group of
words for fruit, or a group of words for numbers, or a group of words for people names.  Processing
entails swapping out original input words with the class name for the set the word belongs.

## Functionality

It looks to me that the class Word_Set should be a combination of the builtin Python `set` [type](http://docs.python.org/2/library/stdtypes.html#set) and `dict` [type](http://docs.python.org/2/library/stdtypes.html#dict).

