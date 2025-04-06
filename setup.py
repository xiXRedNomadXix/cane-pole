from setuptools import setup, find_packages

setup(
    name="cane-pole",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "scapy",
        "pyroute2",
    ],
    entry_points={
        "console_scripts": [
            "cane-pole=cane_pole.main:run",
        ],
    },
)
