#найти самый большой палиндром из умножения 3х значных чисел  (913 * 993 = 906609) max998001

def is_palindrom(palindrom):
    str_palindrom = str(palindrom)
    return True if str_palindrom==str_palindrom[::-1] else False



max_multiplier = int(input('введите максимальный множитель: '))

max_palindrom = 0
max_a = 0
max_b = 0

for a in range(1, max_multiplier+1):    
    for b in range(a, max_multiplier+1):
        res = a*b
        if is_palindrom(res) and res > max_palindrom:
            max_a = a
            max_b = b
            max_palindrom = res

print(max_palindrom)

with open('history.txt', 'w+') as file:
    file.write(f'Multiply-limit = {max_multiplier} \n The biggest number is: {max_a} * {max_b} = {max_palindrom} \n')
