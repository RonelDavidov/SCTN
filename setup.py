from setuptools import setup, find_packages

VERSION = '0.1.1'
DESCRIPTION = 'Spiking Continues Time Neuron'
LONG_DESCRIPTION = 'A Spiking Neural Network implementation using '


def parse_requirements(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines if line and not line.startswith("#")]
        return lines


# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="sctn",
    version=VERSION,
    author="Yakir Hadad",
    author_email="yakir4123@email.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=parse_requirements('requirements.txt'),
    keywords=['python', 'snn', 'ai'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
    ],
    dependency_links=[
        'git+https://github.com/BindsNET/bindsnet.git#egg=bindsnet'
    ]
)