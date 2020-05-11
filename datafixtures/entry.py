from pathlib import Path

import pytest

if False:  # pragma nocover
    from _pytest.fixtures import SubRequest  # noqa


@pytest.fixture
def datafix_dir(request: 'SubRequest') -> Path:
    """Returns data fixtures directory (as Path object) for test."""
    return Path(request.module.__file__).absolute().parent / 'datafixtures'


@pytest.fixture
def datafix(datafix_dir, request) -> Path:
    """Returns data fixture Path object for current test."""
    return datafix_dir / request.node.name
