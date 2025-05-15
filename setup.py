from setuptools import setup, find_packages
from pathlib import Path

long_description = (Path(__file__).parent / 'README.md').read_text()

setup(
    name='PyOverlayKit',
    version='0.4.0',
    description='Always-on-top overlays for PyQt and PySide.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/puff-dayo/PyOverlayKit',
    packages=find_packages(),
    install_requires=[
        'pyqtgraph', 
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10.6', 
    project_urls={
        'Repository': 'https://github.com/puff-dayo/PyOverlayKit',
    },
)
