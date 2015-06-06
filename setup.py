#!/usr/bin/env python

from distutils.core import setup

setup(name='Gluino3',
      version='0.4',
      description='port of web2py libs to bottle, flask, pyramid, tornado (includes copy of modules from the web2py framework)',
      author='Massimo Di Pierro',
      author_email='massimo.dipierro@gmail.com',
      license='lgpl',
      url='https://github.com/hipercenter/gluino3',
      packages=['gluino'],
      package_dir={'gluino': 'gluino'},
      )

