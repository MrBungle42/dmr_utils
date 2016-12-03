#!/usr/bin/env python

from setuptools import setup

def readme():
    with open('README.rst') as file:
        return file.read()

setup(name='dmr',
      version='0.10',
      description='ETSI DMR (Digital Mobile Radio) Teir II Utilities',
      long_description='Modules to disassemble and assemble DMR packets, including generating and decoding varoius FEC routines',
      classifiers=[
          'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)'
          'Programming Language :: Python :: 2.7'
          'Intended Audience :: Developers'
          'Natural Language :: English'
          'Operating System :: OS Independent'
          'Programming Language :: Python :: Implementation :: CPython'
          'Topic :: Communications :: Ham Radio'
          'Topic :: Software Development :: Libraries :: Python Modules'
          'Topic :: Utilities'
      ],
      keywords='dmr radio digital fec ecc mmdvm ham amateur radio',
      author='Cortney T. Buffington, N0MJS',
      author_email='n0mjs@me.com',
      url='https://www.python.org/sigs/distutils-sig/',
      install_requires=['bitarray'],
      license='GPLv3'
     )