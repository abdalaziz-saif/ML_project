from setuptools import find_packages, setup


HYPHEN_DOT = "-e ."

def get_requirements(file_path: str) -> list[str]:
    """
    Read requirements.txt and return a clean list of dependencies
    """
    requirements = []

    with open(file_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and line != HYPHEN_DOT:
                requirements.append(line)

    return requirements




setup(
name='ML_PROJECT',
version='0.0.1',
author='ABDALAZIZ',
author_email='abdazizsaif15@gmail.com',
packages=find_packages(),
install_requires=get_requirements("requirements.txt")

)