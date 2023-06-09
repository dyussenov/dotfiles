import re

def check_regex(text, regex, expected_result) -> bool:
    result = re.findall(regex, text)
    expected_result = expected_result.split(',')

    result.sort()
    expected_result.sort()

    print(result, expected_result)
    return (result == expected_result, ''.join(result))


if __name__ == '__main__':
    print(check_regex(
        'Эта строка написана 19.01.2018, а могла бы и 01.09.2017',
        r'\d\d\.\d\d\.\d{4}',
        '19.01.2018,01.09.2017'
        )
        )
