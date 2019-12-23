import pathlib
from setuptools import setup


HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()
setup(
    name="aws-ic",
    version="1.0.0",
    scripts=['aws-ic/aws-ic'],
    description="A wrapper for EC2 Instance Connect to make a ssh connection to keyless EC2 instances more streamlined and secure.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/johnbarney/aws-ic",
    author="John Barney",
    author_email="john.barney@johnbarney.co",
    license="Apache 2.0",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["aws-ic"],
    include_package_data=True,
    install_requires=["cryptography", "boto3"],
)
