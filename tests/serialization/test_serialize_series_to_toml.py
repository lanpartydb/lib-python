"""
:Copyright: 2024-2025 Jochen Kupperschmidt
:License: MIT
"""

from textwrap import dedent

import pytest

from lanpartydb.models import Series
from lanpartydb.serialization import serialize_series_to_toml


@pytest.mark.parametrize(
    ('series', 'expected'),
    [
        (
            Series(
                slug='gammalan',
                title='GammaLAN',
                alternative_titles=[],
                country_codes=['ca', 'us'],
            ),
            dedent("""\
            slug = "gammalan"
            title = "GammaLAN"
            country_codes = ["ca", "us"]
            """),
        ),
        (
            Series(
                slug='deltalan',
                title='DeltaLAN',
                alternative_titles=['Δ LAN', 'Δέλτα LAN'],
                country_codes=['au'],
            ),
            dedent("""\
            slug = "deltalan"
            title = "DeltaLAN"
            alternative_titles = ["Δ LAN", "Δέλτα LAN"]
            country_codes = ["au"]
            """),
        ),
    ],
)
def test_serialize_series_to_toml(series: Series, expected: str):
    assert serialize_series_to_toml(series) == expected
