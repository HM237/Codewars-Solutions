def greatest_product(n):
  max = 0
  for i in range(len(n)+1):
      product = 1
      for x in n[i:i+5]:
         if len(n[i:i+5]) < 5 or "0" in n[i:i+5]:
             break
         product = product * int(x)
      if product > max and product != 1: max = product
  return max
