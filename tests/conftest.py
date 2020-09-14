# -*- coding: utf-8 -*-

from zipfile import ZipFile

import pytest
from mimesis.enums import Gender
from mimesis.schema import Field, Schema
from yakutils import write_csv


def fake(items: int = 20):
    """Mimesis fake function using tutorial example."""

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


@pytest.fixture()
def zipfile_csv(tmp_path):
    """CSV file and directory creator."""

    d = tmp_path / "sub"

    d.mkdir()

    a_csv = d / "description.csv"

    write_csv(fake(), a_csv)

    a_zip = d / "description.zip"

    with ZipFile(a_zip, "w") as f:
        f.write(a_csv)

    return a_zip


@pytest.fixture(scope="module")
def zipfile_json(tmp_path_factory):
    """Random json file with data."""
    pass
