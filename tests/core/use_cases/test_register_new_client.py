"""Test use case register_new_client."""

import datetime
import uuid
from typing import Any

from use_case_registry import UseCaseRegistry
from use_case_registry.errors import CommandInputValidationError
from simple_banking.core.models import Client
from simple_banking.core.use_cases.register_new_client import RegisterNewClient
import pytest


class TestRegisterNewClient:
    """Set of test definitions around the RegisterNewClient use case."""

    def test_input_validation_pass(self) -> None:
        """Test use case inputs pass."""
        register_new_client = RegisterNewClient(
            email="name.last_name@factored.ai",
            name="Peter",
            last_name="Parker",
            password="123",  # noqa: S106
            birthday_date=datetime.date(year=2000, month=1, day=1),
        )
        register_new_client.validate().unwrap()

    @pytest.mark.parametrize(
        argnames="inputs",
        argvalues=[
            {
                "email": "not_an_email",
                "name": "Peter",
                "last_name": "Parker",
                "password": 123,
                "birthday_date": datetime.date(year=2000, month=1, day=1),
            },
            {
                "email": "name.last_name@factored.ai",
                "name": "Peter123",
                "last_name": "Parker@",
                "password": 123,
                "birthday_date": datetime.date(year=2000, month=1, day=1),
            },
        ],
    )
    def test_input_validation_not_pass(self, inputs: dict[str, Any]) -> None:
        """Test use case inputs fail to pass."""
        register_new_client = RegisterNewClient(**inputs)
        err = register_new_client.validate().err()
        assert isinstance(err, CommandInputValidationError)

    def test_register_a_new_client(self) -> None:
        """Test register a new client when does not exists in the application."""
        register_new_client = RegisterNewClient(
            email="not_valid_email",
            name="Peter",
            last_name="Parker",
            password="123",  # noqa: S106
            birthday_date=datetime.date(year=2000, month=1, day=1),
        )

        register_new_client.execute(
            write_ops_registry=UseCaseRegistry[Any](max_length=10),
        ).unwrap()

        created_client = register_new_client.repository.get_client(
            email="not_valid_email"
        ).unwrap()

        assert created_client
        assert created_client.email == "not_valid_email"
        assert created_client.name == "Peter"
        assert created_client.last_name == "Parker"
        assert created_client.birthday_date == datetime.date(year=2000, month=1, day=1)

    def test_cannot_register_a_client_that_already_exists(self) -> None:
        """
        Test a register new client fails if user already exists.

        Definition of an already existing client is that email already exists.
        """
        register_new_client = RegisterNewClient(
            email="existing_email",
            name="Peter",
            last_name="Parker",
            password="123",  # noqa: S106
            birthday_date=datetime.date(year=2000, month=1, day=1),
        )
        write_operations = UseCaseRegistry[Any](max_length=10)
        register_new_client.repository.insert_client(
            new_client=Client(
                client_id=uuid.uuid4(),
                email="existing_email",
                name="name",
                last_name="last_name",
                password="123",  # noqa: S106
                birthday_date=datetime.date(year=2000, month=1, day=1),
            ),
            write_operations=write_operations,
        )

        register_new_client.repository.commit_write_transaction(
            write_operations=write_operations
        ).unwrap()

        register_new_client.execute(write_ops_registry=write_operations).unwrap()
