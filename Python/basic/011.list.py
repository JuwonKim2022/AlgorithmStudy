# 리스트 선언
a = list()
b = [1, 2, 3]
b.append(4)
print(b)
b.insert(2, '안녕')
b.append(True)
print(b)
print(b[2])
print(b[1:6:2])

# 존재하지 않는 리스트 예외처리
try:
    print(a[9])
except IndexError:
    print('존재하지 않는 리스트')

# del : 인덱스 위치 삭제
del b[3]
print(b)

# remove : 해당 값을 삭제
b.remove('안녕')
print(b)
