def create_phone_number(n):
  temp = []
  for i in n:
    s = str(i)
    temp.append(s)
  string = "".join(temp)
  a = string[:3]
  b = string[3:6]
  c = string[6:10]
  return f'({a}) {b}-{c}'
