#найти самый большой палиндром из умножения 3х значных чисел  (913 * 993 = 906609) max998001

def is_palindrom(palindrom):
    str_palindrom = str(palindrom)
    return True if str_palindrom==str_palindrom[::-1] else False
    

a = 100
b = 100
max_palindrom = 0

while a <= 999:
    while b <= 999:
        res = a*b
        max_palindrom = res if is_palindrom(res) else max_palindrom if max_palindrom<res else max_palindrom
        b+=1
    print('a:', a)
    print('b:', b)
    a+=1
    b = 100

print(max_palindrom)