def square_digits(num):
  temp = []
  for i in str(num):
      a = str(int(i) ** 2)
      temp.append(a)
  n ="".join(temp)
  n = int(n)  
  return n
