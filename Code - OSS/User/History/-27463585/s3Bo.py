#найти самый большой палиндром из умножения 3х значных чисел  (913 * 993 = 906609) max998001

def is_palindrom(palindrom):
    str_palindrom = str(palindrom)
    return True if str_palindrom[:3]==str_palindrom[3:] else False
    


print(is_palindrom(100001))