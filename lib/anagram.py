# your code goes here!
class Anagram:
   def __init__(self, word):
      self.set_word(word)

   def set_word(self, word):
      self._word = word
   
   def get_word(self):
      return self._word

   def match(self, matchable):
      matches = []
      for m in matchable:
         if sorted(self.get_word())== sorted(m):
            matches.append(m)
      return matches

   word = property(get_word, set_word)