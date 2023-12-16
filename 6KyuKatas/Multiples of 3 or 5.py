def solution(number):
  array = []
  if number < 0 :
    return 0
  for i in range (number) :
    if i % 3 == 0 and i % 5 == 0:
      array.append(i)
    elif i % 3 == 0:
      array.append(i)
    elif i % 5 == 0:
      array.append(i)
  return sum(array)
