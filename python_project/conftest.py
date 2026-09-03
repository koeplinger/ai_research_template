"""Puts src/ on the import path for every test under python_project/.

Created 3 September 2026; updated 3 September 2026.

This is the entire test configuration. Check programs are not collected
by pytest: each is its own test and is run directly.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent / "src"))
