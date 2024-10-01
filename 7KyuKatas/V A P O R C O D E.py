def vaporcode(s):
    vapor = []
    for i in s:
        if i != ' ': vapor.append(i.upper())
    vapor = "  ".join(vapor)
    return vapor
