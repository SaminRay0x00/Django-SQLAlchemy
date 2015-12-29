
from setuptools import setup, find_packages
import sys

userena = __import__('userena')

readme_file = 'README.md'
try:
    long_description = open(readme_file).read()
except IOError, err:
    sys.stderr.write("[ERROR] Cannot find file specified as "
        "``long_description`` (%s)\n" % readme_file)
    sys.exit(1)

setup(name='django-userena',
      version=userena.get_version(),
      description='Complete user management application for Django',
      long_description=long_description,
      zip_safe=False,
      author='Ramin Farajpour Cami',
      author_email='ramin.blackhat@gmail.com',
      url='https://github.com/RaminFP/Django-SQLAlchemy',
      download_url='https://github.com/RaminFP/Django-SQLAlchemy/downloads',
      packages = find_packages(exclude=['demo', 'demo.*']),
      include_package_data=True,
      install_requires = [
        'django==1.8.7',
        'SQLAlchemy',
       
      ],
      test_suite='tests.main',
      classifiers = ['Development Status :: 1',
                     'Environment :: Web Environment',
                     'Framework :: Django',
                     'Intended Audience :: Developers',
                     'License :: OSI Approved :: BSD License',
                     'Operating System :: OS Independent',
                     'Programming Language :: Python',
                     'Topic :: Utilities'],
