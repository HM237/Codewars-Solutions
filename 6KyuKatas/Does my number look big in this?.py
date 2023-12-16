def narcissistic( value ):
  temp = []
  string = str(value)
  for i in string:
      a = int(i) ** int(len(string))
      temp.append(a)
  a = sum(temp)
  if a == value:
    return True
  else:
    return False
