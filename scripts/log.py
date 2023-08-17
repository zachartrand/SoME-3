from math import frexp, isfinite, isnan, nan, inf


def log(x: float) -> float:
    """Return the natural log of x"""
    # =================================================================
    # This algorithm uses the Taylor series for ln(1+y) to calculate
    # the value of ln(x). The argument is reduced using the frexp()
    # function from the math module, which reduces a number to
    # r * 2**p, where 0.5 <= r < 1.0. The reduced value r is then
    # plugged into the Taylor series as y = r - 1:
    #
    #     ln(1+y) = y - y**2/2 + y**3/3 - y**4/4 + ... - y**48/48
    #
    # 48 terms is enough to get an answer within double-precision
    # floating point accuracy (which is what Python uses). This is
    # because our reduction algorithm has an input with an absolute
    # value of at most 0.5 (or 2**-1), and the smallest term is less
    # than floating point error:
    #
    #     (2**-1)**48/48 = 2**-48/48 = 2**-53/1.5 < 2**-53
    # =================================================================

    ln2 = 0.6931471805599453

    if not isfinite(x):
        if isnan(x):
            return x
        elif x > 0:  # positive infinity
            return x
        else:  # Negative infinity
            raise ValueError("math domain error")

    if x <= 0.0:
        raise ValueError("math domain error")

    r, p = frexp(x)
    a = r - 1
    answer = 0
    # Horner's method applied to Taylor series
    for i in range(48, 0, -1):
        answer = a*(1/i - answer)

    answer += p*ln2  # Rescale.

    return answer
