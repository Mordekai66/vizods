from setuptools import setup, find_packages
from pathlib import Path

# Read long description from README
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="vizods",
    version="2.3.0",
    author="Abdelrahman Ali",
    author_email="abdelrahman.ali.dev@gmail.com",
    description="The ultimate Python toolkit for animating Data Structures and Algorithms.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Mordekai66/vizods",
    project_urls={
        "Homepage": "https://github.com/Mordekai66/vizods",
        "Bug Tracker": "https://github.com/Mordekai66/vizods/issues",
        "Documentation": "https://github.com/Mordekai66/vizods#readme",
        "Source Code": "https://github.com/Mordekai66/vizods",
        "Changelog": "https://github.com/Mordekai66/vizods/releases",
    },
    packages=find_packages(exclude=["tests", "tests.*", "examples", "examples.*"]),
    include_package_data=True,
    package_data={"vizods": ["**/*"]},
    keywords=[
        "visualization", "data-structures", "algorithms", "sorting",
        "binary-search-tree", "dijkstra", "linked-list", "education",
        "animation", "matplotlib", "networkx", "teaching", "computer-science"
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Education",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=[
        "matplotlib>=3.5.0",
        "imageio>=2.20.0",
        "imageio-ffmpeg>=0.4.7",
        "networkx>=2.8.0",
        "numpy>=1.21.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=22.0.0",
            "flake8>=5.0.0",
        ],
    },
)
