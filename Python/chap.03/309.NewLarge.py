def ladd(u, v):
    n = len(u) if (len(u) > len(v)) else len(v)
    result = []
    carry = 0
    for k in range(n):
        i = u[k] if (k < len(u)) else 0
        j = v[k] if (k < len(v)) else 0
        value = i + j + carry
        carry = value // 10
        result.append(value % 10)
    if (carry > 0):
        result.append(carry)
    return result


def lsub(u, v):
    n = len(u) if (len(u) > len(v)) else len(v)
    result = []
    borrow = 0
    for k in range(n):
        i = u[k] if (k < len(u)) else 0
        j = v[k] if (k < len(v)) else 0
        value = i - j + borrow
        if (value < 0):
            value += 10
            borrow = -1
        else:
            borrow = 0
        result.append(value % 10)
    if (borrow < 0):
        print("음의 정수는 처리 못함")
    return result


def exp(u, m):
    if (u == [0]):
        return [0]
    else:
        return ([0]*m)+u


def div(u, m):
    if (len(u) < m):
        u.append(0)
    return u[m:len(u)]


def rem(u, m):
    if (len(u) < m):
        u.append(0)
    return u[0:m]


def lmult(u, v):
    i = u[0] if (0 < len(u)) else 0
    j = v[0] if (0 < len(v)) else 0
    value = i*j
    carry = value//10
    result = []
    result.append(value % 10)
    if (carry > 0):
        result.append(carry)
    return result


def prod2(u, v):
    n = len(u) if (len(u) > len(v)) else len(v)
    if (len(u) == 0 or len(v) == 0):
        # print(u, v, [0])
        return [0]
    elif (n <= threshold):
        return lmult(u, v)
    else:
        m = n//2
        x = div(u, m)
        y = rem(u, m)
        w = div(v, m)
        z = rem(v, m)
        r = prod2(ladd(x, y), ladd(w, z))
        p1 = prod2(x, w)
        p3 = prod2(y, z)
        p2 = lsub(r, ladd(p1, p3))
        return ladd(ladd(exp(p1, 2*m), exp(p2, m)), p3)


threshold = 1
u = [2, 3, 8, 7, 6, 5]
v = [3, 2, 7, 3, 2, 4, 9]


print(567832*9423723)
print(prod2(u, v)[::-1])
