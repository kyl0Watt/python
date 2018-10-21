def rebase(input_base, digits, output_base):           # TODO make it work!
    if input_base or output_base <= 0:
        raise ValueError('something go wrong')
    d = ''
    for i in digits:
        if 0 <= i < 10:
            d += str(i)
        elif i == 10:
            d += 'a'
        elif i == 11:
            d += 'b'
        elif i == 12:
            d += 'c'
        elif i == 13:
            d += 'd'
        elif i == 14:
            d += 'e'
        elif i == 15:
            d += 'f'
        else:
            raise ValueError('something fo wrong')
    in_dec = int(d, base=input_base)
    result = []
    while in_dec:
        in_dec, r = divmod(in_dec, output_base)
        result.append(r)
    result.reverse()
    return result