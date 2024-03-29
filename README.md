# A Pascal Repl in Python

  This is a Pascal interpreter based off of the blog : [ruslanspivak.com](https://ruslanspivak.com/lsbasi-part1/)

## Directory Structure

  This project tries to contain all the documentation, source code, and build tests in the following way:

  ```
  doc/
  src/
    main/
    test/
  test/
  ```

  - `doc/` : contains all the usage documentation, the project models, and the module APIs.
  - `src/` : contains the runnable package in all of its entirety which has the following modules:
    - `main/` : this module contains the backend logic for the interpreter, parser, and lexer.  It
       also contains the entry point for running the program. 
    - `test/` : this module contains all of the unit tests and the likes
  - `test/` : contains the conformity and usability tests for each module

## Running the Package

  There are three way to utilize the package:
  1. Interactively via a cli : `python -m pascal-repl`
  