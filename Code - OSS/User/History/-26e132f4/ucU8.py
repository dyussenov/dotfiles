import re

def check_regex(text, regex, expected_result) -> bool:
    result = re.findall(regex, text).sort()
    expected_result = expected_result.split(',')
    return result == expected_result


if __name__ == '__main__':
    print(check_regex(
        'Дед мороз увидел мой сюрприз и сказал хохо! Хехе в этом было мало, но было забавно!',
        'хохо',
        'хохо'
        )
        )
    print([1,2,3].sort()==[3,2,1].sort())
