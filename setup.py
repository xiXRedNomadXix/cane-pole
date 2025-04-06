from setuptools import setup

setup(
    name='cane-pole',
    version='0.1',
    py_modules=['cane_pole'],
    install_requires=[
        'scapy',
        'pyroute2',
    ],
    entry_points={
        'console_scripts': [
            'cane-pole=cane_pole:main',
        ],
    },
)
