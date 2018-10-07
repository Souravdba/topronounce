import os
import pip
from setuptools import setup


with open('requirements.txt') as f:
    requires = f.read().strip().split('\n')


setup(
    name='topronounce',
    version='0.2',
    author='abc',
    include_package_data=True,
    packages=['topronounce', 'topronounce.src','topronounce.test'],
    package_data={'topronounce.src':['topronounce/src/etc/*']},
    install_requires=requires,
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
)
