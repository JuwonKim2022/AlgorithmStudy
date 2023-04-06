a: str = '1'
b: int = 1

print(a)
print(b)


def fn(c: int) -> bool:
    result = c * 100
    if result > 100:
        return True
    else:
        return False
