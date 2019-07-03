# A Pascal Repl in Python

  This is a Pascal interpreter based off of the blog : [ruslanspivak.com](https://ruslanspivak.com/lsbasi-part1/)

## Directory Structure

  This project tries to contain all the documentation, source code, and build tests in the following way:

  ```
  doc/
  src/
    debug/
    interpreter/
    io/
  test/		
  ```

  - `doc/` : contains all the usage documentation, the project models, and the module APIs.
  - `src/` : contains the runnable package in all of its entirety which has the following modules:
    - `debug/` : this module contains all of the logging and debug reporting logic
    - `core/` : this module contains the backend logic for the interpreter, parser, and lexer 
    - `io/` : this module contains the frontend interface for users; :exclamation: NOTE `io` is a temp name
  - `test/` : contains the conformity and usability tests for each module

