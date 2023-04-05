import re

def check_regex(text, regex, expected_result) -> bool:
    result = re.findall(regex, text)
    expected_result = expected_result.split(',')

    result.sort()
    expected_result.sort()

    return result == expected_result


if __name__ == '__main__':
    print(check_regex(
        'Бирюзовый цвет: #ABCDEF, розовый цвет: #d3CDEF',
        '/^#(?:[0-9a-f]{3}){1,2}$/i',
        '#ABCDEF,#d3CDEF'
        )
        )
