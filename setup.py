# -*- coding: utf-8 -*-
"""Setuptools for rpi2caster."""

from setuptools import setup, find_packages

with open('README.rst', 'r') as readme_file:
    long_description = readme_file.read()

clas = ['Development Status :: 2 - Development',
        'License :: OSI Approved :: MIT',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3 :: Only']

setup(name='rpi2caster_editor',
      version='0.1.dev1',
      description='Data editor for rpi2caster',
      long_description=long_description,
      url='http://github.com/elegantandrogyne/rpi2caster-data-editor',
      author='Christophe Slychan',
      author_email='krzysztof.slychan@gmail.com',
      license='MIT',
      zip_safe=True,
      include_package_data=True,
      classifiers=clas,
      install_requires=['pip > 1.5', 'click > 6.0'],
      keywords=['rpi2caster', 'typography'],
      packages=find_packages(exclude=['data', 'docs', 'tests']),
      entry_points={'console_scripts':
                    ['rpi2caster-editor = rpi2caster_editor.editor:main']})
