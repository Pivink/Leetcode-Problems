def divde(dividend,divisor):
    if divisor<0:
        div=dividend//(divisor*(-1))
        return min(max(-2147483647, div), 2147483647)
    return min(max(-2147483648, div), 2147483647)
print(divde(-2147483648,-3))