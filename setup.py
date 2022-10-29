from setuptools import setup, PEP420PackageFinder

setup(
    name="qpythonic",
    version="0.0.1",
    packages=PEP420PackageFinder.find("src/python"),
    package_dir={"": "src/python"},
    classifiers=[
        "Intendend Audience :: Science/Research",
        "Development Status :: 0 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering :: Statistics",
    ],
)
