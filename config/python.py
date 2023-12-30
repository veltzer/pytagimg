from typing import List


console_scripts: List[str] = [
    "pytagimg=pytagimg.main:main",
]
config_requires: List[str] = []
dev_requires = [
    "pypitools",
]
make_requires: List[str] = [
    "pyclassifiers",
    "pydmt",
    "pymakehelper",
]
install_requires: List[str] = [
    "pytconf",
    "pylogconf",
]
test_requires: List[str] = [
    "pylint",
    "pytest",
    "pytest-cov",
    "pyflakes",
    "flake8",
    "mypy",
]
requires = config_requires + install_requires + make_requires + test_requires
