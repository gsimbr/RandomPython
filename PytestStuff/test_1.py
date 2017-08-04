import pytest


@pytest.fixture(scope="module", params=[1, 3, 5])
def fixture_1(request):
    yield "blabla" + str(request.param)


@pytest.fixture(scope="module")
def fixture_2(fixture_1):
    my_stringi = "haha"
    yield fixture_1 + my_stringi


def test_01(fixture_2):
    res = fixture_2
    assert res == "blabla1" + "haha"