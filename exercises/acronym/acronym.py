import re
def abbreviate(words):
    result = words[0]
    res = re.findall(r'\W(\w)', words)
    result += ''.join(res)
    return result.upper()