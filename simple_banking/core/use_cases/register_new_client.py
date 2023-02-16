"""Register new client in the application."""


import datetime
import uuid
from typing import Any, cast

import inject
from email_validator import EmailNotValidError, validate_email
from result import Err, Ok, Result
from use_case_registry import UseCaseRegistry
from use_case_registry.base import ICommand
from use_case_registry.errors import CommandInputValidationError

from simple_banking.core.exceptions import UnexpectedError
from simple_banking.core.models import Client
from simple_banking.core.services.email import EmailClient
from simple_banking.database.base import IRepository


class RegisterNewClient(ICommand):
    """
    Register new client in the application.

    This use case orchestrates the creation of a new client
    in the application.
    """

    def __init__(  # noqa: D107
        self,
        email: str,
        name: str,
        last_name: str,
        password: str,
        birthday_date: datetime.date,
    ) -> None:
        self.email = email
        self.name = name
        self.last_name = last_name
        self.password = password
        self.birthday_date = birthday_date

        self.email_service = EmailClient()
        self.repository = cast(IRepository, inject.instance(IRepository))

    def validate(self) -> Result[None, CommandInputValidationError]:
        """Validate input commands."""
        try:
            validate_email(email=self.email)
        except EmailNotValidError:
            return Err(CommandInputValidationError())

        if not self.name.isalpha() and not self.last_name.isalpha():
            return Err(CommandInputValidationError())

        return Ok()

    def execute(
        self, write_ops_registry: UseCaseRegistry[Any]
    ) -> Result[Any, Exception]:
        """Execute register new client workflow."""
        client = Client(
            client_id=uuid.uuid4(),
            email=self.email,
            name=self.name,
            last_name=self.last_name,
            password=self.password,
            birthday_date=self.birthday_date,
        )

        self.repository.insert_client(
            new_client=client,
            write_operations=write_ops_registry,
        )

        commited = self.repository.commit_write_transaction(
            write_operations=write_ops_registry
        )
        commited_err = commited.err()
        if commited_err is not None:
            return Err(UnexpectedError(unexpected_error=commited_err))

        email_sent = self.email_service.send_email(
            to_email=client.email,
            msg="You registration has been completed!",
        )

        email_sent_err = email_sent.err()
        if email_sent_err is not None:
            return Err(UnexpectedError(unexpected_error=email_sent_err))

        return Ok()
