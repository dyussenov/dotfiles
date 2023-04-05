import re

def check_regex(text, regex, expected_result) -> bool:
    try:
        result = re.findall(regex, text)
    except re.error:
        return (False, 'invalid regex')

    expected_result = expected_result.split(',')

    result.sort()
    expected_result.sort()

    print(result, expected_result)
    return (result == expected_result, ', '.join(result))


if __name__ == '__main__':
    print(check_regex(
        '1 2 3 4 5 6 78 9',
        '[1-4]',
        '19.01.2018,01.09.2017'
        )
        )
