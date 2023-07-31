import pytest
from configparser import ConfigParser


def load_test_config():
    config = ConfigParser()
    config.read("tests/test_config.ini")
    return config

def pytest_addoption(parser):
    config = load_test_config()
    db_choices = list(config.sections())[1:]
    db_choices_str = ", ".join(db_choices)
    parser.addoption(
        "--db-type",
        action="store",
        default="sqlite",
        choices=db_choices,
        help=f"Specify the database type to use for testing. Available choices: {db_choices_str} (default: sqlite).",
    )
