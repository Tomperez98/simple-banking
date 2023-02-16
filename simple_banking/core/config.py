"""Application configuration."""


import inject

from simple_banking import database
from simple_banking.core.services import email


def dependency_injection(binder: inject.Binder) -> None:
    """Configure dependency injection for the application."""
    binder.install(
        config=email.config.dependency_injection,
    ).install(
        config=database.config.dependency_injection,
    )
