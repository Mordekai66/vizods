from setuptools import setup, find_packages

setup(
    name="vizods",
    version="1.0.0",
    author="Abdelrahman Ali",
    author_email="abdelrahman.ali.dev@gmail.com",
    description="A Python library for visualizing Data Structures and Algorithms with images and videos",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Mordekai66/vizods",
    project_urls={
        "Bug Tracker": "https://github.com/Mordekai66/vizods/issues",
        "Documentation": "https://github.com/Mordekai66/vizods#readme",
        "Source Code": "https://github.com/Mordekai66/vizods",
    },
    packages=find_packages(),
    include_package_data=True,
    package_data={"InnoCaptcha": ["**/*"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Education",
        "Topic :: Scientific/Engineering :: Visualization",
    ],
    python_requires='>=3.8',
    install_requires=[
        "matplotlib>=3.5.0",
        "imageio>=2.20.0",
        "imageio-ffmpeg>=0.4.7",
        "networkx>=2.8.0",
        "numpy>=1.21.0",
    ],
)
