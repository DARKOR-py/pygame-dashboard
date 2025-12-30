from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pygame-dashboard",
    version="0.1.0",
    author="Robinson Petit",
    author_email="robinson@argil.fr",
    description="A simple UI library for pygame projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/pygame-dashboard",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: pygame",
    ],
    python_requires=">=3.7",
    install_requires=[
        "pygame>=2.0.0",
    ],
    keywords="pygame ui dashboard panel widgets",
)