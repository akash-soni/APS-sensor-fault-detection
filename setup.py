from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    """
    This function will return list of requirements
    """
    HYPEN_E_DOT = "-e ."
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements: # when running requirements.txt it will ignore -e . as we already have setup.py which will build setup for us
            requirements.remove(HYPEN_E_DOT)
    requirements_list:List[str] = [requirements]
    return requirements_list

setup(
    name="sensor",
    version="0.01",
    author="ineuron",
    author_email="akash.soni@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)