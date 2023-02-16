"""Loan model."""

import dataclasses
import decimal
import uuid

import polars as pl


@dataclasses.dataclass
class Loan:
    """Loan representation in the application core domain."""

    loan_id: uuid.UUID
    amount: decimal.Decimal
    interest_rate: decimal.Decimal
    periods: int
    cashflows: pl.DataFrame
