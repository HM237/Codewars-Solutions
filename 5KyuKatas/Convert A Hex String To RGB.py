def hex_string_to_RGB(hex_string): 
    hex_string = hex_string.replace("#", "")
    hexes = [hex_string[0:2], hex_string[2:4], hex_string[4:6]]
    rgb = {"r": 0,
           "g": 0,
           "b": 0}
    n = 0
    for keys, values in rgb.items():
        rgb[keys] = int(format(int(hexes[n], 16), 'd'))
        n +=1
    return rgb
