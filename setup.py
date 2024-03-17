from setuptools import find_packages,setup
from typing import List
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"
REPO_NAME = "end-end-MLP-with-MLFlow"
AUTHOR_USER_NAME = "Vishal Ganapathy"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "vishalganpathy@gmail.com"

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements
setup(
name="IDS_CICIDS17",
version={__version__},
author={AUTHOR_USER_NAME},
author_email={AUTHOR_EMAIL},
packages=find_packages(),
install_requires=get_requirements("requirements.txt")
)
