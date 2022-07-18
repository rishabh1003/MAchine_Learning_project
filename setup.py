from setuptools import setup
from typing import List 

def get_requirements_list()->List[str]:
    """ Description: This function is going to return list of 
    requirements mention in requirements.txt file 
    """
    with open("requirements.txt") as requirement_file:
        return requirement_file.readlines()


setup(
    name="housing-predictor",
    version="0.0.1",
    author="Rishabh Gupta",
    packages=["housing"],
    install_requires=get_requirements_list()

)


if __name__=="__main__":
    print(get_requirements_list())