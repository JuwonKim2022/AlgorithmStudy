a = [2, 5, 1, 9, 7]
print(a)
print(sorted(a))

b = 'zbdaf'
print(sorted(b))
print(''.join(sorted(b)))

# 덮어쓰는 형식의 sort(), 추가 공간 필요없음
a.sort()
print(a)

# 길이 순으로 (조건 넣기)
c = ['ccc', 'aaaa', 'd', 'bb']
print(sorted(c, key=len))

d = ['cde', 'cfc', 'abc']


def fn(s):
    return s[0], s[-1]


print(sorted(d, key=fn))
