#найти самый большой палиндром из умножения 3х значных чисел  (913 * 993 = 906609) max998001

def is_palindrom(palindrom):
    str_palindrom = str(palindrom)
    return True if str_palindrom==str_palindrom[::-1] else False
    

a = b = 100
max_palindrom = 0

while a <= 999:
    while b <= 999:
        print(b)
        res = a*b
        max_palindrom = res if is_palindrom(res) else max_palindrom
        b+=1
    print(a)
    a+=1

print(max_palindrom)