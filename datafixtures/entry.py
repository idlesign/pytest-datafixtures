from pathlib import Path
from typing import Optional

import pytest

if False:  # pragma nocover
    from _pytest.fixtures import SubRequest  # noqa


@pytest.fixture
def datafix_dir(request: 'SubRequest') -> Path:
    """Returns data fixtures directory (as Path object) for test."""
    return Path(request.module.__file__).absolute().parent / 'datafixtures'


@pytest.fixture
def datafix(datafix_dir: Path, request: 'SubRequest') -> Path:
    """Returns data fixture Path object for current test."""
    return datafix_dir / request.node.name


@pytest.fixture
def datafix_read(datafix_dir: Path, request: 'SubRequest'):
    """Returns text from the data fixture by it's name."""

    testname = request.node.name

    def datafix_read_(fname: str = None, *, encoding: Optional[str] = None) -> str:
        fname = fname or testname
        return (datafix_dir / fname).read_text(encoding=encoding)

    return datafix_read_
