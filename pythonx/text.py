import re

def to_camel_case(s):
    if len(s) == 0:
        return s
    s = s[0].lower() + s[1:]
    return re.sub(r'(?!^)_([a-zA-Z])', lambda m: m.group(1).upper(), s)

def to_pascal_case(s):
    s = to_camelCase(s);
    return s[0].upper() + s[1:]


def to_snake_case(s):
    if len(s) == 0:
        return s
    s = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', s)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s).lower()

def to_capitals_case(s):
    return to_snake_case(s).upper()
