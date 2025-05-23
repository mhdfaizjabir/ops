from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        # Remove newlines and extra whitespace, and filter out empty strings
        requirements = [req.strip() for req in requirements if req.strip()]
        # Remove '-e .' if present
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements

 
setup(
    name="pydantic-typing",
    version="0.0.1",
    author="faiz",
    author_email="faizjabir003@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)