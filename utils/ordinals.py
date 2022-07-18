#
# This is to write ordinals with a proper suffix
# and provide the proper return when called

def ordinal_suffix(value):
    s = str(value)
    if s.endswith('11'):
        return 'th'
    elif s.endswith('12'):
        return 'th'
    elif s.endswith('13'):
        return 'th'
    elif s.endswith('1' or '01'):
        return 'st'
    elif s.endswith('2' or '02'):
        return 'nd'
    elif s.endswith('3' or '03'):
        return 'rd'
    return 'th'
    pass

def ordinal(value):
    return str(value) + ordinal_suffix(value)
