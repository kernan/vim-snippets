import re

def to_camel(s, upper = False):
    if len(s) == 0:
        return s
    r = re.sub(r'(?!^)_([a-zA-Z])', lambda m: m.group(1).upper(), s)
    if upper:
        if len(s) == 1:
            return r[0].upper()
        else:
            return r[0].upper() + r[1:]
    else:
        if len(s) == 1:
            return r[0].lower()
        else:
            return r[0].lower() + r[1:]

def to_snake(s):
    if len(s) == 0:
        return s
    r = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', s)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', r).lower()

if __name__ == '__main__':
    print(to_camel('getHTTPResponseCode'))
    print(to_camel('getHTTPResponseCode', True))
    print(to_camel('getHTTPResponseCode'))
    print(to_camel('get_http_response_code', True))
    print(to_snake('getHTTPResponseCode'))
    print(to_snake('get_http_response_code'))
