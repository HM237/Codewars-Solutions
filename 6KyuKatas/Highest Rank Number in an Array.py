def highest_rank(arr):
  numbers = []
  temp = []
  highest = []
  frequency = []
  indexes = []
  for i in arr:
    occurence = arr.count(i)
    if occurence >= 1:
      temp.append(i)
  for i in temp:
    if i not in numbers:
      numbers.append(i)
  for i in numbers:
    counts = arr.count(i)
    frequency.append(counts)
  maximum =max(frequency)
  for i in range (len(frequency)):
    if frequency[i] == maximum:
      indexes.append(i)
  for i in indexes:
    a= numbers[i]
    highest.append(a)
  highest_value = max(highest)
  return highest_value  
