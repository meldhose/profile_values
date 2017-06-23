import subprocess
import sys
import os
import setuptools

# check if pip is installed. If not, raise an ImportError
PIP_INSTALLED = True

try:
    import pip
except ImportError:
    PIP_INSTALLED = False

if not PIP_INSTALLED:
    raise ImportError('pip is not installed.')


def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)


# Checking and installing the required packages
install_and_import('pandas')
install_and_import('numpy')

# find packages to be included.
packages = setuptools.find_packages()

with open('README.md') as f:
    LONG_DESCRIPTION = f.read()

setuptools.setup(
    name='profile_values',
    version='0.2.1',
    description='Python library for data profiling.',
    long_description=LONG_DESCRIPTION,
    url='',
    author='Meera George',
    author_email='meera@cs.wisc.edu',
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Scientific/Engineering',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries',
    ],
    packages=packages,
    install_requires=[
        'numpy >= 1.7.0',
        'six'
    ],
    setup_requires=[
        'numpy >= 1.7.0'
    ],
    include_package_data=True,
    zip_safe=False
)