
def power(b, e):
    
    pow = 1

    for i in range(abs(e)):
        pow = pow * b

    if e < 0:
        return 1 / pow

    return pow

if __name__ == "__main__":
    b = 3.0
    e = 5
    res = power(b, e)
    print(res)