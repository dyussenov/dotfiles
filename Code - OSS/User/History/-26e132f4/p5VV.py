import re

def check_regex(text, regex, expected_result) -> bool:
    result = re.findall(regex, text)
    return result


if __name__ == '__main__':
    print(check_regex(
        'Дед мороз увидел мой сюрприз и сказал хохо! Хехе в этом было мало, но было забавно!',
        'хохо',
        'хохо'
        )
        )

