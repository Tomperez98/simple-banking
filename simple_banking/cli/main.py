"""CLI entrypoint."""

import datetime
import sys
from typing import Any

import click
import inject
from use_case_registry import UseCaseRegistry

from simple_banking.core.config import (
    dependency_injection,
)
from simple_banking.core.use_cases import RegisterNewClient

inject.configure_once(dependency_injection)


@click.group()
def cli() -> None:
    """CLI root group."""


@cli.command()
@click.argument("email")
@click.argument("name")
@click.argument("last_name")
@click.argument("password")
@click.argument("birthday_date")
def register_new_user(
    email: str,
    name: str,
    last_name: str,
    password: str,
    birthday_date: datetime.date,
) -> None:
    """Register a new client in the application."""
    register_new_client = RegisterNewClient(
        email=email,
        name=name,
        last_name=last_name,
        password=password,
        birthday_date=birthday_date,
    )
    validated = register_new_client.validate()
    validated_err = validated.err()
    if validated_err is not None:
        click.echo(message="Arguments are not valid.")
        sys.exit(1)

    write_ops_registry = UseCaseRegistry[Any](max_length=10)
    success = register_new_client.execute(write_ops_registry=write_ops_registry)
    success_err = success.err()
    if success_err is not None:
        click.echo(message="Something went wrong.")
        sys.exit(1)
