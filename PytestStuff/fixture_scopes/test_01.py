import pytest


@pytest.fixture
def dependency_1():
    return "dependency_1"


@pytest.fixture(scope="session")
def dependency_2():
    print "Setup dep_2 from test_01"
    return "depencency_2"


@pytest.fixture
def to_override_fixture(dependency_1, dependency_2):
    return dependency_1 + " " + dependency_2


def test_01(to_override_fixture):
    print to_override_fixture
