def max_and_min(arr1,arr2):
  temp = []
  diff = []
  for i in arr1 :
    a= i
    for i in arr2:
      b = a- i
      if b < 0:
        b= -b
        temp.append(b)
      else:
        temp.append(b)
  diff.append(max(temp))
  diff.append(min(temp))
  return diff
