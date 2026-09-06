# Tests

*Created 3 September 2026; updated 6 September 2026.*

The test suite for the foundation modules under `src/`: the shared code a
check imports, tested so that a check's verdict rests on a module known
to do what its docstring says. Check programs are not tested here; each
is its own test and its own verdict.

| File | Covers |
|---|---|
| [test_make_roll.py](test_make_roll.py) | the generator: every row a Tuesday or a fair, cancelled Tuesdays absent, rows sorted and unique |
