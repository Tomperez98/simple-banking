"""RestAPI root app."""
from typing import Any

import fastapi
import inject
from fastapi.responses import ORJSONResponse
from use_case_registry import UseCaseRegistry

from simple_banking.api.models.register_new_client import RegisterNewClientRequest
from simple_banking.core.config import (
    dependency_injection,
)
from simple_banking.core.use_cases import RegisterNewClient

inject.configure_once(dependency_injection)
app = fastapi.FastAPI()


@app.post(path="/client/register-new")
async def register_new_client(request: RegisterNewClientRequest) -> fastapi.Response:
    """Register a new client in the application."""
    write_ops_registry = UseCaseRegistry[Any](max_length=10)
    register_new_client = RegisterNewClient(
        email=request.email,
        name=request.name,
        last_name=request.last_name,
        password=request.password,
        birthday_date=request.birthday_date,
    )
    validated = register_new_client.validate()
    validated_err = validated.err()
    if validated_err is not None:
        return ORJSONResponse(
            content="Arguments are not valid.",
            status_code=fastapi.status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
    success = register_new_client.execute(write_ops_registry=write_ops_registry)
    success_err = success.err()
    if success_err is not None:
        return ORJSONResponse(
            content="Something went wrong.",
            status_code=fastapi.status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    return ORJSONResponse(content="New client has been registered.")
