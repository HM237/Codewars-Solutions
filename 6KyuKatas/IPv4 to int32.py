def ip_to_int32(ip):
  arr = ip.split(".")
  binary_arr = []
  for i in arr:
      binary = bin(int(i))
      binary_value = str(binary[2:])
      if len(binary_value) < 8 : 
        binary_value= binary_value.zfill(8)
      binary_arr.append(binary_value)
  binary = ("".join(binary_arr))
  decimal = int(binary, 2)
  return decimal
