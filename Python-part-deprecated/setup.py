import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="A9-windows-cliker",
    version="1.0.0",
    install_requires=requirements,
    author="Yaldabaoth444",
    author_email="gizar@inbox.ru",
    description="A9 setupable cliker (not only A9)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yaldabaoth444/Ashpalt9w",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
