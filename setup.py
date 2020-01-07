import os
import pathlib
import subprocess
from setuptools import setup, find_packages
from setuptools.command.install import install

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="jacfal-sensor-data-collector",
    version="0.0.1",
    description="Collects data from iot sensors and sent them to the defined targets",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Jacfal/SensorDataCollector",
    author="Jacfal",
    author_email="jacfal.tech@protonmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(),
    package_data={"jsdc": ["config.yml", "/etc/jdc/config.yml"]},
    include_package_data=True,
    entry_points={
        "console_scripts": ["jsdc=jsdc.sensor_data_collector:main", ]
    },
)
