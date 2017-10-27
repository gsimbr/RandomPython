import pytest


@pytest.fixture(scope="function")
def dependency_2():
    print "Setup dep_2 from test_03"
    return "dependency_2" + "star"


def test_03(dependency_2):
    print dependency_2


def test_03_2(dependency_2):
    print dependency_2
