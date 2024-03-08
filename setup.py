import re

import setuptools

with open("README.md", encoding="utf8") as f:
    long_description = f.read()

with open("requirements.txt", encoding="utf8") as f:
    dependencies = f.read()

with open("exaroton/__init__.py", encoding="utf-8") as f:
    version = re.findall(r"__version__ = \"(.+)\"", f.read())[0]


setuptools.setup(
    name="Exaroton Expanded",
    version=version,
    description="An effort to continue and add to the exaroton library for Minecraft server hosting",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GalacticalEdge/exaroton-expanded",
    author="GalacticalEdge",
    author_email="galacticaledge@protonmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Internet",
        "Topic :: Games/Entertainment",
    ],
    keywords="exaroton minecraft api wrapper",
    project_urls={"Issue Tracker": "https://github.com/GalacticalEdge/exaroton-expanded"},
    # package_dir={"": "exaroton-expanded"},
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=dependencies,
)
