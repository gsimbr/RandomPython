import argparse
import pytest
import os

HERE = str(os.path.dirname(__file__))


def test_01():
    """
    This is a running test.
    """
    assert True


def test_no_execute():
    """
    This is a failing test.
    """
    assert False


def cmd_line_parse():
    parser = argparse.ArgumentParser(
        description="Parses pytest args")
    parser.add_argument(
        "--run-tests",
        help="The test names to be contained in the tests if they are to be "
             "executed",
        default=None)
    args = parser.parse_args()
    return args


def main():
    args = cmd_line_parse()
    run_tests = args.run_tests
    pytest_args = ['-x', HERE, "--pdb"]

    if run_tests:
        pytest_args.extend(["-k", run_tests])

    pytest.main(pytest_args)


if __name__ == '__main__':
    main()
