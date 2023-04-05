#найти самый большой палиндром из умножения 3х значных чисел  (913 * 993 = 906609) max998001

def is_palindrom(palindrom):
    str_palindrom = str(palindrom)
    return True if str_palindrom==str_palindrom[::-1] else False
    

max_palindrom = 0

for a in range(100,999):
    for b in range(100,999):
        res = a*b
        if is_palindrom(res) and res > max_palindrom:
            max_palindrom = res

print(max_palindrom)
