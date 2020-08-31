def dec_to_base(number, base):
    """
    Input: number is the number to be converted
           base is the new base  (eg. 2, 6, or 8)
    Output: the converted number in the new base without the prefix (eg. '0b')
    """
    remainder_stack = []

    while number > 0:
        remainder_stack.append(number % base)
        number = number // base
    
    return int(''.join(map(str, reversed(remainder_stack))))
