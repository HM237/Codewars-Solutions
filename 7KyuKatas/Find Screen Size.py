def find_screen_height(width, ratio): 
    ratio = ratio.split(":")
    height = int((width / int(ratio[0])) * int(ratio[1]))
    return f'{width}x{height}'
