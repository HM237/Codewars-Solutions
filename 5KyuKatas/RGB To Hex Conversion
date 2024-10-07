def rgb(r, g, b):
    array = [r , g, b]
    rgb = []
    for value in array:
        if abs(value) != value: rgb.append("00")
        elif value > 255 : rgb.append("FF")
        else:
            hex_value = (hex(value)[2:]).upper()
            if len(hex_value) < 2 : rgb.append(hex_value.zfill(2))
            else: rgb.append(hex_value)
    return "".join(rgb)
