import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sra_py",
    version="2.0.1",
    author="Atidipt123",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Atidipt123/sra_py",
    project_urls={
        "Bug Tracker": "https://github.com/Atidipt123/sra_py/issues",
    },
    package_dir={"": "sra_py"},
    packages=setuptools.find_packages(where="sra_py"),
    python_requires=">=3.6",
)
