import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SciDataTool",
    version="0.0.1",
    author="Helene Toubin",
    author_email="helene.toubin@eomys.com",
    description="Scientific Data Tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Eomys/SciDataTool",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Apache License v2.0",
        "Operating System :: OS Independent",
    ],
    python_requires=">=2.7",
    install_requires=["numpy","scipy","matplotlib"]
)