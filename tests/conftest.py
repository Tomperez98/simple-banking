"""Root conftest for unittesting."""

from collections.abc import Generator

import inject
import pytest

from simple_banking.core.services.email.api import FakeApiEmail
from simple_banking.core.services.email.api.base import IApiEmail
from simple_banking.database import InMemoryRepository
from simple_banking.database.base import IRepository


@pytest.fixture(autouse=True)
def _dependency_injection() -> Generator[None, None, None]:
    """Configure dependency injection fot unittesting."""
    inject.clear()
    inject.configure(
        config=lambda binder: binder.bind(  # type: ignore[arg-type]
            cls=IApiEmail,
            instance=FakeApiEmail(),
        ).bind(
            cls=IRepository,
            instance=InMemoryRepository(),
        )
    )
    yield
    inject.clear()
