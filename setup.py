from setuptools import setup, find_packages

base_requirements = [
    "fastapi>=0.70.0",
    "uvicorn>=0.15.0",
    "prometheus-client>=0.12.0",
    "scikit-learn>=1.0.1",
]

dev_requirements = {

}

setup(
    name="scikitProm",
    author="Harm-Jan Setz",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=base_requirements,
    extras_require=dev_requirements,
)