# Solutions to [Project Euler](https://projecteuler.net) problems in Python3

## Requirements
* Python3

## Repo structure and naming
`src/`: the source modules grouped under one package.

`tests/`: unit test files.

Each source module is the solution to one question from the project. Source modules are numbered according to corresponding problem number in [Project Euler](https://projecteuler.net).

Each source module has its own test file. Test file names follow Python test discovery convention. For example, `test_p001.py` is the test file for `p001.py`.

## How to import source modules
Source modules are grouped under a package called `src` and can be imported from repo's root directory as:

```
from src import p1
```

## How to run the unit tests
To run all tests, from root of the repo run:

```
python -m unittest
```

To run a specific test file such as `test_p001.py`:

```
python -m unittest tests/test_p1.py
```
