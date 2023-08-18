from math import frexp, isfinite, isnan, nan, inf


def log(x: float) -> float:
    """Return the natural log of x"""
    # =================================================================
    # This algorithm uses the Taylor series for ln(1+y) - ln(1-y) to
    # calculate the value of ln(x). The argument is reduced using the
    # frexp() function from the math module, which reduces a number to
    # r * 2**p, where 0.5 <= r < 1.0. The reduced value r is then
    # plugged into the Taylor series as y = (r-1)/(r+1):
    #
    #     ln(1+y) - ln(1-y) = 2*(y + y**3/3 + y**5/5 +  ... + y**31/31)
    #
    # 16 terms is enough to get an answer within double-precision
    # floating point accuracy (which is what Python uses). This is
    # because our reduction algorithm gives us an input with an
    # absolute value of at most 1/3 (~2**-1.58), and the smallest term
    # is less than floating point error:
    #
    #     (2**-1.58)**31/31 = 2**-48.98/31 = 2**-52.98/1.9 < 2**-53
    # =================================================================

    ln2_hi = 6.93147180369123816490e-01  # 0x3fe6 2e42 fee0 0000
    ln2_lo = 1.90821492927058770002e-10  # 0x3dea 39ef 3579 3c76

    if not isfinite(x):
        if isnan(x):
            return x
        elif x > 0:  # positive infinity
            return x
        else:  # Negative infinity
            raise ValueError("math domain error")

    if x <= 0.0:
        raise ValueError("math domain error")

    if x == 1.0:
        return 0.0

    if x > 2 or x < 0.5:
        r, p = frexp(x)
    else:
        r, p = x, 0

    a = (r-1)/(r+1)
    a2 = a*a
    T = 0
    # Horner's method applied to Taylor series
    for i in range(31, 2, -2):
        T = a2*(2/i + T)

    answer = p*ln2_hi + 2*a + (a*T + p*ln2_lo)

    return answer
