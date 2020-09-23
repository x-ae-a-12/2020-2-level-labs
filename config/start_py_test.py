# pylint: skip-file

import argparse
import re
import sys


def check_assert_is_in_file(content: str):
    print(content)
    expected = 'assert RESULT'
    actual = re.findall(expected, content)
    if expected == actual or expected in content:
        return 0
    return 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Checks start.py files and tests them')
    parser.add_argument('--start_py_content', type=str, help='Content of start.py for each lab')
    args: argparse.Namespace = parser.parse_args()

    result = check_assert_is_in_file(args.start_py_content)
    if result == 1:
        print('Make sure you made assert RESULT in start.py file')
        sys.exit(result)
    print('Passed')
    sys.exit(result)

# Test: a) assert concordance_realize is in file
# Test: b) call start.py, expect it does not throw Error
