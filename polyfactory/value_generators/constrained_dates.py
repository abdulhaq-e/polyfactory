from __future__ import annotations
from datetime import date, timedelta, datetime, timezone
from typing import TYPE_CHECKING, cast


if TYPE_CHECKING:
    from faker import Faker


def handle_constrained_date(
    faker: Faker,
    ge: date | None = None,
    gt: date | None = None,
    le: date | None = None,
    lt: date | None = None,
) -> date:
    """Generates a date value fulfilling the expected constraints.

    :param faker: An instance of faker.
    :param lt: Less than value.
    :param le: Less than or equal value.
    :param gt: Greater than value.
    :param ge: Greater than or equal value.

    :returns: A date instance.
    """
    start_date = datetime.now(tz=timezone.utc).date() - timedelta(days=100)
    if ge:
        start_date = ge
    elif gt:
        start_date = gt + timedelta(days=1)

    end_date = datetime.now(tz=timezone.utc).date() + timedelta(days=100)
    if le:
        end_date = le
    elif lt:
        end_date = lt - timedelta(days=1)

    return cast("date", faker.date_between(start_date=start_date, end_date=end_date))
