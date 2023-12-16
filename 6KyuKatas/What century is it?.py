def what_century(year):
  cent = int(year[0:2])
  newcent = cent + 1
  end = int(year[2:])
  second_digit = int(year[1])
  if end == 00:
      if int(year[0]) == 1:
          century = ""
          century = str(cent) + "th"
      elif second_digit == 1:
          century= ""
          century = str(cent) + "st"
      elif second_digit == 2:
          century = ""
          century= str(cent) + "nd"
      elif second_digit == 3:
          century = ""
          century= str(cent) + "rd"
      else:
          century= ""
          century= str(cent) + "th"
      return century
  elif str(newcent)[0] == "1":
    century = ""
    century = str(newcent) + "th"
    return century
  elif str(newcent)[1] == "1":
    century = ""
    century = str(newcent) + "st"
    return century 
  elif str(newcent)[1] == "2":
    century = ""
    century = str(newcent) + "nd"
    return century
  elif str(newcent)[1] == "3":
    century = ""
    century = str(newcent) + "rd"
    return century
  else:
    century = ""
    century = str(newcent) + "th"
    return century
