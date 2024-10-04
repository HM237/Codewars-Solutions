import re
def is_valid_IP(string):
    regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
    if "\n" in string: return False
    elif(re.search(regex, string)): return True
    else: return False
