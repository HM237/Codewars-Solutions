import re
def ipv4_address(address):
    regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
    if "\n" in address: return False
    elif(re.search(regex, address)): return True
    else: return False
