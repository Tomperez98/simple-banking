"""Application configuration."""


import inject

from simple_banking.core.services import email
from simple_banking.database import config


def dependency_injection(binder: inject.Binder) -> None:
    """Configure dependency injection for the application."""
    binder.install(
        config=email.config.dependency_injection,
    ).install(
        config=config.dependency_injection,
    )
