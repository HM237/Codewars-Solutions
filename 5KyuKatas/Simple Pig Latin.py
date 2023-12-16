def pig_it(text):
  temp = []
  for i in text.split():
    if i in "!?":
      temp.append(i)
    else:
      a = ""
      b = i[0]
      c = i[1:]
      a = c +b + "ay"
      temp.append(a)
  return " ".join(temp)
