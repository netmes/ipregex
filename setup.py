from setuptools import setup
import os

here = os.path.abspath(os.path.dirname(__file__))

about = {}
with open(os.path.join(here, 'ipregex', '__version__.py'), 'r') as f:
    exec(f.read(), about)

with open(os.path.join(here, 'README.rst'), 'r') as f:
    readme = f.read()

setup(
    name='ipregex',
    version=about['__version__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    packages=['ipregex'],
    url=about['__url__'],
    license=about['__license__'],
    description=about['__description__'],
    long_description=readme,
    long_description_content_type='text/x-rst',
    python_requires='>=2.6, !=3.0.*, !=3.1.*, !=3.2.*',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: System :: Networking',
    ],
)

