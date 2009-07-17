import os

from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

requires = [
    'setuptools',
    'pysqlite',
    'SQLAlchemy',
    'z3c.saconfig',
    'zope.sqlalchemy',
    'pysqlite'
    ]

setup(name='pas.plugins.sqlalchemy',
      version='0.1dev',
      description="SQLAlchemy-based PAS user/group/prop store.",
      long_description=read("README.txt") + '\n\n' +  read("CHANGES.txt"),
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='Malthe Borch and Stefan Eletzhofer',
      author_email="stefan.eletzhofer@inquant.de",
      license="GNU GPL v2",
      keywords='web pas plone',
      package_dir = {'': 'src'},
      packages=find_packages("src"),
      include_package_data=True,
      namespace_packages=['pas', 'pas.plugins'],
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="pas.plugins.sqlalchemy",
      )
