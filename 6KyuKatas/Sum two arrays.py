def sum_arrays(array1,array2):
  arr1 = []
  arr2 = []
  sum = []
  if array1 == [] and array2 == []:
    return []
  elif array1 == []:
    array1.append(0)
  elif array2 == []:
    array2.append(0)
  for i in array1:
    arr1.append(str(i))
  for i in array2:
    arr2.append(str(i))
  arr1 = "".join(arr1)
  arr2 = "".join(arr2)
  c = int(arr1) + int(arr2)
  if c < 0:
    c = abs(c)
    for i in str(c):
      sum.append(int(i))
    sum[0] *= -1
  else:
    for i in str(c):
      sum.append(int(i))
  return sum
