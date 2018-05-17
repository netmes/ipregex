import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--run-slow", action="store_true", default=False,
        help="Run slow tests.")
    parser.addoption(
        "--skip-exhaustive", action="store_true", default=False,
        help="Skip exhaustive tests.")

def pytest_collection_modifyitems(config, items):
    if not config.getoption("--run-slow"):
        skip_slow = pytest.mark.skip(reason="Need --run-slow option to run.")
        for item in items:
            if "slow" in item.keywords:
                item.add_marker(skip_slow)
    if config.getoption("--skip-exhaustive"):
        skip_exhaustive = pytest.mark.skip(
            reason="Skipping due to --skip-exhaustive option.")
        for item in items:
            if "exhaustive" in item.keywords:
                item.add_marker(skip_exhaustive)
