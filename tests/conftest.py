# -*- coding: utf-8 -*-

import pytest
from mimesis.enums import Gender
from mimesis.schema import Field, Schema
from yakutils import write_csv


def fake(items: int = 20):
    """Mimesis fake function using tutorial example"""

    _ = Field("en")

    description = lambda: {
        "id": _("uuid"),
        "name": _("text.word"),
        "version": _("version", pre_release=True),
        "timestamp": _("timestamp", posix=False),
        "owner": {
            "email": _(
                "person.email",
                domains=["test.com", "yahoo.com"],
                key=str.lower,
            ),
            "token": _("token_hex"),
            "creator": _("full_name", gender=Gender.FEMALE),
        },
    }
    schema = Schema(schema=description)
    return schema.create(iterations=items)


@pytest.fixture(scope="module")
def zipfile_csv(tmp_path_factory):
    """CSV file and directory creator"""

    mydir = tmp_path_factory.mkdir("mydir")

    a_csv = mydir / "description.csv"

    write_csv(fake(), a_csv)

    return a_csv


@pytest.fixture(scope="module")
def zipfile_json(tmp_path_factory):
    """Random json file with data."""
    pass
