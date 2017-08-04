"""
Taken from
https://docs.pytest.org/en/latest/proposals/parametrize_with_fixtures.html
"""

import operator
import pytest


FOSS_LICENSES = ['Apache 2.0', 'MIT', 'GPL', 'BSD']

PYTHON_PKGS = ['pytest', 'requests', 'django', 'cookiecutter']


class Package(object):
    def __init__(self, name, license):
        self.name = name
        self.license = license

    @property
    def is_open_source(self):
        return self.license in FOSS_LICENSES


class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self._skills = ['eating', 'sleeping']

    def learn(self, skill):
        self._skills.append(skill)

    @property
    def looks_like_a_programmer(self):
        return any(
            package in self._skills
            for package in PYTHON_PKGS
        )


class Woman(Person):
    def __init__(self, name):
        super(Woman, self).__init__(name, 'female')


class Man(Person):
    def __init__(self, name):
        super(Man, self).__init__(name, 'male')


PACKAGES = [
    Package('requests', 'Apache 2.0'),
    Package('django', 'BSD'),
    Package('pytest', 'MIT'),
]


@pytest.fixture(params=PACKAGES, ids=operator.attrgetter('name'))
def python_package(request):
    return request.param


@pytest.mark.parametrize('person', [
    Woman('Audrey'), Woman('Brianna'),
    Man('Daniel'), Woman('Ola'), Man('Kenneth')
])
def test_become_a_programmer(person, python_package):
    person.learn(python_package.name)
    assert person.looks_like_a_programmer


def test_is_open_source(python_package):
    assert python_package.is_open_source
