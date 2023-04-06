a = dict()
a = {}

a = {'key1': 'val1', 'key2': 'val2'}
print(a)
a['key3'] = 'val3'
print(a)

# 예외처리
try:
    print(a['key4'])
except KeyError:
    print('존재하지 않는 키')

for k, v in a.items():
    print(k, v)

# 삭제
del a['key2']
print(a)
