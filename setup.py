from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements (file_path:str)-> List[str]:
    """
    This funcion will return the list of requirements
    """

    requirements=[]
    with open(file_path)  as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)





setup (
    name = 'mlproject',
    verison='0.0.1',
    author= 'Navneet',
    author_email= 'navneet.priya@hotmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirement.txt')

)