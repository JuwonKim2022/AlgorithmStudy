print(5/3)
print(int(5/3))

print(5//3)
print(5 % 3)

print('A1', 'B1')
print('A1', 'B1', sep=',')

# 줄바꿈
print('A1', end=' ')
print('B1')
# 리스트화 해서 출력
a = ['A', 'B']
print(','.join(a))

idx = 1
fruit = "Apple"
print('{0} -> {1}'.format(idx+1, fruit))
print('{} --> {}'.format(idx+1, fruit))
# f 이용
print(f'{idx+1} ---> {fruit}')
