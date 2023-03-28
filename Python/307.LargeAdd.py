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


u = [3, 2, 1]
v = [5, 4]
print(123 + 45)
print(ladd(u, v)[::-1])
print()
u = [2, 3, 8, 7, 6, 5]
v = [3, 2, 7, 3, 2, 4, 9]
print(567832 + 9423723)
print(ladd(u, v)[::-1])
