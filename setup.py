from os.path import abspath, dirname, join, normpath

from setuptools import find_packages, setup

from asterisk import __version__ as version


LICENSES = (
    'Python Software Foundation License',
    'GNU Library or Lesser General Public License (LGPL)',
    'UNLICENSE',
)


setup(

    # Basic package information:
    name = 'asterisk-python',
    version = version,
    packages = find_packages(),

    # Packaging options:
    zip_safe = False,
    include_package_data = True,

    # Metadata for PyPI:
    author = 'Karl Putland',
    author_email='kputland@users.sourceforge.net',
    maintainer = 'Randall Degges',
    maintainer_email = 'rdegges@gmail.com',
    license = ', '.join(LICENSES),
    url = 'http://asterisk-python.readthedocs.org/en/latest/',
    keywords = 'telephony call phone voip asterisk pbx telephone pstn',
    description = 'A python interface to Asterisk.',
    long_description = open(normpath(join(dirname(abspath(__file__)),
         'README'))).read(),
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: Telecommunications Industry',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Communications :: Internet Phone',
        'Topic :: Communications :: Telephony',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ] + ['License :: OSI Approved :: ' + l for l in LICENSES],

)

