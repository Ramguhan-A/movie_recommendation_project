from setuptools import setup,find_packages
from typing import List

def get_requirements(file_path:str) -> list[str]:
    requirements = []
    try:
        with open(file_path,'r') as file_obj:
            requirements = file_obj.read().splitlines()
    except FileNotFoundError:
        print(f"Error: Requirements file not found at {file_path}")
        return[]
    return requirements

setup (
    name = "Movie Recommendation Project",
    version = "0.0.1",
    author = "Ramguhan A",
    author_email= "ramguhan99gmail.com",
    packages=find_packages(where="src"),
    package_dir={'':'src'},
    install_requires= get_requirements("requirements.txt"),
    description="A machine learning project"
        
)