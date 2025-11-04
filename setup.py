"""Setup configuration for lethimcook package."""

from setuptools import find_packages, setup

setup(
    name="lethimcook",
    version="0.1.0",
    description="A Python library for unit conversions, especially for cooking",
    author="",
    packages=find_packages(),
    python_requires=">=3.11",
    install_requires=["pydantic>=2.0.0"],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
        ],
    },
)
