import pytest


@pytest.fixture(scope="module")
def dependency_3():
    return "dependency_3"


@pytest.fixture
def to_override_fixture(dependency_3):
    return dependency_3


def test_02(to_override_fixture):
    print to_override_fixture
