import re

def check_regex(text, regex, expected_result) -> bool:
    print(regex)
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
        'aa aba abba abbba abca abea',
        r'\b(ab)?a\b',
        'aa,aba'
        )
        )
