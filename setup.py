from setuptools import setup

setup(
    name='ipregex',
    version='0.1.2',
    author='Omer F. Ozarslan',
    author_email='omer@utdallas.edu',
    packages=['ipregex'],
    url='http://github.com/netmes/ipregex/',
    license='Apache Software License (Apache 2.0)',
    description=('Provides regular expression for IPv4/IPv6 addresses.'),
    long_description=open('README.rst').read(),
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: System :: Networking',
    ],
)

