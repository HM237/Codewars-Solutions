def format_duration(seconds):
    if seconds == 0: return "now"
    format = []
    #Used a dictionary method
    times = {"year":31536000, "day": 86400, "hour": 3600, "minute": 60, "second":1}
    #divmod just does both of them at the same time
    for unit, value in times.items():
        count,seconds = divmod(seconds, value)
        if count == 1:
            format.append(f'{count} {unit}')
        if count >1:
            format.append(f'{count} {unit}s')
            
    #Unpacking the format. The * leaves only one thing separating first from last
    *first, last = format
    if not first:
        return last
    else:
        return f"{', '.join(first)} and {last}"
