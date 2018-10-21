import gmpy


alphabet = 'abcdefghijklmnopqrstuvwxyz'         # TODO: make it norm
alen = len(alphabet)


def encode(plain_text, a, b):
    if a % 2 == 0:                              # not solution
        raise ValueError('somwthing wrong')
    result = []
    counter = 0
    for i in plain_text.lower():
        if counter == 5:
            result += ' '
            counter = 0
        if i in '0123456789':
            result += i
            counter += 1
        elif i in alphabet:
            index = alphabet.index(i)
            new_index = (a*index + b) % alen
            result += alphabet[new_index]
            counter += 1
        else:
            continue
        if result[-1] == ' ':
            result.pop()
    if ''.join(result)[-1] == ' ':
        return ''.join(result)[:-1]         # this is mistake
    return ''.join(result)


def decode(ciphered_text, a, b):
    if len(alphabet) % a == 0:
        raise ValueError('it wrong')      # this is mistake tooo
    result = []
    for i in ciphered_text:
        if i in '0123456789':
            result += i
        elif i in alphabet:
            index = alphabet.index(i)
            ni = int(gmpy.invert(a, alen)) / (index - b) % alen
            result += alphabet[ni]
        else:
            continue
    return ''.join(result)
