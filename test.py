def polynomial(data):
    coeffs = {}
    splits = map(str.strip, re.split(r"([+ \-])",data))
    sign = 1
    for p in splits:
        if p in "+-":
            sign = 1 if p == '+' else -1
            continue
        s = re.split('[^0-9]+', p)
        coeff = int(s[0])
        if len(s) == 1:
            pow = 0
        elif s[1] == '':
            pow = 1
        else:
            pow = int(s[1])
        coeffs[pow] = sign * coeff
    return coeffs

def derive(poly):
    return dict([(p-1, p*c) for p,c in poly.items() if p != 0])

def print_poly(poly, var = 'x'):
    print(''.join(['{0}{1}{2}^{3}'.format('+-'[c<0],c,var,p) for p,c in sorted(poly.items(), reverse = True)]))

print derive("x^4-2x^3+7x^2-16x+4")