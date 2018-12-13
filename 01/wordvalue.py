from data import DICTIONARY, LETTER_SCORES
import string

def load_words():
  """Load dictionary into a list and return list"""
  with open(DICTIONARY) as f:
    return [x.strip() for x in f]
    

def calc_word_value(word):
  """Calculate the value of the word entered into function
  using imported constant mapping LETTER_SCORES"""
  return sum([LETTER_SCORES[letter.upper()] for letter in word if letter in string.ascii_letters])

def word_values(words):
  for word in words:
    yield(word, calc_word_value(word))

def max_word_value(words=None):
  """Calculate the word with the max value, can receive a list
  of words as arg, if none provided uses default DICTIONARY"""
  if words is None:
    words =load_words()

  return max(word_values(words), key=lambda x: x[1])[0]

if __name__ == "__main__":
  pass # run unittests to validate
