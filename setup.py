from setuptools import setup, find_packages
from typing import List

''' This file define the package metadata and dependencies. It specifies the package name, version and author information, 
as well as the dependencies required to install the package (in this case, the qadence library). 
The find_packages() function is used to automatically discover and include 
all packages in the src directory'''

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''This function will return the list of requirements'''
    requirements = []
    with open('requirements.txt') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='qir-project',
    version='1.0',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages(),
    author='Kassu Gebresellasie',
    author_email='kassu.gebresellasie@gmail.com',
    description='A Quantum Intermediate Representation (QIR) compiler and runner',
    long_description='This package provides a QIR compiler and runner using the Qadence framework.',
    url='https://github.com/KassuBG/qir-project',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)