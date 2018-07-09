# Solutions to [Project Euler](https://projecteuler.net) problems in Python3
(being updated daily)

## Repo structure and naming
`src/`: the source modules grouped under one package.

`tests/`: unit test files.

Each source module is the solution to one question from the project. Source modules are numbered according to corresponding problem number in [Project Euler](https://projecteuler.net).

Each source module has its own test file. Test file names follow Python test discovery convention: a `test_` prefix is added to source module name. For example, `test_p1.py` is the test file for `p1.py`.

## How to import source modules
Source modules are grouped under a package called `src` and can be imported from a parent directory as:

```
from src import p1
```

or

```
import src.p1
```

## How to run the unit tests
To run all tests, simply use Python test dicovery (from root of the repo):

```
python -m unittest
```

For a specific test file such as `test_p1.py`, run (from root of the repo):

```
python -m unittest tests/test_p1.py
```
