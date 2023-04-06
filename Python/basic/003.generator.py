# 1. next()

def get_natural_number():
    n = 0
    while True:
        n += 1
        yield n


g = get_natural_number()
for _ in range(0, 100):
    print(next(g))


# 2. range()
print(list(range(5)))
