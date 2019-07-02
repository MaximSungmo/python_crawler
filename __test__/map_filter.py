a = [1, 2, 3, 4]

# iterator 객체로 만들어졌으므로 next(lst)를 통해서 실행할 수 있음
lst = map(lambda x: print(x**2), a)
next(lst)
next(lst)
next(lst)
next(lst)
print('------------------------------------\n')

# list 안에 iterator로 만들어진 객체가 담기며 list 형식으로 변환해줌, 따라서 list로 실행할 수 있음
lst = list(map(lambda x: x**2, [1, 2, 3, 4]))
print(lst)

# for i in lst:
    # i


# filter
# 조건에 맞는 지 확인해서 iterator로 만들어진 객체가 담기며 list로 담아줘서 실행함
lst = list(filter(lambda x: x % 2 ==0, [1, 2, 3, 4]))
print(lst)



# lambda 표현
def f(x):
    return x**2