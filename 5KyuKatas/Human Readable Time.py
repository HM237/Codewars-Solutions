def make_readable(sec):
  hours = sec // 3600
  minutes = sec / 3600
  decimal = minutes - int(minutes)
  decimal = (decimal * 60)
  minutes = int(decimal)
  decimal = decimal - int(decimal)
  seconds = (decimal * 60)
  seconds = int(round(seconds, 0))
  return f'{hours:02}:{minutes:02}:{seconds:02}'
