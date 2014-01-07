
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

## Word_Set

It looks to me that the class Word_Set should be a combination of the builtin Python
[`set`](http://docs.python.org/2/library/stdtypes.html#set) and
[`dict`](http://docs.python.org/2/library/stdtypes.html#dict).  This class will need to perform
the matching function for this task.  Match function input is a word, processing searches internal
data structures for match, return match if there is one, otherwise return None.

The Word_Set class needs to be initialized from some sort of config data.  I will store that in a
JSON file.  That will naturally lend itself to managing lists and dicts.

Testing for Word_Set: confirm that it can read its config data from a file.  Also confirm that it
is able to perform word matching for a number of scenarios: Class tag word is present/not present
in the test sentence.  Confirm method is robust to cases where sentence is empty, or other ...?

## Class_Tagger

This class is to be initialized with config data for various word set mappings.  Load config data.
Create internal Word_Set to manage tag mapping.

Main work method for this class to be one that accepts an input string of words, performs
pre-processing on string and split it up into a list of words.  For each word in the sentence,
call tag matching method on Word_Set object.  Maintain appropriate data structures to output
required sequence of four items.

Testing for Class_Tagger: Confirm that it initializes itself.  Confirm that it can correctly split
up a sentence into discrete words.  Confirm that it does NOT barf with extra punctuation??
Confirm that it does not barf with irregular whitespace, e.g. multiple space characters, tabs, etc.
Confirm internal data storage is correct after running matching function.  Confirm output
sequences are correct for a range of test cases.
