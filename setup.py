from setuptools import setup

setup(
    name='ipregex',
    version='0.1',
    author='Omer F. Ozarslan',
    author_email='omer@utdallas.edu',
    packages=['ipregex'],
    url='http://github.com/ozars/ipregex/',
    license='LICENSE',
    description=('Provides regular expression for IPv4/IPv6 addresses.'),
    long_description=open('README.rst').read(),
    setup_requires=[
        'pytest_runner',
    ],
    tests_require=[
        'pytest',
    ]
)

