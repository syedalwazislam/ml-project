from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = "-e ."


def get_requirements(file_path:str) -> List[str]:
    requirements = []
    with open(file_path) as fileobj:
        requirements = fileobj.readlines()
        requirements = [req.replace("\n", " ") for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements


setup(
    name='ml-project',
    version='0.0.1',
    author='Alwaz',
    author_email='syedalwaz007@gmail.com',
    install_requires = get_requirements('requirements.txt')
    )