import os
import pip
from setuptools import setup


requires = []
requirements = pip.req.parse_requirements('requirements.txt',session=pip.download.PipSession())

for item in requirements:
    if getattr(item, 'url', None):  # older pip has url
        links.append(str(item.url))
    if getattr(item, 'link', None): # newer pip has link
        links.append(str(item.link))
    if item.req:
        requires.append(str(item.req))

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
