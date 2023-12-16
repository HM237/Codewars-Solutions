import heapq
import re
def top_3_words(text):
  words = []
  occurences = []
  result = []
  text = text.lower()
  text = re.sub("[^a-zA-Z']+"," ", text)
  if len(text) == 0: 
    return result
  text = text.split()
  for i in text:
    if i not in words:
      words.append(i)
  for i in words:
    counter = text.count(i)
    occurences.append(counter)
  if len(occurences) <= 3:
    indexes = heapq.nlargest(3, range(len(occurences)), occurences.__getitem__)
    for i in indexes:
      word = words[i]
      result.append(word)
  else:
    indexes = heapq.nlargest(3, range(len(occurences)), occurences.__getitem__)
    for i in indexes:
      word = words[i]
      result.append(word)
  if "'''" in result or "'" in result :
    return []
  else:
    return result
